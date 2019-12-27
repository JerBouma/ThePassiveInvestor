from tkinter import *
from utils import symbolCollector
from report import excelReport
from PIL import ImageTk
from PIL import Image
# from tkinter import filedialog

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.initWindow()
        
    def initWindow(self):

        def onClick(event):
            event.widget.delete(0,END)
            event.widget.insert(0,"")
            event.widget.config(fg='black')
    
        self.master.title("The Passive Investor")
        self.pack(fill=BOTH, expand=1)

        image = ImageTk.PhotoImage(Image.open(r"C:\Users\jerbo\Google Drive\Programming\Python\testing.png"))
        panel = Label(self, image = image)
        panel.image = image
        panel.grid(row=1,column=1, columnspan=2,sticky=W+E+N+S)

        filenameLabel = Label(self, text="Filename")
        filenameLabel.grid(row=2, column=1, sticky=E)
        screenerLabel = Label(self, text='ETF Screener URL')
        screenerLabel.grid(row=3, column=1, sticky=E)
        
        self.filenameEntry = StringVar()
        self.filenameEntryExample = "Example: C:\Documents\Investing\Output\BestETFs.xlsx"
        filenameEntry = Entry(self, textvariable=self.filenameEntry, width=100, fg='gray')
        filenameEntry.grid(row=2, column=2, sticky=W, pady=10, padx=10)
        filenameEntry.insert(0, self.filenameEntryExample)
        filenameEntry.bind('<FocusIn>', onClick)

        self.screenerEntry = StringVar()
        self.screenerEntryExample = "Example: https://finance.yahoo.com/etfs (or from https://finance.yahoo.com/screener/etf/new)"
        screenerEntry = Entry(self, textvariable=self.screenerEntry, width=100, fg='gray')
        screenerEntry.grid(row=3, column=2, sticky=W, pady=10, padx=10)
        screenerEntry.insert(0, self.screenerEntryExample)
        screenerEntry.bind('<FocusIn>', onClick)

        excelReportButton = Button(self, text="Create Report", command=self.generateReport,bg='#4a00a0',fg='white')
        excelReportButton.grid(row=4,column=1, columnspan=2, sticky=W+E+N+S,padx=10, pady=10)

    def generateReport(self):
        screenerURL = self.screenerEntry.get()
        filename = self.filenameEntry.get()

        tickers = symbolCollector(screenerURL)
        excelReport.excelWriter(self, tickers, filename)

root = Tk()
app = Window(root)
root.geometry('725x200')
root.mainloop()