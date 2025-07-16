try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    from tkinter import ttk
    import tkinter.messagebox
import os

def doNothing():
    print("Nothing")

def setMember():
    selectedSite.set("Member Demo")
    app.update_idletasks()
    statusUpdate.set('Member Demo Selected')
    site.set('1')

def setProvider():
    selectedSite.set("Provider Demo")
    app.update_idletasks()
    statusUpdate.set('Provider Demo Selected')
    site.set('2')

def setApi():
    selectedSite.set("API Check")
    app.update_idletasks()
    statusUpdate.set('API Check Selected')
    site.set('3')

def setV2():
    selectedSite.set("V2 Check")
    app.update_idletasks()
    statusUpdate.set('V2 Check Selected')
    site.set('4')

def resetSite():
    selectedSite.set("Select Site")
    app.update_idletasks()
    statusUpdate.set('Site Select Reset')
    site.set('0')

def setChrome():
    selectedBrowser.set('Chrome')
    app.update_idletasks()
    statusUpdate.set('Chrome Selected')
    browser.set('1')

def setFirefox():
    selectedBrowser.set('Firefox')
    app.update_idletasks()
    statusUpdate.set('Firefox Selected')
    browser.set('2')

def setIntexp():
    selectedBrowser.set('Internet Explorer')
    app.update_idletasks()
    statusUpdate.set('Internet Explorer Selected')
    browser.set('3')

def setSafari():
    selectedBrowser.set('Safari')
    app.update_idletasks()
    statusUpdate.set('Safari Selected')
    browser.set('4')

def resetBrowser():
    selectedBrowser.set('Select Browser')
    app.update_idletasks()
    statusUpdate.set('Browser Selector Reset')
    browser.set('0')

def setFirstServer():
    selectedServer.set('1')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 1 Selected')
    server.set('1')

def setSecondServer():
    selectedServer.set('2')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 2 Selected')
    server.set('2')

def setThirdServer():
    selectedServer.set('3')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 3 Selected')
    server.set('3')

def setFourthServer():
    selectedServer.set('4')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 4 Selected')
    server.set('4')

def setFifthServer():
    selectedServer.set('5')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 5 Selected')
    server.set('5')

def setSixthServer():
    selectedServer.set('6')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 6 Selected')
    server.set('6')

def setSeventhServer():
    selectedServer.set('7')
    batchSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('Server 7 Selected')
    server.set('7')

def resetServer():
    selectedServer.set('Select Server')
    batchSelect.configure(state='active')
    app.update_idletasks()
    statusUpdate.set('Server Selector Reset')
    server.set('0')

def setFirstBatch():
    selectedBatch.set('1-3')
    serverSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('1-3 Selected')
    batch.set('1')

def setSecondBatch():
    selectedBatch.set('4-7')
    serverSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('4-7 Selected')
    batch.set('2')

def setAllBatch():
    selectedBatch.set('All')
    serverSelect.configure(state='disabled')
    app.update_idletasks()
    statusUpdate.set('All Selected')
    batch.set('3')

def resetBatch():
    selectedBatch.set('Select Batch')
    serverSelect.configure(state='active')
    app.update_idletasks()
    statusUpdate.set('Server Batch Reset')
    batch.set('0')

