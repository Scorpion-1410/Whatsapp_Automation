from tkinter import *
from tkinter.ttk import *
import pywhatkit
from pytube import YouTube
import pywhatkit.mainfunctions
from PIL import Image, ImageTk
import os

# Creating the GUI Window
root = Tk() 
root.geometry('640x300')
root.resizable(0,0)
root.configure(background="black")

# Title of GUI Window
root.title("Whatsapp Automator")

# Tkinter variable used for hour, minute, message
hours = IntVar()
minutes = IntVar()
text = StringVar()

# Tkinter variable used for CountryCode and phone number
countrycode = StringVar()
phno = StringVar()

# Tkinter variable used for GroupID
grp_id=StringVar()

# Tkinter variable used for WikiSearch Query
wiki_search = StringVar()

# Tkinter variable used for YouTubeSearch Query
yt_search = StringVar()

# Tkinter variable used for GoogleSearch Query
google_search = StringVar()

# Tkinter variable used for SndrMail, SndrPass, RcvrMail and Content
sndr_mail = StringVar()
sndr_pass = StringVar()
rcvr_mail = StringVar()
cntnt = StringVar()

# Tkinter variable used for Link
link = StringVar()

# function to send Whatsapp msg to personal
def send_to_personal():
    ph = phno.get()
    cc1 = countrycode.get()
    cc = cc1.split('-')
    ph = cc[0] + ph
    root.configure(background="green")
    pywhatkit.sendwhatmsg(ph,text.get(),hours.get(),minutes.get(),wait_time=10)
    
# function to send Mail
def mail():
    print(sndr_mail.get())
    print(sndr_pass.get())
    pywhatkit.mainfunctions.sendMail(sndr_mail.get(),sndr_pass.get(),rcvr_mail.get(),cntnt.get())
    root.configure(background="orange")

# function to send Whatsapp msg to group
def send_to_group():
    pywhatkit.sendwhatmsg_to_group(grp_id.get(),text.get(),hours.get(),minutes.get(),wait_time=10)
    root.configure(background="green")

# function to Wiki/Terminal Search
def wikiSearch():
    pywhatkit.info(wiki_search.get())
    root.configure(background="white")

# function to play first video on Youtube
def play_on_youtube():
    pywhatkit.playonyt(yt_search.get())
    root.configure(background="red")

# function to Google search
def googleSearch():
    pywhatkit.search(google_search.get())
    root.configure(background="blue")
    
# function to Youtube Downloader
def downloader():     
    url =YouTube(str(link.get()))
    filters = url.streams.filter(progressive=True, file_extension='mp4')
    filters.get_highest_resolution().download(output_path="path for downloaded file")

    label = Label(root, text = 'Downloaded', width=10)
    label.grid(row=10,column=2)     

# Label for the country_code Combo Box
c_label = Label(root, text="Country", width = 10)
c_label.grid(row=0, column=0) 
c_label.configure(background="black",foreground="white")

# Combo box for Country codes
combo = Combobox(root,textvariable = countrycode, width= 18)
combo['values'] = ("+91-India", "+92-Pakistan", "+33-France", "+90-Trukey", "+52-Mexico",
                   '+966-Saudi Arabia', "+1-US", "+61-Australia", "+30-Greece", 
                   '+86-China', '+49-Germany', '+852-Honk Kong', '+55-Canada', '+34-Spain', 
                   '+7-Russia', '+380-Ukrain', '+48-Poland', '+39-Italy', 
                   '+60-Malaysia', '+66-Thailand', '+81-Japan', '+44-UK', '+977-Nepal', 
                   '+94-Sri Lanka', '+32-Belgium', '+880-Bangladesh') 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(row=0, column = 1)

# Label for Phone Number
phno_label = Label(root, text="Ph Number", width = 10) 
phno_label.grid(row = 1 , column = 0)
phno_label.configure(background="black",foreground="white")

# Entry box for Phone Number
phno_entry = Entry(root,textvariable = phno)
phno_entry.grid(row= 1, column = 1)
phno_entry.configure(background="black")

# Label for Message
text_label = Label(root,text="Message", width = 10)
text_label.grid(row = 2, column = 0)
text_label.configure(background="black",foreground="white")

# Entry box for Message
text_entry = Entry(root,textvariable = text)
text_entry.grid(row=2,column = 1)

# Label for Hours
hours_label = Label(root, text="Hours", width = 10) 
hours_label.grid(row = 3, column = 0)
hours_label.configure(background="black",foreground="white")

# Entry box for Hours
hours_entry = Entry(root,textvariable = hours)
hours_entry.grid(row=3,column=1)

# Label for Minutes
minutes_label = Label(root, text="Minutes", width = 10) 
minutes_label.grid(row = 4, column = 0)
minutes_label.configure(background="black",foreground="white")

