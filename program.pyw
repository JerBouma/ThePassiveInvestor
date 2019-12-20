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
        
        Button(self, text="Get Data", command=self.get_data).grid(row=11,column=2)
        Button(self, text="Manual Ticker selection (Excel)", command=self.chooseInput).grid(row=10,column=1)

        self.screener = StringVar()
        Entry(self, textvariable=self.screener).grid(row=12,column=1)

        # self.tickerList = Variable()
        # self.tickerListEntry = Entry(self, textvariable = self.tickerList).grid(row=10,column=3)

    def chooseInput(self):
        self.tickerList = filedialog.askopenfilename()
        self.ticker = pd.read_excel(self.tickerList)['Tickers'].to_list()
        
    def get_data(self):
        import yfinance as yf
        import pandas as pd

        def symbolCollector(url="https://finance.yahoo.com/etfs"):
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
            for symbol in self.ticker:
                tickerData = yf.Ticker(symbol)
                try:
                    mainVariables       =  {'Financials'       : tickerData.financials,
                                            'Balance Sheet'    : tickerData.balance_sheet,
                                            'Cashflow'         : tickerData.cashflow,
                                            'Earnings'         : tickerData.earnings,
                                            'Dividends'        : tickerData.dividends,
                                            'Splits'           : tickerData.splits}

                    extraVariables      =  {'Sustainability'   : tickerData.sustainability,
                                            'Recommendations'  : tickerData.recommendations,
                                            'Actions'          : tickerData.actions,
                                            'Event Calendar'   : tickerData.calendar,
                                            'Options'          : tickerData.options}

                    for choice in self.data:
                        if self.data[choice].get() == 1:
                            if choice in mainVariables: 
                                print(mainVariables[choice])
                            elif choice in extraVariables:
                                print(extraVariables[choice])
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