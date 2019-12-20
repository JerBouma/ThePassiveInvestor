from tkinter import *
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
        
        Button(self, text="Get", command=self.get_data).grid(row=10,column=1)

        self.Ticker = StringVar()
        self.entry_widget = Entry(self, textvariable=self.Ticker).grid(row=10,column=2)
        
    def get_data(self):
        import yfinance as yf
        import options

        ticker = self.Ticker.get()

        if ticker:
            print(1)
            tickerData = yf.Ticker(ticker)
            print(tickerData.balance_sheet)
        else:
            tickerData = options.tickerData

        intervalChoice = options.interval[self.intervalChoice.get()]
        periodChoice = options.period[self.periodChoice.get()]

        if self.historicChoice.get() == 1:
            print(tickerData.history(period=periodChoice, interval=intervalChoice))

        for choice in self.data:
            if self.data[choice].get() == 1:
                if choice in options.mainVariables: 
                    print(options.mainVariables[choice])
                elif choice in options.extraVariables:
                    print(options.extraVariables[choice])
        
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
root.geometry("375x250")
app = Window(root)
root.mainloop()