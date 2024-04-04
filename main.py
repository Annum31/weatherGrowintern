import requests
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz


window= tk.Tk()
window.title("Weather App")
window.geometry("900x500+300+200")
window.resizable(False,False)

def getWeather():
    try:
       city= textfield.get()

       geolocator= Nominatim(user_agent="geoapiExercises")
       location= geolocator.geocode(city)
       obj= TimezoneFinder()
       result= obj.timezone_at(lng=location.longitude,lat=location.latitude)

       home= pytz.timezone(result)
       local_time=datetime.now(home)
       current_time=local_time.strftime('%H:%M:%S %p')
       clock.config(text=current_time)
       t.after(1000,current_time)
       name.config(text="CURRENT WEATHER")
     #weather
       api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9cf6388abfaee1d3dc4091fde4daa25d"

       json_data = requests.get(api).json()
       condition = json_data['weather'][0]['main']
       description = json_data['weather'][0]['description']
       temp = int(json_data['main']['temp']-273.15)
       max_temp = int(json_data['main']['temp_max']-273.15)
       pressure = json_data['main']['pressure']
       humidity = json_data['main']['humidity']
       wind= json_data['wind']['speed']
       #sunrise = t.strftime("%I:%M:%S",t.gmtime(json_data['sys']['sunrise']-21600))
       #sunset = t.strftime("%I:%M:%S",t.gmtime(json_data['sys']['sunset']-21600))


       t.config(text=(temp,"°"))
       c.config(text=(condition, "|", "FEELS LIKE", f"{temp}°"))

       w.config(text=wind)
       d.config(text=humidity)
       p.config(text=description)
       q.config(text=pressure)
    except Exception as e:
       messagebox.showerror("weather App", "Invalid Entry!!")
#Search Box
search_image= PhotoImage(file="search.png")
my_image=Label(image=search_image)
my_image.place(x=20,y=20)

textfield=tk.Entry(window, justify="center",width=17,font=("poppins",25,"bold"),foreground="white",background="#404040",border=0,)
textfield.place(x=50,y=40)
textfield.focus()
#search icon
search_icon= PhotoImage(file="search_icon.png")
my_image_icon= Button(image=search_icon,borderwidth=0,cursor="hand2",background="#404040",command=getWeather)
my_image_icon.place(x=400,y=34)
#logo
logo_image= PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)
#Bottom Box
Frame_image= PhotoImage(file="box.png")
frame_myimage= Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#Time
name= Label(window,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(window,font=("Helvetica",20,"bold"))
name.place(x=30,y=130)
#Label
Label1=Label(window,text="Wind",font=("Helvetica",15,'bold'),foreground="white",background="#1ab5ef")
Label1.place(x=120,y=400)

Label2=Label(window,text="Humidity",font=("Helvetica",15,'bold'),foreground="white",background="#1ab5ef")
Label2.place(x=250,y=400)

Label3=Label(window,text="Description",font=("Helvetica",15,'bold'),foreground="white",background="#1ab5ef")
Label3.place(x=430,y=400)

Label4=Label(window,text="Pressure",font=("Helvetica",15,'bold'),foreground="white",background="#1ab5ef")
Label4.place(x=650,y=400)

t= Label(font=("arial",70,"bold"),foreground="#ee666b")
t.place(x=400,y=150)

c= Label(font=("arial",15,"bold"), foreground="#ee666b")
c.place(x=400,y=250)

w= Label(text="...",font=("arial",20,"bold"),background="#1ab5ef")
w.place(x=120,y=430)

d= Label(text="...",font=("arial",20,"bold"),background="#1ab5ef")
d.place(x=280,y=430)

p= Label(text="...",font=("arial",20,"bold"),background="#1ab5ef")
p.place(x=470,y=430)

q= Label(text="...",font=("arial",20,"bold"),background="#1ab5ef")
q.place(x=680,y=430)
    
window.mainloop()