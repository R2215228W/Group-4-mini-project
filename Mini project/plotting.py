import csv
import os.path
import matplotlib.pyplot as plt

def read_traverse_data(file_path):
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return None
    
    traverse_data = []
    
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip header row
        if header != ['Point', 'Easting', 'Northing']:
            print("Error: Invalid CSV format.")
            return None
        
        for row in csv_reader:
            try:
                point_number = row[0]
                easting = float(row[1])
                northing = float(row[2])
                traverse_data.append((point_number, easting, northing))
            except (IndexError, ValueError) as e:
                print(f"Error in row {csv_reader.line_num}: {e}")
    
    return traverse_data

def plot_traverse(traverse_data):
    if not traverse_data:
        print("Error: No traverse data provided.")
        return
    
    point_numbers = [point[0] for point in traverse_data]
    eastings = [point[1] for point in traverse_data]
    northings = [point[2] for point in traverse_data]
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    plt.scatter(eastings, northings, color='blue', label='Traverse Points')
    for i, point in enumerate(traverse_data):
        plt.annotate(point[0], (point[1], point[2]), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Easting')
    plt.ylabel('Northing')
    plt.title('Traverse Scatter Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
file_path = 'traverse_data.csv'
traverse_data = read_traverse_data(file_path)
if traverse_data:
    print("Traverse data successfully loaded.")
    plot_traverse(traverse_data)
