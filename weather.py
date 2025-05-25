import tkinter as tk
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Initialize root window
root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
# root.configure(bg="white")
root.configure(bg="#F4F3F0")

# Function to get weather and timezone
def getWeather():
    try:
        city = textfield.get()

        # Get weather and coordinates from OpenWeatherMap
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}YOUR_OPENWEATHERMAP_API_KEY"
        response = requests.get(weather_url)
        data = response.json()

        if data.get("cod") != 200:
            raise ValueError("City not found")

        # Extract data
        lat = data['coord']['lat']
        lon = data['coord']['lon']

        condition = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = int(data['main']['temp'] - 273.15)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        # Timezone
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lat=lat, lng=lon)
        timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(timezone).strftime("%I:%M %p")

        # Update UI
        clock.config(text=local_time)
        name.config(text="CURRENT WEATHER")
        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", str(e))

# UI Components

#search box
Search_image = tk.PhotoImage(file="search.png")
myimage = tk.Label(root, image=Search_image, bg="#F4F3F0")  # Add bg to match your root if needed
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 20, "bold"),bg="#404040", border=0, fg="white")
textfield.place(x=60, y=40)
textfield.focus()

Search_icon = tk.PhotoImage(file="search_icon.png")
myimage_icon = tk.Button(root, image=Search_icon, bd=0, cursor="hand2",bg="#404040", activebackground="#F4F3F0", command=getWeather)
myimage_icon.place(x=395, y=31)

#logo
Logo_image = tk.PhotoImage(file="logo.png")
logo = tk.Label(root, image=Logo_image, bg="#F4F3F0")  # Add bg="white" to blend with the root if needed
logo.place(x=170, y=100)

#Bottom box
Frame_image=tk.PhotoImage(file="box.png")
frame_myimage=tk.Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=tk.BOTTOM)

#time
name=tk.Label(root, font=("arial", 12, "bold"))
name.place(x=30,y=100)
clock=tk.Label(root, font=("Helvetica", 17))
clock.place(x=30,y=130)


#label
label1=tk.Label(root, text="WIND", font=("Helvetica", 13, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
label2=tk.Label(root, text="HUMIDITY", font=("Helvetica", 13, 'bold'), fg="white", bg="#1ab5ef")
label2.place (x=250,y=400)
label3=tk.Label(root, text="DESCRIPTION", font=("Helvetica", 13, 'bold'), fg="white", bg="#1ab5ef")
label3.place (x=430,y=400)
label4=tk.Label(root, text="PRESSURE", font=("Helvetica", 13, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t=tk.Label(font=("arial", 60, "bold"), fg="#ee666d")
t.place(x=440,y=150)

c=tk.Label(font=("arial", 12, 'bold'))
c.place(x=440,y=250)

w=tk.Label(text="...", font=("arial", 13, "bold"), bg="#1ab5ef")
w.place(x=120,y=430)
h=tk.Label(text="...", font=("arial", 13, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d=tk.Label(text="...", font=("arial", 13, "bold"), bg="#1ab5ef")
d.place (x=430,y=430)
p=tk.Label(text="...", font=("arial", 13, "bold"), bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()