def runScripts():
    siteChoice = site.get()
    browserChoice = browser.get()
    serverChoice = server.get()
    batchChoice = batch.get()
    if siteChoice == 1:
        if browserChoice == 1:
            if serverChoice == 1:
                statusUpdate.set("Running Automated Member Demo Test on Server 1 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_v5-1.py')
                pbar.start(130)
            elif serverChoice == 2:
                statusUpdate.set("Running Automated Member Demo Test on Server 2 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_v5-2.py')
            elif serverChoice == 3:
                statusUpdate.set("Running Automated Member Demo Test on Server 3 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_v5-3.py')
            elif serverChoice == 4:
                statusUpdate.set("Running Automated Member Demo Test on Server 4 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_v5-4.py')
            elif serverChoice == 5:
                statusUpdate.set("Running Automated Member Demo Test on Server 5 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_v5-5.py')
            elif serverChoice == 6:
                statusUpdate.set("Running Automated Member Demo Test on Server 6 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_v5-6.py')
            elif serverChoice == 7:
                statusUpdate.set("Running Automated Member Demo Test on Server 7 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_v5-7.py')
            elif batchChoice == 1:
                statusUpdate.set("Running Automated Member Demo Test Batch for Servers 1-3 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_run_1-3.bat')
            elif batchChoice == 2:
                statusUpdate.set("Running Automated Member Demo Test Batch for Servers 4-7 for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_run_4-7.bat')
            elif batchChoice == 3:
                statusUpdate.set("Running Automated Member Demo Test Batch for All Servers for Chrome")
                os.system('MemberDemo\\member_demosite_automation_chrome_run_all.bat')
            else:
                statusUpdate.set("No Server/Batch Selected")
        elif browser == 2:
            if serverChoice == 1:
                statusUpdate.set("Running Automated Member Demo Test on Server 1 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_v5-1.py')
            elif serverChoice == 2:
                statusUpdate.set("Running Automated Member Demo Test on Server 2 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_v5-2.py')
            elif serverChoice == 3:
                statusUpdate.set("Running Automated Member Demo Test on Server 3 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_v5-3.py')
            elif serverChoice == 4:
                statusUpdate.set("Running Automated Member Demo Test on Server 4 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_v5-4.py')
            elif serverChoice == 5:
                statusUpdate.set("Running Automated Member Demo Test on Server 5 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_v5-5.py')
            elif serverChoice == 6:
                statusUpdate.set("Running Automated Member Demo Test on Server 6 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_v5-6.py')
            elif serverChoice == 7:
                statusUpdate.set("Running Automated Member Demo Test on Server 7 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_v5-7.py')
            elif batchChoice == 1:
                statusUpdate.set("Running Automated Member Demo Test Batch for Servers 1-3 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_run_1-3.bat')
            elif batchChoice == 2:
                statusUpdate.set("Running Automated Member Demo Test Batch for Servers 4-7 for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_run_4-7.bat')
            elif batchChoice == 3:
                statusUpdate.set("Running Automated Member Demo Test Batch for All Servers for Firefox")
                os.system('MemberDemo\\member_demosite_automation_firefox_run_all.bat')
            else:
                statusUpdate.set("No Server/Batch Selected")
        elif browser == 3:
            if serverChoice == 1:
                statusUpdate.set("Running Automated Member Demo Test on Server 1 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_v5-1.py')
            elif serverChoice == 2:
                statusUpdate.set("Running Automated Member Demo Test on Server 2 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_v5-2.py')
            elif serverChoice == 3:
                statusUpdate.set("Running Automated Member Demo Test on Server 3 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_v5-3.py')
            elif serverChoice == 4:
                statusUpdate.set("Running Automated Member Demo Test on Server 4 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_v5-4.py')
            elif serverChoice == 5:
                statusUpdate.set("Running Automated Member Demo Test on Server 5 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_v5-5.py')
            elif serverChoice == 6:
                statusUpdate.set("Running Automated Member Demo Test on Server 6 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_v5-6.py')
            elif serverChoice == 7:
                statusUpdate.set("Running Automated Member Demo Test on Server 7 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_v5-7.py')
            elif batchChoice == 1:
                statusUpdate.set("Running Automated Member Demo Test Batch for Servers 1-3 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_run_1-3.bat')
            elif batchChoice == 2:
                statusUpdate.set("Running Automated Member Demo Test Batch for Servers 4-7 for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_run_4-7.bat')
            elif batchChoice == 3:
                statusUpdate.set("Running Automated Member Demo Test Batch for All Servers for Internet Explorer")
                os.system('MemberDemo\\member_demosite_automation_intexplorer_run_all.bat')
            else:
                statusUpdate.set("No Server/Batch Selected")
        elif browser == 4:
            statusUpdate.set("Running Automated Member Demo Test for Safari")
            os.system('MemberDemo\\member_demosite_automation_safari_run.bat')
        else:
            statusUpdate.set("No Browser Selected")

    if siteChoice == 2:
        if browserChoice == 1:
            if serverChoice == 1:
                statusUpdate.set("Running Automated Provider Demo Test on Server 1 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_v2-1.py')
            elif serverChoice == 2:
                statusUpdate.set("Running Automated Provider Demo Test on Server 2 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_v2-2.py')
            elif serverChoice == 3:
                statusUpdate.set("Running Automated Provider Demo Test on Server 3 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_v2-3.py')
            elif serverChoice == 4:
                statusUpdate.set("Running Automated Provider Demo Test on Server 4 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_v2-4.py')
            elif serverChoice == 5:
                statusUpdate.set("Running Automated Provider Demo Test on Server 5 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_v2-5.py')
            elif serverChoice == 6:
                statusUpdate.set("Running Automated Provider Demo Test on Server 6 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_v2-6.py')
            elif serverChoice == 7:
                statusUpdate.set("Running Automated Provider Demo Test on Server 7 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_v2-7.py')
            elif batchChoice == 1:
                statusUpdate.set("Running Automated Provider Demo Test Batch for Servers 1-3 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_run_1-3.bat')
            elif batchChoice == 2:
                statusUpdate.set("Running Automated Provider Demo Test Batch for Servers 4-7 for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_run_4-7.bat')
            elif batchChoice == 3:
                statusUpdate.set("Running Automated Provider Demo Test Batch for All Servers for Chrome")
                os.system('ProviderDemo\\provider_demosite_automation_chrome_run_all.bat')
            else:
                statusUpdate.set("No Server/Batch Selected")
        elif browser == 2:
            if serverChoice == 1:
                statusUpdate.set("Running Automated Provider Demo Test on Server 1 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_v2-1.py')
            elif serverChoice == 2:
                statusUpdate.set("Running Automated Provider Demo Test on Server 2 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_v2-2.py')
            elif serverChoice == 3:
                statusUpdate.set("Running Automated Provider Demo Test on Server 3 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_v2-3.py')
            elif serverChoice == 4:
                statusUpdate.set("Running Automated Provider Demo Test on Server 4 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_v2-4.py')
            elif serverChoice == 5:
                statusUpdate.set("Running Automated Provider Demo Test on Server 5 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_v2-5.py')
            elif serverChoice == 6:
                statusUpdate.set("Running Automated Provider Demo Test on Server 6 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_v2-6.py')
            elif serverChoice == 7:
                statusUpdate.set("Running Automated Provider Demo Test on Server 7 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_v2-7.py')
            elif batchChoice == 1:
                statusUpdate.set("Running Automated Provider Demo Test Batch for Servers 1-3 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_run_1-3.bat')
            elif batchChoice == 2:
                statusUpdate.set("Running Automated Provider Demo Test Batch for Servers 4-7 for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_run_4-7.bat')
            elif batchChoice == 3:
                statusUpdate.set("Running Automated Provider Demo Test Batch for All Servers for Firefox")
                os.system('ProviderDemo\\provider_demosite_automation_firefox_run_all.bat')
            else:
                statusUpdate.set("No Server/Batch Selected")
        elif browser == 3:
            if serverChoice == 1:
                statusUpdate.set("Running Automated Provider Demo Test on Server 1 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_v2-1.py')
            elif serverChoice == 2:
                statusUpdate.set("Running Automated Provider Demo Test on Server 2 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_v2-2.py')
            elif serverChoice == 3:
                statusUpdate.set("Running Automated Provider Demo Test on Server 3 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_v2-3.py')
            elif serverChoice == 4:
                statusUpdate.set("Running Automated Provider Demo Test on Server 4 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_v2-4.py')
            elif serverChoice == 5:
                statusUpdate.set("Running Automated Provider Demo Test on Server 5 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_v2-5.py')
            elif serverChoice == 6:
                statusUpdate.set("Running Automated Provider Demo Test on Server 6 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_v2-6.py')
            elif serverChoice == 7:
                statusUpdate.set("Running Automated Provider Demo Test on Server 7 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_v2-7.py')
            elif batchChoice == 1:
                statusUpdate.set("Running Automated Provider Demo Test Batch for Servers 1-3 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_run_1-3.bat')
            elif batchChoice == 2:
                statusUpdate.set("Running Automated Provider Demo Test Batch for Servers 4-7 for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_run_4-7.bat')
            elif batchChoice == 3:
                statusUpdate.set("Running Automated Provider Demo Test Batch for All Servers for Internet Explorer")
                os.system('ProviderDemo\\provider_demosite_automation_intexplorer_run_all.bat')
            else:
                statusUpdate.set("No Server/Batch Selected")
        else:
            statusUpdate.set("No Browser Selected")

    if siteChoice == 3:
        if serverChoice == 1:
            statusUpdate.set("Running API Check Test on Server 1 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_v1-1.py')
        elif serverChoice == 2:
            statusUpdate.set("Running API Check Test on Server 2 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_v1-2.py')
        elif serverChoice == 3:
            statusUpdate.set("Running API Check Test on Server 3 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_v1-3.py')
        elif serverChoice == 4:
            statusUpdate.set("Running API Check Test on Server 4 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_v1-4.py')
        elif serverChoice == 5:
            statusUpdate.set("Running API Check Test on Server 5 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_v1-5.py')
        elif serverChoice == 6:
            statusUpdate.set("Running API Check Test on Server 6 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_v1-6.py')
        elif serverChoice == 7:
            statusUpdate.set("Running API Check Test on Server 7 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_v1-7.py')
        elif batchChoice == 1:
            statusUpdate.set("Running API Check Test Batch for Servers 1-3 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_run_1-3.bat')
        elif batchChoice == 2:
            statusUpdate.set("Running API Check Test Batch for Servers 4-7 for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_run_4-7.bat')
        elif batchChoice == 3:
            statusUpdate.set("Running API Check Test Batch for All Servers for Chrome")
            os.system('APICheck\\apicheck_automation_chrome_run_all.bat')
        else:
            statusUpdate.set("No Server/Batch Selected")

def endScripts():
    print("Nothing")


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

selectedSite = StringVar()
selectedSite.set('Select Site')
selectedBrowser = StringVar()
selectedBrowser.set('Select Browser')
selectedServer = StringVar()
selectedServer.set('Select Server')
selectedBatch = StringVar()
selectedBatch.set('Select Batch')
site = IntVar()
site.set('0')
browser = IntVar()
browser.set('0')
server = IntVar()
server.set('0')
batch = IntVar()
batch.set('0')

siteSelect = Menubutton(toolbar, textvariable=selectedSite, relief=RAISED, width=25)
siteSelect.menu = Menu(siteSelect, tearoff=0)
siteSelect["menu"] = siteSelect.menu
siteSelect.menu.add_command(label="Select Site", command=resetSite)
siteSelect.menu.add_command(label="Member Demo", command=setMember)
siteSelect.menu.add_command(label="Provider Demo", command=setProvider)
siteSelect.menu.add_command(label="API Check", command=setApi)
siteSelect.menu.add_command(label="V2 Check", command=setV2)

browserSelect = Menubutton(toolbar, textvariable=selectedBrowser, relief=RAISED, width=25)
browserSelect.menu = Menu(browserSelect, tearoff=0)
browserSelect["menu"] = browserSelect.menu
browserSelect.menu.add_command(label="Select Browser", command=resetBrowser)
browserSelect.menu.add_command(label="Chrome", command=setChrome)
browserSelect.menu.add_command(label="Firefox", command=setFirefox)
browserSelect.menu.add_command(label="Internet Explorer", command=setIntexp)
browserSelect.menu.add_command(label="Safari", command=setSafari)

serverSelect = Menubutton(toolbar, textvariable=selectedServer, relief=RAISED, width=25)
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

batchSelect = Menubutton(toolbar, textvariable=selectedBatch, relief=RAISED, width=25)
batchSelect.menu = Menu(batchSelect, tearoff=0)
batchSelect["menu"] = batchSelect.menu
batchSelect.menu.add_command(label="Select Batch", command=resetBatch)
batchSelect.menu.add_command(label="1-3", command=setFirstBatch)
batchSelect.menu.add_command(label="4-7", command=setSecondBatch)
batchSelect.menu.add_command(label="All", command=setAllBatch)

siteSelect.pack(side=LEFT, padx=2, pady=2)
browserSelect.pack(side=LEFT, padx=2, pady=2)
serverSelect.pack(side=LEFT, padx=2, pady=2)
batchSelect.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

toolbar2 = Frame(app)
runTestButton = Button(toolbar2, text="Run Test", command=runScripts)
cancelTestButton = Button(toolbar2, text="Cancel", command=endScripts)
runTestButton.pack(side=LEFT, padx=2, pady=2)
cancelTestButton.pack(side=LEFT, padx=2, pady=2)
toolbar2.pack(side=TOP, pady=10)

toolbar3 = Frame(app)
pbar = ttk.Progressbar(toolbar3, orient=HORIZONTAL, length=500, mode='determinate', maximum=1000)
pbar.pack(padx=5, pady=5)
toolbar3.pack(side=TOP, fill=X, pady=10)

#status bar
statusUpdate = StringVar()
statusUpdate.set('')

status = Label(app, textvariable=statusUpdate, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

#if answer == 'yes':
#    print('yes')

app.mainloop()