from tkinter import *
from utils import symbolCollector
from report.excelReport import excelWriter
# from tkinter import filedialog

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.initWindow()
        
    def initWindow(self):
        self.master.title("The Passive Investor")
        self.pack(fill=BOTH, expand=1)

        filenameLabel = Label(self, text="Filename")
        filenameLabel.grid(row=1, column=1, sticky=W)
        screenerLabel = Label(self, text='ETF Screener URL')
        screenerLabel.grid(row=2, column=1, sticky=W)
        
        self.filenameEntry = StringVar()
        filenameEntry = Entry(self, textvariable=self.filenameEntry, width=100)
        filenameEntry.grid(row=1, column=2, sticky=W, pady=10)

        self.screenerEntry = StringVar()
        screenerEntry = Entry(self, textvariable=self.screenerEntry, width=100)
        screenerEntry.grid(row=2, column=2, sticky=W, pady=10)

        excelReportButton = Button(self, text="Create Report", command=self.generateReport)
        excelReportButton.grid(row=3,column=1, columnspan=2, sticky=W+E+N+S,padx=10, pady=10)

    def generateReport(self):
        screenerURL = self.screenerEntry.get()
        filename = self.filenameEntry.get()

        tickers = symbolCollector(screenerURL)
        excelWriter(self, tickers, filename)

root = Tk()
app = Window(root)
root.mainloop()