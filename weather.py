import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Your API key and city
api_key = "c5b3cf478350dac1ae3185ead2aad78f"
city = "Mumbai"

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Fetch data from API
response = requests.get(url)
data = response.json()

# Extract useful data
if 'main' in data and 'temp' in data['main']:
    temperature = data['main']['temp']
    print(f"Temperature: {temperature}")
else:
    print("Data structure is not as expected:", data)
humidity = data['main']['humidity']
pressure = data['main']['pressure']
weather_desc = data['weather'][0]['description']

# Print fetched data
print(f"Weather in {city}:")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure} hPa")
print(f"Condition: {weather_desc}")

# Visualize with Matplotlib & Seaborn
sns.set(style="whitegrid")
fig, ax = plt.subplots()

# Data for plotting
labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
values = [temperature, humidity, pressure]

# Bar plot
sns.barplot(x=labels, y=values, palette="coolwarm", ax=ax)
ax.set_title(f"Current Weather Data in {city}")

# Show the graph
plt.show()
