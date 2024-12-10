import csv
from datetime import datetime

def load_uber_data(filepath):
    """Load and preprocess Uber trip data from CSV file."""
    trips = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert string datetime to Python datetime object
                row['pickup_datetime'] = datetime.strptime(row['pickup_datetime'], '%Y-%m-%d %H:%M:%S')
                row['dropoff_datetime'] = datetime.strptime(row['dropoff_datetime'], '%Y-%m-%d %H:%M:%S')
                # Convert string numbers to float
                row['distance'] = float(row['distance'])
                row['fare'] = float(row['fare'])
                trips.append(row)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None
    
    return trips