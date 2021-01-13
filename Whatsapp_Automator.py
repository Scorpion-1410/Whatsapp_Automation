from tkinter import *
from tkinter.ttk import *
import pywhatkit


root = Tk() 
countrycode = StringVar()
phno = StringVar()
hours = IntVar()
minutes = IntVar()
text = StringVar()

def send():
    ph = phno.get()
    cc1 = countrycode.get()
    cc = cc1.split('-')
    ph = cc[0] + ph
    pywhatkit.sendwhatmsg(ph,text.get(),hours.get(),minutes.get())

root.title("Whatsapp Automator")

c_label = Label(root, text="Country")
c_label.grid(row=0, column=0) 

combo = Combobox(root,textvariable = countrycode)
combo['values'] = ("+91-India", "+92-Pakistan", "+33-France", "+90-Trukey", "+52-Mexico", "+966-Saudi Arabia", "+1-US", "+61-Australia", "+30-Greece", 
                   '+86-China', '+49-Germany', '+852-Honk Kong', '+55-Canada', '+34-Spain', '+7-Russia', '+380-Ukrain', '+48-Poland', '+39-Italy', 
                   '+60-Malaysia', '+66-Thailand', '+81-Japan', '+44-UK', '+977-Nepal', '+94-Sri Lanka', '+32-Belgium', '+880-Bangladesh') 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(row=0, column = 1)

phno_label = Label(root, text="Phone Number") 
phno_label.grid(row = 3, column = 0)

phno_entry = Entry(root,textvariable = phno)
phno_entry.grid(row= 3, column = 1)

text_label = Label(root,text="Message")
text_label.grid(row = 3, column = 2)

text_entry = Entry(root,textvariable = text)
text_entry.grid(row=3,column = 3)

hours_label = Label(root, text="Hours") 
hours_label.grid(row = 4, column = 0)

hours_entry = Entry(root,textvariable = hours)
hours_entry.grid(row=4,column=1)

minutes_label = Label(root, text="Minutes") 
minutes_label.grid(row = 4, column = 2)

minutes_entry = Entry(root,textvariable = minutes)
minutes_entry.grid(row=4,column=3)

generate_button = Button(root, text="Send", command=send) 
generate_button.grid(row=0, column=3) 

root.mainloop() 
