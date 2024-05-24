import csv

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

# Example usage
file_path = 'traverse_data.csv'
traverse_data = read_traverse_data(file_path)
if traverse_data:
    print("Traverse data successfully read:")
    for point in traverse_data:
        print(point)