# Entry box for Minutes
minutes_entry = Entry(root,textvariable = minutes)
minutes_entry.grid(row=4,column=1)

# Send Button which will call the sendwhatmsg_to_personal()
generate_send_to_personal_button = Button(root, text="Send_Psnl", command=send_to_personal, width = 10) 
generate_send_to_personal_button.grid(row=6, column=0) 

# Lable for Group_ID
id_label = Label(root, text="Group_ID", width = 10)
id_label.grid(row=5,column=0)
id_label.configure(background="black",foreground="white")

#Entry box for Group_ID
id_entry = Entry(root,textvariable = grp_id)
id_entry.grid(row=5,column=1)

# Send Button which will call sendwhatmsg_to_group()
generate_send_to_group_button = Button(root, text="Send_Grp", command=send_to_group, width = 10) 
generate_send_to_group_button.grid(row=6, column=1) 

# Label for Wiki Search
wiki_label = Label(root, text="Wiki", width = 10)
wiki_label.grid(row=0,column=2)
wiki_label.configure(background="black",foreground="white")

# Entry box for wiki_label
wiki_entry = Entry(root,textvariable = wiki_search)
wiki_entry.grid(row=0,column=3)

# Wiki Search Button which will call wikiSearch()
generate_wiki_search_button = Button(root, text="Search",command=wikiSearch)
generate_wiki_search_button.grid(row=1,column=3)

# Label for YouTube Search
yt_label = Label(root, text="YouTube", width = 10)
yt_label.grid(row=2,column=2)
yt_label.configure(background="black",foreground="white")

# Entry box for Youtube Saerch
yt_entry = Entry(root,textvariable = yt_search)
yt_entry.grid(row=2,column=3)

# Wiki Search Button which will call play_on_youtube()
generate_yt_search_button = Button(root, text="Search",command=play_on_youtube)
generate_yt_search_button.grid(row=3,column=3)

# Label for Google Search
google_label = Label(root, text="Google", width = 10)
google_label.grid(row=4,column=2)
google_label.configure(background="black",foreground="white")

# Entry box for Google Search
google_entry = Entry(root,textvariable = google_search)
google_entry.grid(row=4,column=3)

# Wiki Search Button which will call googleSearch()
generate_google_search_button = Button(root, text="Search",command=googleSearch)
generate_google_search_button.grid(row=5,column=3)

# Label for Sender's Mail Address
sndr_mail_label = Label(root, text="Sender Mail", width = 10)
sndr_mail_label.grid(row=7,column=0)
sndr_mail_label.configure(background="black",foreground="white")

# Entry box for Sender's Mail Address
sndr_mail_entry = Entry(root,textvariable = sndr_mail)
sndr_mail_entry.grid(row=7,column=1)

# Label for Sender's Mail Password
sndr_pass_label = Label(root, text="Sender Pass", width = 10)
sndr_pass_label.grid(row=8,column=0)
sndr_pass_label.configure(background="black",foreground="white")

# Entry box for Sender's Mail Password
sndr_pass_entry = Entry(root,textvariable = sndr_pass, show = '*')
sndr_pass_entry.grid(row=8,column=1)

# Label for Receiver's Mail Address
rcvr_mail_label = Label(root, text="Receiver Mail", width = 10)
rcvr_mail_label.grid(row=9,column=0)
rcvr_mail_label.configure(background="black",foreground="white")

# Entry box for Receiver's Mail Address
rcvr_mail_entry = Entry(root,textvariable = rcvr_mail)
rcvr_mail_entry.grid(row=9,column=1)

# Label for Content
cntnt_label = Label(root, text="Content", width = 10, background="black",foreground="white")
cntnt_label.grid(row=7,column=2)
#cntnt_label.configure(background="black",foreground="white")

# Entry box for Content
cntnt_entry = Entry(root,textvariable = cntnt)
cntnt_entry.grid(row=7,column=3)

# Send Mail Button which will call mail()
generate_send_mail_button = Button(root, text="Send_Mail",command=mail, width = 10)
generate_send_mail_button.grid(row=8,column=3)

# Label for Link
link_label=Label(root, text = 'Link', width=10)
link_label.grid(row=9,column=2)
link_label.configure(background="black",foreground="white")

# Entry box for Link
link_entry = Entry(root, textvariable = link)
link_entry.grid(row=9,column=3)

# Download Button which will call downloader()
generate_link_button=Button(root,text = 'Download', command = downloader, width=7)
generate_link_button.grid(row=10,column=3)

# Button for closing 
generate_exit_button = Button(root, text="Exit", command=root.destroy, width=7) 
generate_exit_button.grid(row=10,column=1)

# START THE GUI
root.mainloop()   
