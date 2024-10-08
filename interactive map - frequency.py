# Topic: distant reading of Bandcamp fundraisers/ fundraisers geographical distribution on OpenStreetMap
# Author: Hana Arshid
# Date: 06/10/2024

import folium
from collections import Counter

# Sample location data
locations = [
    "Berlin, Germany",
    "Stockholm, Sweden",
    "Beirut, Lebanon",
    "Kilkenny, Ireland",
    "Pittsburgh, Pennsylvania",
    "Berlin, Germany",
    "London, UK",
    "Germany",
    "Philadelphia, Pennsylvania",
    "Buffalo, New York",
    "Lyon, France",
    "Rome, Italy",
    "Turin, Italy",
    "UK",
    "London, UK",
    "Indiana, USA",
    "New Zealand",
    "Apache Junction, Arizona",
    "Dublin, Ireland",
    "Italy",
    "GA, Spain",
    "Turin, Italy",
    "Rouen, France",
    "New York, New York",
    "London, UK",
    "Palestine",
    "New York, New York"
]

# Count frequency of each location
location_counts = Counter(locations)

# Create a map centered around the approximate center of the locations
m = folium.Map(location=[20, 0], zoom_start=2)  # World view

# Define a function to get coordinates based on location
def get_coordinates(location):
    coordinates = {
        "Berlin, Germany": [52.52, 13.405],
        "Stockholm, Sweden": [59.3293, 18.0686],
        "Beirut, Lebanon": [33.8938, 35.5018],
        "Kilkenny, Ireland": [52.6542, -7.2539],
        "Pittsburgh, Pennsylvania": [40.4406, -79.9959],
        "London, UK": [51.5074, -0.1278],
        "Germany": [51.1657, 10.4515],  # Central point for Germany
        "Philadelphia, Pennsylvania": [39.9526, -75.1652],
        "Buffalo, New York": [42.8864, -78.8784],
        "Lyon, France": [45.7640, 4.8357],
        "Rome, Italy": [41.9028, 12.4964],
        "Turin, Italy": [45.0703, 7.6869],
        "UK": [55.3781, -3.4360],  # Central point for the UK
        "Indiana, USA": [39.7910, -86.7816],
        "New Zealand": [-40.9006, 174.8860],
        "Apache Junction, Arizona": [33.4152, -111.5492],
        "Dublin, Ireland": [53.3498, -6.2603],
        "Italy": [41.8719, 12.5674],  # Central point for Italy
        "GA, Spain": [37.3572, -5.9920],
        "Rouen, France": [49.4432, 1.0991],
        "New York, New York": [40.7128, -74.0060],
        "Palestine": [31.9522, 35.2332],  # Approximate center for Palestine
    }
    return coordinates.get(location, [0, 0])  # Default to [0, 0] if not found

# Define continent colors
continent_colors = {
    "North America": "blue",
    "South America": "green",
    "Europe": "orange",
    "Africa": "red",
    "Asia": "purple",
    "Oceania": "magenta",  
    "Antarctica": "gray",
}

# Define a function to get continent based on location
def get_continent(location):
    continents = {
        "Germany": "Europe",
        "Sweden": "Europe",
        "Lebanon": "Asia",
        "Ireland": "Europe",
        "Pennsylvania": "North America",
        "New York": "North America",
        "UK": "Europe",
        "Italy": "Europe",
        "Spain": "Europe",
        "New Zealand": "Oceania",
        "Palestine": "Asia",
        "Arizona": "North America",
        "France": "Europe",  
        "Indiana": "North America",  
    }
    for key in continents:
        if key in location:
            return continents[key]
    return None  # Return None if not found

# Add circle markers for each location
for location, frequency in location_counts.items():
    coords = get_coordinates(location)
    continent = get_continent(location)
    color = continent_colors.get(continent, 'black')  # Use defined continent colors

    folium.CircleMarker(
        location=coords,
        radius=frequency * 2,  
        popup=f"{location}: {frequency}",
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6
    ).add_to(m)

# Save map
m.save('city_frequency_map_with_continent_colors.html')
print("Map has been created and saved as 'city_frequency_map_with_continent_colors.html'.")
