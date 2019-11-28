# Use GeoPy package
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="bimaplus-geolocation")

# Ask a user for the input of the address
address = input("Enter City, Country (e.g. Ljubljana, Slovenia): ")
print("Location address:", address)

# Get the location of the address and print it out to screen
location = geolocator.geocode(address)
print("Latitude and Longitude of the entered address:")
print(location.latitude, location.longitude)
