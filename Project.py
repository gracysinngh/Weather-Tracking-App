
from tkinter import *
from tkinter import ttk
import requests 



def data_get():
    city=city_name.get()

    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9a14cbefe80fbda01b3e4181ca11e90d").json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])

    temp = data["main"]["temp"] - 273.15
    temp_label1.config(text=f"{temp:.2f} °C")

    per_label1.config(text=data["main"]["pressure"])

# create window
win = Tk()

# window settings
win.title("MY First python project")
win.config(bg="teal")
win.geometry("550x550")

# heading label
name_Label = Label(win, text = "Weather Fetch", font = ("Arial", 30, "bold"))

name_Label.place(x=70, y=50, height=50, width=320)
list_name=["Ludhiana","Chandigarh","Delhi","Mumbai","Kolkata","Bangalore","Hyderabad"]

city_name=StringVar()

com=ttk.Combobox(win,text="Select City", values=list_name, font=("Arial",30,"bold"),textvariable=city_name)

com.place(x=70,y=120,height=40,width=320)

done_button = Button(win, text="Get Data", font=("Arial", 18, "bold"), command=data_get)
done_button.place(x=130, y=180, height=50, width=200)

w_label = Label(win, text="Weather Climate", font=("Arial", 20))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Arial", 20))
w_label1.place(x=260, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Arial", 17))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Arial", 17))
wb_label1.place(x=260, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Arial", 20))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Arial", 20))
temp_label1.place(x=260, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Arial", 20))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Arial", 20))
per_label1.place(x=260, y=470, height=50, width=210)


# run window
win.mainloop()
