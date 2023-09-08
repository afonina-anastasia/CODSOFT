import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from uszipcode import SearchEngine
from tkinter import messagebox


def get_city(city):
    try:
        sr = SearchEngine()
        z = sr.by_zipcode(city)
        city_z = z.major_city
        return city_z
    except AttributeError:
        messagebox.showinfo("Attention", "an invalid zip code entered.")


def input_button():
    city = name.get()
    weather_info = get_weather(city)
    st.delete("1.0", tk.END)
    st.insert("1.0", weather_info)


def clear():
    name.delete(0, tk.END)
    st.delete("1.0", tk.END)


def get_weather(city):
    try:
        url = (
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&units=metric&lang=en&appid=611d88789ce72b0dc0b5697dc63bfa16"
        )
        response = requests.get(url)

        if response.status_code == 200:
            if city.isdigit():
                weather_data = response.json()
                temperature = round(weather_data["main"]["temp"])
                feels_like_temperature = round(weather_data["main"]["feels_like"])
                wind_speed = round(weather_data["wind"]["speed"])
                description = weather_data["weather"][0]["description"]
                city = get_city(city)
                return (
                    f"Current weather in {city}: {str(temperature)} °C\n"
                    f"Feels like: {str(feels_like_temperature)} °C\n"
                    f"Wind speed: {str(wind_speed)} m/s\n"
                    f"Description: {str(description)}"
                )
            else:
                weather_data = response.json()
                temperature = round(weather_data["main"]["temp"])
                feels_like_temperature = round(weather_data["main"]["feels_like"])
                wind_speed = round(weather_data["wind"]["speed"])
                description = weather_data["weather"][0]["description"]
                return (
                    f"Current weather in {city}: {str(temperature)} °C\n"
                    f"Feels like: {str(feels_like_temperature)} °C\n"
                    f"Wind speed: {str(wind_speed)} m/s\n"
                    f"Description: {str(description)}"
                )
        elif response.status_code == 404:
            return f"City {city} not found"

        else:
            return f"An error occurred: {response.status_code}"

    except requests.ConnectionError:
        return "<Network error>"


def press_key(event):
    print(repr(event.char))
    if event.keysym == "Return":
        input_button()


win = tk.Tk()
win.title("Weather")
win.geometry("490x290+100+200")

photo = tk.PhotoImage(file="5766846.png")
win.config(bg="#F2F7FC")
win.iconphoto(False, photo)
win.bind("<Return>", press_key)


name = tk.Entry(win)
name.grid(row=0, column=1, stick="wens", padx=1, pady=1)

tk.Label(win, text="Enter city names or zip codes").grid(row=0, column=0, sticky="w")

button = tk.Button(
    win, text="Get Weather", font=("Arial", 12, "bold"), fg="blue", command=input_button
)
button.grid(row=0, column=2, stick="wens", padx=1, pady=1)

button = tk.Button(
    win, text="Delete", font=("Arial", 12, "bold"), fg="blue", command=clear
)
button.grid(row=1, column=2, stick="wens", padx=1, pady=1)

st = ScrolledText(
    win, height=10, width=50, font=("Arial", 12), wrap="word", spacing1=10
)
st.grid(row=1, column=0, columnspan=2)


tk.Label(
    win,
    text="Enter city names or zip codes",
    font=("Arial", 12, "bold"),
    fg="blue",
    width=15,
).grid(row=0, column=0, stick="wens", padx=1, pady=1)

win.grid_columnconfigure(0, minsize=40)
win.grid_columnconfigure(1, minsize=40)
win.grid_columnconfigure(2, minsize=40)
win.grid_columnconfigure(3, minsize=40)

win.grid_rowconfigure(0, minsize=40)
win.grid_rowconfigure(1, minsize=40)
win.mainloop()
