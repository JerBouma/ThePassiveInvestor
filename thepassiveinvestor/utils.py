import io

import urllib3
from openpyxl.chart import Reference, LineChart
from openpyxl.chart.axis import DateAxis
from openpyxl.drawing.image import Image as ExcelImage
from openpyxl.styles import Alignment, Font
from openpyxl.styles.numbers import FORMAT_PERCENTAGE_00


def data_placer(data, sheet, starting_row, column, column_key, column_value, horizontal_alignment_key=False,
                horizontal_alignment_value=False, change_key_dimensions=True, change_value_dimensions=True,
                value_formatting_style=None):
    """
    Description
    ----
    This function places data in the given Excel sheet based on the positions given.

    Input
    ----
    data (dictionary):
        The data that is filled into the sheet.
    sheet (object):
        The sheet that is filled within the Workbook.
    starting_row (integer or float):
        The first row the data is placed.
    column (integer or float):
        The column that is filled in.
    column_key (string):
        Which column the key of the dictionary is placed.
    column_value (string):
        Which columns the value of the dictionary is placed.
    horizontal_alignment_key (boolean, default is False):
        Align the key of the dictionary horizontally.
    horizontal_alignment_value (boolean, default is False):
        Align the value of the dictionary horizontally.
    change_key_dimensions (boolean, default is True):
        Increase the width of the cell of the key of the dictionary.
    change_value_dimensions (boolean, default is True):
        Increase the width of the cell of the key of the dictionary.
    value_formatting_style (string, default is None):
        Option to change the formatting style of the value. Currently only works with 'percentage'.

    Output
    ----
    Fills in the sheet with the data based on the parameters.
    """
    max_length_key = 0
    max_length_value = 0

    for key, value in data.items():
        if value_formatting_style == 'percentage':
            try:
                value = float(value[:-1]) / 100
                sheet[f"{column_value}{starting_row}"].number_format = FORMAT_PERCENTAGE_00
            except ValueError:
                pass

        key_position = sheet.cell(column=column, row=starting_row, value=key)
        value_position = sheet.cell(column=column + 1, row=starting_row, value=value)

        starting_row += 1

        if horizontal_alignment_key:
            key_position.alignment = Alignment(horizontal=horizontal_alignment_key)

        if horizontal_alignment_value:
            value_position.alignment = Alignment(horizontal=horizontal_alignment_value)

        length_key = len(str(key_position.value))
        length_value = len(str(value_position.value))

        if length_key > max_length_key:
            max_length_key = length_key

        if length_value > max_length_value:
            max_length_value = length_value

    if change_key_dimensions:
        sheet.column_dimensions[column_key].width = max_length_key * 1.2

    if change_value_dimensions:
        sheet.column_dimensions[column_value].width = max_length_value * 1.2


def image_placer(image_url, sheet, location):
    """
    Description
    ----
    This function places an image in the given Excel sheet based on the location given.

    Input
    ----
    image_url (string):
        The data that is filled into the sheet.
    sheet (object):
        The sheet that is filled within the Workbook.
    location (string):
       The exact location the graph should be placed.

    Output
    ----
    Fills in the sheet with the selected image at the specified location.
    """
    try:
        http = urllib3.PoolManager()
        image_location = http.request('GET', image_url)
        image_file = io.BytesIO(image_location.data)
        image = ExcelImage(image_file)
        sheet.add_image(image, location)
    except Exception:
        sheet[location] = "No image available"
        sheet[location].font = Font(italic=True)


def graph_placer(stock_sheet, stock_data, sheet, min_col, min_row, max_col, location):
    """
    Description
    ----
    This function places a stock data graph at a specified location.

    Input
    ----
    stock_sheet (object):
        A sheet filled with stock data.
    stock_data (DataFrame):
        All stock data where the right position is determined automatically.
    sheet (string):
        A sheet that is filled in.
    min_col (integer):
        The minimum column of the stock sheet where the data starts.
    min_row (integer):
        The minimum row of the stock sheet where the data starts.
    max_col (integer):
        The maximum column available in the stock sheet.

    Output
    ----
    Fills in the sheet with the selected graph at the specified location.
    """
    data = Reference(stock_sheet, min_col=min_col + 1, min_row=min_row, max_col=max_col + 1, max_row=len(stock_data))
    cats = Reference(stock_sheet, min_col=1, min_row=3, max_col=1, max_row=len(stock_data))

    chart = LineChart()
    chart.title = None
    chart.legend = None
    chart.y_axis.title = "Stock Price"
    chart.y_axis.crossAx = 500
    chart.x_axis = DateAxis()
    chart.x_axis.number_format = 'yyyy'
    chart.x_axis.title = "Date"

    chart.add_data(data)
    chart.set_categories(cats)

    sheet.add_chart(chart, location)
