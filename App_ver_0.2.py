from tkinter import *
from PIL import Image, ImageTk
import requests

root = Tk()
root.geometry("480x320")
root.title("Weather! Now 🌤️")

#---- Load background Image ------
bg_image = Image.open(r"D:\weather.jpg") 
bg_photo = ImageTk.PhotoImage(image = bg_image)

#----- creating canvas----
canvas = Canvas(root,width=480,height=320)
canvas.pack(fill="both", expand= True)

# Adding the bg Image
canvas.create_image(0,0,image= bg_photo,anchor= "nw")


#---- Add widgets----
city_label = Label(root, text="Enter city name ",font=16,bg="lightblue")
city_entry = Entry(root)

button = Button(root,text="Get Weather")

#--- result label (blank at first)

result_label = Label(root,text="",font=("Aerial",16),bg="lightblue")

canvas.create_window(240,50,window=city_label) # x= 240 center horizontally
canvas.create_window(240,100,window=city_entry) # entry box
canvas.create_window(240,128,window=button)
canvas.create_window(240,170,window=result_label)

API_key = "81803dda60468b87287a879ab670f0b5"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"

    try:
        response = requests.get(url)
        print("Status code:", response.status_code)   # debug
        print("Raw response:", response.text)         # debug

        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            city_name = data['name']

            result_label.config(text=f"{city_name}\n{temp}°C,{desc}")

        else:
            result_label.config(text="City not found")


    except :
        result_label.config(text="Opps! No internet,\nPlease check your connection")

# --- Button action ---
button.config(command=lambda:get_weather(city_entry.get()))

root.mainloop()