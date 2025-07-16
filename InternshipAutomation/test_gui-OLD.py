try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    import tkinter.messagebox

def doNothing():
	print("Nothing")

def setChrome():
    selectedBrowser.set('Chrome')
    app.update_idletasks()
    statusUpdate.set('Chrome Selected')

def setFirefox():
    selectedBrowser.set('Firefox')
    app.update_idletasks()
    statusUpdate.set('Firefox Selected')

def setIntexp():
    selectedBrowser.set('Internet Explorer')
    app.update_idletasks()
    statusUpdate.set('Internet Explorer Selected')

def setSafari():
    selectedBrowser.set('Safari')
    app.update_idletasks()
    statusUpdate.set('Safari Selected')

def resetBrowser():
    selectedBrowser.set('Select Browser')
    app.update_idletasks()
    statusUpdate.set('Browser Selector Reset')

def setFirstServer():
    selectedServer.set('1')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 1 Selected')

def setSecondServer():
    selectedServer.set('2')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 2 Selected')

def setThirdServer():
    selectedServer.set('3')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 3 Selected')

def setFourthServer():
    selectedServer.set('4')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 4 Selected')

def setFifthServer():
    selectedServer.set('5')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 5 Selected')

def setSixthServer():
    selectedServer.set('6')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 6 Selected')

def setSeventhServer():
    selectedServer.set('7')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 7 Selected')

def resetServer():
    selectedServer.set('Select Server')
    batchSelect.configure(state='active')
    app.update_idletasks()
    statusUpdate.set('Server Selector Reset')

def setFirstBatch():
    selectedBatch.set('1-3')
    serverSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('1-3 Selected')

def setSecondBatch():
    selectedBatch.set('4-7')
    serverSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('4-7 Selected')

def setAllBatch():
    selectedBatch.set('All')
    serverSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('All Selected')

def resetBatch():
    selectedBatch.set('Select Batch')
    serverSelect.configure(state='active')
    app.update_idletasks()
    statusUpdate.set('Server Batch Reset')

app = Tk()
app.title("Automation GUI")
app.geometry('750x500')

#main menu

menu = Menu(app)
app.config(menu=menu)

fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Test", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=app.quit)

helpMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Selenium Setup", command=doNothing)
helpMenu.add_command(label="Tutorials", command=doNothing)

#toolbar

toolbar = Frame(app)

selectedBrowser = StringVar()
selectedBrowser.set('Select Browser')
selectedServer = StringVar()
selectedServer.set('Select Server')
selectedBatch = StringVar()
selectedBatch.set('Select Batch')

browserSelect = Menubutton(toolbar, textvariable=selectedBrowser, relief=RAISED, width = 25)
browserSelect.menu = Menu(browserSelect, tearoff=0)
browserSelect["menu"] = browserSelect.menu
browserSelect.menu.add_command(label="Select Browser", command=resetBrowser)
browserSelect.menu.add_command(label="Chrome", command=setChrome)
browserSelect.menu.add_command(label="Firefox", command=setFirefox)
browserSelect.menu.add_command(label="Internet Explorer", command=setIntexp)
browserSelect.menu.add_command(label="Safari", command=setSafari)

serverSelect = Menubutton(toolbar, textvariable=selectedServer, relief=RAISED, width = 25)
serverSelect.menu = Menu(serverSelect, tearoff=0)
serverSelect["menu"] = serverSelect.menu
serverSelect.menu.add_command(label="Select Server", command=resetServer)
serverSelect.menu.add_command(label="1", command=setFirstServer)
serverSelect.menu.add_command(label="2", command=setSecondServer)
serverSelect.menu.add_command(label="3", command=setThirdServer)
serverSelect.menu.add_command(label="4", command=setFourthServer)
serverSelect.menu.add_command(label="5", command=setFifthServer)
serverSelect.menu.add_command(label="6", command=setSixthServer)
serverSelect.menu.add_command(label="7", command=setSeventhServer)

batchSelect = Menubutton(toolbar, textvariable=selectedBatch, relief=RAISED, width = 25)
batchSelect.menu = Menu(batchSelect, tearoff=0)
batchSelect["menu"] = batchSelect.menu
batchSelect.menu.add_command(label="Select Batch", command=resetBatch)
batchSelect.menu.add_command(label="1-3", command=setFirstBatch)
batchSelect.menu.add_command(label="4-7", command=setSecondBatch)
batchSelect.menu.add_command(label="All", command=setAllBatch)

runTestButton = Button(toolbar, text="Run Test", command=doNothing)

browserSelect.pack(side=LEFT, padx=2, pady=2)
serverSelect.pack(side=LEFT, padx=2, pady=2)
batchSelect.pack(side=LEFT, padx=2, pady=2)
runTestButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

#status bar
statusUpdate = StringVar()
statusUpdate.set('')

status = Label(app, textvariable=statusUpdate, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

#messagebox

#tkinter.messagebox.showinfo('Title', 'This is a test')
#answer = tkinter.messagebox.askquestion('Title', 'Do you wish to exit?')

#if answer == 'yes':
#    print('yes')

app.mainloop()