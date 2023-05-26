import tkinter as tk
import requests
import time
import screeninfo

def getWeather(root):
    city = cityEntry.get()
    unit = "standard"
    symbol = "K"

    if unitsVariable.get() == "Celsius":
        unit = "metric"
        symbol = "°C"
    elif unitsVariable.get() == "Fahrenheit":
        unit = "imperial"
        symbol = "°F"
    else:
        unit = "standard"
        symbol = "K"

    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f01e80368f05c66b03425d3f08ab1a1c" + "&units=" + unit 

    json_data = requests.get(api).json()
    
    if json_data["cod"] == "404":
        cityEntry.delete(0, tk.END)
        cityEntry.insert(0, "Invalid city")

        return
    
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'])
    min_temp = int(json_data['main']['temp_min'])
    max_temp = int(json_data['main']['temp_max'])
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + symbol
    final_data = "\n" + "Min Temp: " + str(min_temp) + symbol + "\n" + "Max Temp: " + str(
        max_temp) + symbol + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)

screenWidth = screeninfo.get_monitors()[0].width
screenHeight = screeninfo.get_monitors()[0].height

root = tk.Tk()
root.geometry(f"600x500+{int(screenWidth/2-600/2)}+{int(screenHeight/2-500/2)}")
root.title("Weather App")
root.resizable(False, False)

cityLabelFrame = tk.LabelFrame(root, text="Enter a city")
cityLabelFrame.pack(padx=20)

cityEntry = tk.Entry(cityLabelFrame, justify='center', width=20, font=("poppins", 35, "bold"))
cityEntry.pack(padx=20, pady=20)
cityEntry.focus()
cityEntry.bind('<Return>', getWeather)

unitsVariable = tk.StringVar()
units = ["Celsius", "Fahrenheit", "Kelvin"]
optionMenu = tk.OptionMenu(root, unitsVariable, *units)
optionMenu.pack(fill=tk.X, padx=20)
unitsVariable.set("Celsius")

label1 = tk.Label(root, font=("poppins", 35, "bold"))
label1.pack()
label2 = tk.Label(root, font=("poppins", 15, "bold"))
label2.pack()
root.mainloop()