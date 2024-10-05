from geopy.geocoders import Nominatim

def get_coordinates(city_name):
    try:
        # Initialize a geolocator using Nominatim (OpenStreetMap)
        geolocator = Nominatim(user_agent="city_geocoder")

        # Use geocode to get location information for the city
        location = geolocator.geocode(city_name)

        if location:
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        else:
            return None

    except Exception as e:
        return None

if __name__ == "__main__":
    city_name = input("Enter the city name: ")

    coordinates = get_coordinates(city_name)

    if coordinates:
        latitude, longitude = coordinates
        print(f"City: {city_name}")
        print(f"Latitude: {latitude:.6f}")
        print(f"Longitude: {longitude:.6f}")
    else:
        print(f"Coordinates for {city_name} not found.")
