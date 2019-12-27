import requests
import lxml
from lxml import html
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.styles import Font
from openpyxl.chart import LineChart
from openpyxl.chart import Reference
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart.axis import DateAxis
from utils import *
# from utils import dataPlacer
# from utils import imagePlacer
# from utils import graphPlacer
# from utils import defaultKeyStatisticsChoices
# from utils import defaultsummaryDetailChoices
from yfinance.utils import get_json 
import yfinance as yf
from datetime import datetime


class excelReport:

    def excelWriter(self, tickers, filename):
        wb = Workbook()
        stockData = yf.download(tickers, period='10y')['Adj Close']
        stockData = stockData[tickers]
        wb.create_sheet(title='Stock Data')
        stockSheet = wb['Stock Data']

        for row in dataframe_to_rows(stockData, index=True, header=True):
            stockSheet.append(row)
    
        minCol = 1
        minRow = 3
        maxCol = 1

        for ticker in tickers:
            excelReport.collectData(self,ticker)

            wb.create_sheet(title=ticker)
            sheet = wb[ticker]
            sheet.sheet_view.showGridLines = False

            sheet['B2'].value = self.tickerName
            sheet['B2'].font = Font(bold=True)
            sheet['B2'].alignment = Alignment(horizontal='center')
            sheet.merge_cells('B2:N2')

            sheet['B3'].value = self.businessSummary
            sheet['B3'].alignment = Alignment(wrap_text=True,vertical='center', horizontal='center')
            sheet.merge_cells('B3:N3')
            sheet.row_dimensions[3].height = 100

            sheet['B5'].value = "Sector Holdings"
            sheet['B5'].font = Font(bold=True)

            sheet['E5'].value = "Company Holdings"
            sheet['E5'].font = Font(bold=True)

            sheet['H5'].value = "Risk Statistics"
            sheet['H5'].font = Font(bold=True)
            sheet['H5'].alignment = Alignment(horizontal='center')
            sheet.merge_cells('H5:M5')

            sheet['L18'].value = "Annual Returns"
            sheet['L18'].font = Font(bold=True)

            sheet['B18'].value = 'Key Characteristics'
            sheet['B18'].font = Font(bold=True)

            dataPlacer(self.sectorHoldings,sheet,6,2, 'B','C')
            dataPlacer(self.companyHoldings,sheet,6,5,'E','F')
            dataPlacer(self.annualReturns,sheet,19,12,'L','M',False)
            dataPlacer(self.keyCharacteristics,sheet,19,2,'B','C',False,'left',False)

            try:
                dataPlacer(self.riskData['3y'],sheet,6,8,'H','I',False,'right')
                dataPlacer(self.riskData['5y'],sheet,6,10,'J','K',False,'right')
                dataPlacer(self.riskData['10y'],sheet,6,12,'L','M',False,'right')
            except:
                None
    
            imagePlacer(self.imageURL, sheet,'B26')
            graphPlacer(ticker,stockSheet,stockData,sheet,minCol,minRow,maxCol)
            minCol += 1
            maxCol += 1

        wb.save(filename)

    def collectData(self, ticker):
        url = "https://finance.yahoo.com/quote/" + ticker
        data = get_json(url)

        fundPerformance = data['fundPerformance']
        topHoldings = data['topHoldings']
        defaultKeyStatistics = data['defaultKeyStatistics']
        summaryDetail = data['summaryDetail']

        self.tickerName = data['quoteType']['longName']
        self.businessSummary = data['assetProfile']['longBusinessSummary']

        sectorData = topHoldings['sectorWeightings']
        self.sectorHoldings = {}

        for sector in sectorData:
            for key, value in sector.items():
                self.sectorHoldings[key] = str(round(value * 100, 2)) + '%'

        companyData = topHoldings['holdings']
        self.companyHoldings = {}

        for company in companyData:
            self.companyHoldings[company['holdingName']] = str(round(company['holdingPercent'] * 100, 2)) + '%'

        annualReturnsData = fundPerformance['annualTotalReturns']['returns']
        self.annualReturns = {}

        for returns in annualReturnsData:
            if returns['annualValue'] == None:
                self.annualReturns[returns['year']] = "N/A"
            else:
                self.annualReturns[returns['year']] = str(round(returns['annualValue'] * 100, 2)) + '%'

        riskStatistics = fundPerformance['riskOverviewStatistics']['riskStatistics']
        self.riskData = {}

        for risk in riskStatistics:
            self.riskData[risk['year']] = risk

        self.imageURL = data['fundProfile']['styleBoxUrl']

        self.keyCharacteristics = {}

        for option in defaultKeyStatisticsChoices:
            if option == 'fundInceptionDate':
                self.keyCharacteristics[option] = defaultKeyStatistics[option]
                self.keyCharacteristics[option] = datetime.fromtimestamp(self.keyCharacteristics[option]).strftime('%Y-%m-%d')
            else:
                self.keyCharacteristics[option] = defaultKeyStatistics[option]

        for option in defaultsummaryDetailChoices:
            self.keyCharacteristics[option] = summaryDetail[option]


