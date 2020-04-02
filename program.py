from tkinter import *
from tkinter import messagebox
from report import excelReport
from PIL import ImageTk
from PIL import Image
import threading
from utils import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.initWindow()
        
    def initWindow(self):
        def onClick(event):
            if event.widget.get() == self.filenameEntryExample:
                event.widget.delete(0,END)
                event.widget.insert(0,"")
                event.widget.config(fg='black')
            elif event.widget.get() == self.screenerEntryExample:
                event.widget.delete(0,END)
                event.widget.insert(0,"")
                event.widget.config(fg='black')
    
        self.master.title("The Passive Investor")
        self.pack(fill=BOTH, expand=1)

        image = ImageTk.PhotoImage(Image.open(resourcePath("images\ThePassiveInvestorPNG.png")))
        panel = Label(self, image = image, bg=background)
        panel.image = image
        panel.grid(row=1,column=1, columnspan=2,sticky=W+E+N+S)

        filenameLabel = Label(self, text="Filename",bg=background)
        filenameLabel.grid(row=2, column=1, sticky=E)
        screenerLabel = Label(self, text='Tickers URL/File',bg=background)
        screenerLabel.grid(row=3, column=1, sticky=E)
        
        self.filenameEntry = StringVar()
        self.filenameEntryExample = "Example: C:\Documents\Investing\Output\S&P500_Output.xlsx"
        filenameEntry = Entry(self, textvariable=self.filenameEntry, width=100, fg=entryTextColour)
        filenameEntry.grid(row=2, column=2, sticky=W, pady=10, padx=10)
        filenameEntry.insert(0, self.filenameEntryExample)
        filenameEntry.bind('<FocusIn>', onClick)

        self.screenerEntry = StringVar()
        self.screenerEntryExample = "Example: https://finance.yahoo.com/etfs (or C:\Documents\Investing\Input\S&P500_Input.xlsx)"
        screenerEntry = Entry(self, textvariable=self.screenerEntry, width=100, fg=entryTextColour)
        screenerEntry.grid(row=3, column=2, sticky=W, pady=10, padx=10)
        screenerEntry.insert(0, self.screenerEntryExample)
        screenerEntry.bind('<FocusIn>', onClick)

        excelReportButton = Button(self, text="Create Report", command=self.runProgram,bg=buttonColor,fg=buttonTextColour)
        excelReportButton.grid(row=4,column=1, columnspan=2, sticky=W+E+N+S,padx=10, pady=10)

    def generateReport(self):
        try:
            screenerURL = self.screenerEntry.get()

            if self.filenameEntry.get()[-5:] == '.xlsx':
                filename = self.filenameEntry.get()
            else:
                filename = self.filenameEntry.get() + '.xlsx'

            progress = Label(self, text="Collecting tickers..",bg=buttonColor,fg=buttonTextColour)
            progress.grid(row=4,column=1, columnspan=2, sticky=W+E+N+S,padx=10, pady=10)
            tickers = symbolCollector(screenerURL)

            excelReport.excelWriter(self, tickers, filename)

        except Exception as error:
            messagebox.showerror('Error', "The program has crashed with the following error: \n\n"
                                 + str(error) + "\n\nIf the problem persists, please create an Issue with the error "
                                 + "message on the project's GitHub page:"
                                 + "https://github.com/JerBouma/ThePassiveInvestor/issues. \n\n"
                                 + "You can copy this entire message with CTRL + C.")
        
        excelReportButton = Button(self, text="Create Report", command=self.runProgram,bg=buttonColor,fg=buttonTextColour)
        excelReportButton.grid(row=4,column=1, columnspan=2, sticky=W+E+N+S,padx=10, pady=10)

    def runProgram(self):
        threading.Thread(target=self.generateReport).start()


root = Tk()
app = Window(root)
app.configure(background=background)
root.geometry('725x200')
root.iconbitmap("images/iconICO.ico")
root.resizable(False, False)
root.mainloop() 