import ast
import urllib.request
from datetime import date
from tkinter import *

import bs4

z = []
x = str(date.today())

print(x)

win = Tk()
win.title(f'Zls {x}')
win.resizable(0, 0)
win.geometry('298x435')
win['bg'] = '#2F5A78'

data = ''
inputVal = StringVar()
day = data
url = urllib.request.urlopen('http://api.nbp.pl/api/exchangerates/rates/a/CZK/'+data)
soup = bs4.BeautifulSoup(url, 'html.parser')
CZKkurs = ast.literal_eval(str(soup))['rates'][0]['mid']

print(CZKkurs)

def clickListener(butVal):
    global data
    data = data + str(butVal)
    inputVal.set(data)

def equal():
    global data
    try:
        if data == '':
            inputVal.set('')
            data = ''
        else:
            solution = eval(data)
            inputVal.set(solution)
            data = str(solution)
    except:
        inputVal.set('')
        data = ''

def deleteDigit():
    global data
    try:
        solution = list(data)
        solution.pop()
        data = ''.join(solution)
        inputVal.set(data)
    except:
        inputVal.set('')
        data = ''

def clearAll():
    global data
    data = ''
    inputVal.set('')

def Na_Korony():
    global data
    try:

        solution = float(data) / CZKkurs
        inputVal.set('%0.2f' %solution + " KC")
        data = str('%0.2f' %solution + " KC")
    except:
        inputVal.set('')
        data = ''
def Na_PLN():
    global data
    try:
        solution = float(data) * CZKkurs
        inputVal.set('%0.2f' %solution + " PLN")
        data = str('%0.2f' %solution + " PLN")
    except:
        inputVal.set('')
        data = ''


def handle_key(event):
    key = event.keysym
    key_mappings = {
        'Return': 'equal',

    }
    if key.isdigit():
        clickListener(int(key))
    elif key in key_mappings:
        if key == 'Return':
            equal()
        else:
            clickListener(key_mappings[key])

for digit in '0123456789':
    win.bind(digit, handle_key)
win.bind('<Return>', handle_key)
win.bind('+', handle_key)
win.bind('-', handle_key)
win.bind('*', handle_key)
win.bind('/', handle_key)

frame = Frame(win, width=298, height=20, bd=2)
frame.pack(side=TOP, pady=5)
inputField = Entry(frame, width=20, font=('Arial bold', 20), textvariable=inputVal, bg='white', fg='blue',
                   justify=RIGHT)

inputField.pack()

bton_frame = Frame(win, width=250, height=300, bg='black')
bton_frame.pack(side=BOTTOM, pady=0)
nine = Button(bton_frame, text='9', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
              command=lambda: clickListener(9)).grid(row=0, column=2)
eight = Button(bton_frame, text='8', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clickListener(8)).grid(row=0, column=1)
seven = Button(bton_frame, text='7', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clickListener(7)).grid(row=0, column=0)
clear = Button(bton_frame, text='C', bg='grey', fg='yellow', font=('Arial bold', 10), width=8, height=4,
               command=lambda: deleteDigit()).grid(row=0, column=3)
six = Button(bton_frame, text='6', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
             command=lambda: clickListener(6)).grid(row=1, column=2)
five = Button(bton_frame, text='5', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
              command=lambda: clickListener(5)).grid(row=1, column=1)
four = Button(bton_frame, text='4', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
              command=lambda: clickListener(4)).grid(row=1, column=0)
three = Button(bton_frame, text='1', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clickListener(1)).grid(row=2, column=0)
two = Button(bton_frame, text='2', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
             command=lambda: clickListener(2)).grid(row=2, column=1)
one = Button(bton_frame, text='3', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
             command=lambda: clickListener(3)).grid(row=2, column=2)
equals = Button(bton_frame, text='=', bg='green', fg='white', font=('Arial bold', 10), width=8, height=4,
                   command=lambda: equal()).grid(row=2, column=3)
zero = Button(bton_frame, text='0', bg='light blue', fg='blue', font=('Arial bold', 10), width=8, height=4,
              command=lambda: clickListener(0)).grid(row=3, column=0)
equals = Button(bton_frame, text='=', bg='grey', fg='white', font=('Arial bold', 10), width=8, height=4,
                   command=lambda: equal()).grid(row=1, column=3)
point = Button(bton_frame, text='.', bg='grey', fg='white', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clickListener('.')).grid(row=2, column=3)
win.bind('<Return>', lambda event: equal())
clear = Button(bton_frame, text='Clear', bg='teal', fg='yellow', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clearAll()).grid(row=3, column=2)
kantor = Button(bton_frame, text=f'PLN/CZK\n\nKč={CZKkurs}', bg='teal', fg='white', font=('Arial bold', 10), width=8, height=4,
              command=lambda: Na_Korony()).grid(row=3, column=3)
kantor = Button(bton_frame, text=f' CZK/PLN', bg='teal', fg='white', font=('Arial bold', 10), width=8, height=4,
              command=lambda: Na_PLN()).grid(row=3, column=1)

times = Button(bton_frame, text='*', bg='teal', fg='white', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clickListener('*')).grid(row=4, column=0)
times = Button(bton_frame, text='/', bg='teal', fg='white', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clickListener('/')).grid(row=4, column=1)
times = Button(bton_frame, text='+', bg='teal', fg='white', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clickListener('+')).grid(row=4, column=2)
times = Button(bton_frame, text='-', bg='teal', fg='white', font=('Arial bold', 10), width=8, height=4,
               command=lambda: clickListener('-')).grid(row=4, column=3)



win.mainloop()



