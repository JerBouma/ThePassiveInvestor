import requests
import lxml
from lxml import html
import pandas as pd
from openpyxl.chart import Reference
from openpyxl.chart import LineChart
from openpyxl.chart.axis import DateAxis
from openpyxl.styles import Alignment
from openpyxl.drawing.image import Image
from openpyxl.styles import Font
from PIL import ImageTk
from PIL import Image
import io
import urllib3

def symbolCollector(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    table = tree.xpath('//table')
    symbol = pd.read_html(lxml.etree.tostring(table[0],method='html'))
    symbol = symbol[0]['Symbol'].to_list()

    return symbol

def dataPlacer(data,sheet, startingRow, column, columnKey,
    columnValue, horizonalAlignmentKey=False, horizonalAlignmentValue=False,
    changeKeyDimensions=True, changeValueDimensions=True):

    maxLengthKey = 0
    maxLengthValue = 0

    for key, value in data.items():
        keyPosition     = sheet.cell(column=column, row=startingRow, value=key)
        valuePosition   = sheet.cell(column=column+1, row=startingRow, value=value)
        startingRow += 1

        if horizonalAlignmentKey:
            keyPosition.alignment = Alignment(horizontal=horizonalAlignmentKey) 
        
        if horizonalAlignmentValue:
            valuePosition.alignment = Alignment(horizontal=horizonalAlignmentValue)

        lengthKey = len(str(keyPosition.value))
        lengthValue = len(str(valuePosition.value))

        if lengthKey > maxLengthKey:
            maxLengthKey = lengthKey

        if lengthValue > maxLengthValue:
            maxLengthValue = lengthValue

    if changeKeyDimensions == True:
        sheet.column_dimensions[columnKey].width    = maxLengthKey * 1.2
    
    if changeValueDimensions == True:
        sheet.column_dimensions[columnValue].width  = maxLengthValue * 1.2

def imagePlacer(imageURL, sheet, location):
    try:
        http = urllib3.PoolManager()
        imageLocation = http.request('GET',imageURL)
        imageFile = io.BytesIO(imageLocation.data)
        image = Image(imageFile)
        sheet.add_image(image,location)
    except:
        sheet[location] = "No image available"
        sheet[location].font = Font(italic=True)

def graphPlacer(ticker,stockSheet,stockData,
    sheet,minCol,minRow,maxCol):

    data = Reference(stockSheet, min_col=minCol+1, min_row=minRow, max_col=maxCol+1, max_row=len(stockData))
    cats = Reference(stockSheet, min_col=1, min_row=3, max_col=1, max_row=len(stockData))
            
    chart = LineChart()
    chart.title = ticker
    chart.legend = None
    chart.y_axis.title = "Stock Price"
    chart.y_axis.crossAx = 500
    chart.x_axis = DateAxis(crossAx=100)
    chart.x_axis.number_format = 'mm/yyyy'
    chart.x_axis.title = "Date"

    chart.add_data(data)
    chart.set_categories(cats)

    sheet.add_chart(chart, 'E18')

programImageURL = 'https://raw.githubusercontent.com/JerBouma/ThePassiveInvestor/master/Images/ThePassiveInvestorPNG.png'

def programImagepPlacer(url = programImageURL):
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    image = ImageTk.PhotoImage(image)
    return image

defaultKeyStatisticsChoices =  ['fundInceptionDate',
                                'category',
                                'totalAssets']

defaultsummaryDetailChoices =  ['currency',
                                'navPrice',
                                'previousClose']