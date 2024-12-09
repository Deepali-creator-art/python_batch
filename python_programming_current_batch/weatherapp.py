from tkinter import * #all functions in tkinter library
from tkinter import ttk # importing ttk library
import requests
def data_get():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=123aa9a50ef7c268d5e582791d3f93f4").json()
    print(data)
    wc.config(text=data["weather"][0]["main"])
    wd.config(text=data["weather"][0]["description"])
    temp.config(text=data["main"]["temp"])
    press.config(text=data["main"]["pressure"])
window=Tk()          # create a window
window.title("Weather Application") # title of window
window.geometry("500x500") # set up size of window
window.config(bg='#CCCCFF')
Label(window,text='WEATHER APP',font=("Time New Roman",24,"bold")).place(x=125,y=25)
city_name=StringVar() # declare a variable city_name
# list of india state
list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
Label(window,text='STATE',font=("Time New Roman",16,"bold")).place(x=25,y=100)
c1=ttk.Combobox(window,values=list_name,font=("Time New Roman",16,"bold"),textvariable=city_name)
c1.place(x=125,y=100)
# label for output 
Label(window,text='WEATHER CLIMATE',font=("Time New Roman",12,"bold")).place(x=25,y=145)
Label(window,text='WEATHER DESC',font=("Time New Roman",12,"bold")).place(x=25,y=185)
Label(window,text='TEMPRATURE',font=("Time New Roman",12,"bold")).place(x=25,y=225)
Label(window,text='PRESSURE',font=("Time New Roman",12,"bold")).place(x=25,y=265)
# label for output values
#weather climate
wc=Label(window,text='',font=("Time New Roman",12,"bold"))
wc.place(x=200,y=145,height=28,width=135)
#weather description
wd=Label(window,text='',font=("Time New Roman",12,"bold"))
wd.place(x=200,y=185,height=28,width=135)
#temperature
temp=Label(window,text='',font=("Time New Roman",12,"bold"))
temp.place(x=200,y=225,height=28,width=135)
#pressure
press=Label(window,text='',font=("Time New Roman",12,"bold"))
press.place(x=200,y=265,height=28,width=135)
#Button
b1=Button(window,text='Show Weather',font=("Time New Roman",12,"bold"),command=data_get)
b1.place(x=125,y=350)
window.mainloop()   #running a window
