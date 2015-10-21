import Tkinter
import tkMessageBox

#Create the starting window
startWindow = Tkinter.Tk()
startWindow.title("Welcome to Steganography")
startWindow.geometry("300x300")
startWindow.configure(background="#a1dbcd")

def displayMessage():
    displayMsg=Tkinter.Tk()
    displayMsg.title('Message')
    displayMsg.geometry("300x300")
    displayMsg.configure(background="#a1dbcd")
    messageSLabel = Tkinter.Label(displayMsg, text=messageLabel.get(), bg="#a1dbcd")
    messageSLabel.pack()

def passwordCheck():
    if(password1Entry.get()==password2Entry.get()):
        window3()

def authDecode():
    decodeWindw=Tkinter.Tk()
    decodeWindow.title("Welcome to Steganography")
    decodeWindow.geometry("300x300")
    decodeWindow.configure(background="#a1dbcd")
    passwordLabel = Tkinter.Label(decodeWindow, text="Enter password", bg="#a1dbcd")
    global ent3
    password2Entry = Tkinter.Entry(decodeWindw)
    passwordLabel.pack()
    password2Entry.pack()
    decodeBtn = Tkinter.Button(decodeWindw, text="Authorize", fg="#a1dbcd", bg="#383a39", command=passwordCheck)
    decodeBtn.pack()

#Setting inputs for starting window
#Password
passwordLabel = Tkinter.Label(startWindow, text="Set password", bg="#a1dbcd")
password1Entry = Tkinter.Entry(startWindow)
passwordLabel.pack()
password1Entry.pack()

#Message
messageLabel = Tkinter.Label(startWindow, text="Set message", bg="#a1dbcd")
messageEntry = Tkinter.Entry(startWindow)
messageLabel.pack()
messageEntry.pack()

#Encode
encodeBtn=Tkinter.Button(startWindow, text="Encode", fg="#a1dbcd", bg="#383a39", command=authDecode)
encodeBtn.pack()

startWindow.mainloop()