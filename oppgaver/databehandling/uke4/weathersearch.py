import geocoder
import requests

location = geocoder.arcgis(input("Skriv inn et stedsnavn: "))[0]
lon = location.lng
lat = location.lat

print(f"{location.address} er på lengdegrad {round(lon, 4)} og breddegrad {round(lat, 4)}")

response = requests.get(
    "https://api.met.no/weatherapi/locationforecast/2.0/compact",
    params={"lat": lat, "lon": lon},
    headers={"User-Agent": "Python"},
    timeout=10
)

data = response.json()
temperature = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]

print(f"Temperaturen er {temperature} °C")
