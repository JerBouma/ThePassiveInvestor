from tkinter import *
from tkinter import filedialog
import requests
import lxml
from lxml import html
import pandas as pd

import options

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.options()
        
    def init_window(self):
        self.master.title("The Passive Investor")
        self.pack(fill=BOTH, expand=1)
        
        Button(self, text="Get Data", command=self.getData).grid(row=11,column=2)
        Button(self, text="Manual Ticker selection (Excel)", command=self.chooseInput).grid(row=10,column=1)

        self.screener = StringVar()
        Entry(self, textvariable=self.screener).grid(row=12,column=1)

    def chooseInput(self):
        self.tickerList = filedialog.askopenfilename()
        self.ticker = pd.read_excel(self.tickerList)['Tickers'].to_list()
        
    def getData(self):
        import yfinance as yf
        import pandas as pd
        from options import mainVariables, extraVariables
        from output import excelOutput

        def symbolCollector(url):
            page = requests.get(url)
            tree = html.fromstring(page.content)
            table = tree.xpath('//table')
            self.ticker = pd.read_html(lxml.etree.tostring(table[0], method='html'))[0]['Symbol'].to_list()

        if self.screener.get():
            url = self.screener.get()
            symbolCollector(url)

        intervalChoice = options.interval[self.intervalChoice.get()]
        periodChoice = options.period[self.periodChoice.get()]

        if self.historicChoice.get() == 1:
            print(yf.download(self.ticker, period=periodChoice, interval=intervalChoice))

        if type(self.ticker) == list:
            excelData = {}
            for symbol in self.ticker:
                tickerData = yf.Ticker(symbol)
                try:
                    mainVariablesOptions    =  {mainVariables[0]    : tickerData.financials,
                                                mainVariables[1]    : tickerData.balance_sheet,
                                                mainVariables[2]    : tickerData.cashflow,
                                                mainVariables[3]    : tickerData.earnings,
                                                mainVariables[4]    : tickerData.dividends,
                                                mainVariables[5]    : tickerData.splits}

                    extraVariablesOptions   =  {extraVariables[0]   : tickerData.sustainability,
                                                extraVariables[1]   : tickerData.recommendations,
                                                extraVariables[2]   : tickerData.actions,
                                                extraVariables[3]   : tickerData.calendar,
                                                extraVariables[4]   : tickerData.options}

                    for choice in self.data:
                        if self.data[choice].get() == 1:
                            if choice in mainVariables: 
                                excelData[symbol,choice] = mainVariablesOptions[choice]
                            elif choice in extraVariables:
                                excelData[symbol,choice] = extraVariablesOptions[choice]
                except:
                    continue
        
    def options(self):

        self.data = {}
      
        Label(self,
             text="Historic Data",
             font="Bold").grid(row=1,
                               column=1,
                               sticky='W')
        
        self.historicChoice = IntVar()
        Checkbutton(self,
                    text="Historic Data",
                    variable=self.historicChoice).grid(row=2,
                                                  column = 1,
                                                  sticky = 'W')
        Label(self,
             text="Period").grid(row=3,
                               column=1,
                               sticky='W')
        
        self.periodChoice = StringVar(self)
        self.periodChoice.set('YTD')
        period = options.period
        
        OptionMenu(self, self.periodChoice, *period).grid(row=4,
                                                   column=1,
                                                    sticky="W")
        
        Label(self,
             text="Interval").grid(row=5,
                               column=1,
                               sticky='W')
        
        self.intervalChoice = StringVar(self)
        self.intervalChoice.set('1 Day')
        interval = options.interval
        
        OptionMenu(self, self.intervalChoice, *interval).grid(row=6,
                                                   column=1,
                                                    sticky="W")
        # Technical Analysis
        
        Label(self,
             text="Main Variables",
             font="Bold").grid(row=1,
                               column=2,
                               sticky='W')
        counter = 2
        mainVariables = options.mainVariables
        
        for option in mainVariables:
            self.data[option] = IntVar()
            Checkbutton(self,
                       text=option,
                       variable=self.data[option]).grid(row=counter,
                                                   column = 2,
                                                   sticky = 'W')
            counter += 1

        Label(self,
             text="Extra Variables",
             font="Bold").grid(row=1,
                                        column=3,
                                         sticky='W')
        counter = 2
        extraVariables = options.extraVariables
        
        for option in extraVariables:
            self.data[option] = IntVar()
            Checkbutton(self,
                       text=option,
                       variable=self.data[option]).grid(row=counter,
                                                   column = 3,
                                                   sticky = 'W')
            counter += 1
                    
root = Tk()
root.geometry("500x400")
app = Window(root)
root.mainloop()