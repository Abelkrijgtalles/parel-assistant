from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import messagebox, simpledialog, Tk
from random import choice


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg = decoderen(msg)
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    if msg =="{quit}":
        client_socket.close()
        top.quit()
    msg = coderen(msg)
    client_socket.send(bytes(msg, "utf8"))


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set(coderen("{quit}"))
    send()

def is_even(getal):
    return getal % 2 == 0

def ontvang_even_letters(bericht):
    even_letters = []
    for teller in range(0, len(bericht)):
        if is_even(teller):
            even_letters.append(bericht[teller])
    return even_letters

def ontvang_oneven_letters(bericht):
    oneven_letters = []
    for teller in range(0, len(bericht)):
        if not is_even(teller):
            oneven_letters.append(bericht[teller])
    return oneven_letters

def wissel_letters(bericht):
    letter_lijst = []
    if not is_even(len(bericht)):
        bericht = bericht + "x"
    even_letters = ontvang_even_letters(bericht)
    oneven_letters = ontvang_oneven_letters(bericht)
    for teller in range(0, int(len(bericht) /2)):
        letter_lijst.append(oneven_letters[teller])
        letter_lijst.append(even_letters[teller])
    nieuw_bericht = "".join(letter_lijst)
    return nieuw_bericht

def coderen(bericht):
    gecodeerde_lijst = []
    valse_letters = ["a", "b", "c", "d", "e", "f", "g", "i", "r", "s", "t", "u", "v"]
    for teller in range(0, len(bericht)):
        gecodeerde_lijst.append(bericht[teller])
        gecodeerde_lijst.append(choice(valse_letters))
    nieuw_bericht = "".join(gecodeerde_lijst)
    gecodeerd_bericht = "".join(reversed(nieuw_bericht))
    gecodeerd_bericht = wissel_letters(gecodeerd_bericht)
    return gecodeerd_bericht

def decoderen(bericht):
    gedecodeerd_bericht = wissel_letters(bericht)
    niet_omgedraaid_bericht = "".join(reversed(gedecodeerd_bericht))
    even_letters = ontvang_even_letters(niet_omgedraaid_bericht)
    nieuw_bericht = "".join(even_letters)
    return nieuw_bericht

def ontvang_taak():
    taak = simpledialog.askstring("Taak", "Wil je coderen of decoderen")
    return taak

def ontvang_bericht():
    bericht = simpledialog.askstring("Bericht", "Voer het geheime bericht in :")
    return bericht


top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = '192.168.1.28'
PORT = 64641
if not PORT:
    PORT = 64641
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.