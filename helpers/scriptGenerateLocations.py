import json
import random

# Given location
latitude = 52.6376
longitude = -1.135171

# Radius
radius = 72

# Activities
activities = ["Trumpet", "Communion", "Worship", "Prayer"]

# Number of objects
num_objects = 3000

# List to store generated objects
features = []

for i in range(num_objects):
   # Generate random offset within the radius
    delta_lat = random.uniform(-1, 1) * (radius / 111000)  # Latitude degrees are approximately 111,000 meters apart

    # Calculate maximum delta longitude based on latitude (approximately 40 kilometers)
    max_delta_lon = (40_000 / (111000 * abs(latitude)))

    # Generate random delta longitude within the maximum range
    delta_lon = random.uniform(-1, 1) * max_delta_lon

    # Calculate new coordinates
    new_lat = latitude + delta_lat
    new_lon = longitude + delta_lon

    # Randomly select an activity
    activity = random.choice(activities)

    # Create object
    obj = {
        "type": "Feature",
        "properties": {
            "geojsonId": i + 1,  # Incremental ID
            "name": f"Location {i + 1}",
            "country": "France",
            "city": "Paris",
            "activity": activity
        },
        "geometry": {
            "type": "Point",
            "coordinates": [new_lon, new_lat]
        }
    }

    # Append object to the list of features
    features.append(obj)

# Create the feature collection
feature_collection = {
    "type": "FeatureCollection",
    "features": features
}

# Write to JSON file
output_file = "../data/mockDataCluster.json"
with open(output_file, "w") as f:
    json.dump(feature_collection, f, indent=2)

print(f"Successfully created JSON file: {output_file}")
