import csv
import math

def read_traverse_data(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
            if header != ['Point', 'Easting', 'Northing']:
                raise ValueError("Incorrect file format. Header should be 'Point Number, Easting, Northing'.")
            
            traverse_data = []
            for row in reader:
                # Assuming the data format is: Point Number, Easting, Northing
                point_number, easting, northing = row
                traverse_data.append({
                    'Point': point_number,
                    'Easting': float(easting),
                    'Northing': float(northing)
                })
            return traverse_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"Error: {e}")

def calculate_traverse_characteristics(traverse_data):
    num_points = len(traverse_data)
    eastings = [point['Easting'] for point in traverse_data]
    northings = [point['Northing'] for point in traverse_data]
    min_easting = min(eastings)
    max_easting = max(eastings)
    min_northing = min(northings)
    max_northing = max(northings)
    return {
        'Total Points': num_points,
        'Min Easting': min_easting,
        'Max Easting': max_easting,
        'Min Northing': min_northing,
        'Max Northing': max_northing
    }

def calculate_distance(point1, point2):
    delta_easting = point2['Easting'] - point1['Easting']
    delta_northing = point2['Northing'] - point1['Northing']
    distance = math.sqrt(delta_easting**2 + delta_northing**2)
    return distance

def calculate_bearing(point1, point2):
    delta_easting = point2['Easting'] - point1['Easting']
    delta_northing = point2['Northing'] - point1['Northing']
    bearing = math.atan2(delta_easting, delta_northing)
    # Convert bearing from radians to degrees
    bearing_degrees = math.degrees(bearing)
    # Ensure bearing is between 0 and 360 degrees
    bearing_degrees = (bearing_degrees + 360) % 360
    return bearing_degrees

def main():
    file_path = 'traverse_data.csv'
    traverse_data = read_traverse_data(file_path)
    if traverse_data:
        traverse_characteristics = calculate_traverse_characteristics(traverse_data)
        print("Traverse Characteristics:")
        for characteristic, value in traverse_characteristics.items():
            print(f"{characteristic}: {value}")

        # Calculate distance and bearing between two points provided by the user
        point1_number = input("Enter the point number of the first point: ")
        point2_number = input("Enter the point number of the second point: ")
        
        point1 = next((point for point in traverse_data if point['Point'] == point1_number), None)
        point2 = next((point for point in traverse_data if point['Point'] == point2_number), None)
        
        if point1 and point2:
            distance = calculate_distance(point1, point2)
            bearing = calculate_bearing(point1, point2)
            print(f"Distance between {point1_number} and {point2_number}: {distance}")
            print(f"Bearing from {point1_number} to {point2_number}: {bearing} degrees")
        else:
            print("Error: One or both points not found in the traverse data.")

if __name__ == "__main__":
    main()
