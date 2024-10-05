from geopy.geocoders import Nominatim

# Create geolocater object
geolocator = Nominatim(user_agent="location_app")

try:
    location = geolocator.geocode("")

    if location:
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
        print(f"Location: {location.address}")
    else:
        print("location not found")
except Exception as e:
    print(f"An error occurred: {str(e)}")
