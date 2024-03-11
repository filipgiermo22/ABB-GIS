import csv
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Initialize Nominatim geocoder with a custom user agent
geolocator = Nominatim(user_agent="my_geocoder")

# Function to estimate the approximate time until finishing
def estimate_time_to_finish(total_rows, rows_processed, start_time):
    current_time = time.time()
    elapsed_time = current_time - start_time
    time_per_row = elapsed_time / rows_processed
    remaining_rows = total_rows - rows_processed
    remaining_time = remaining_rows * time_per_row
    return remaining_time

# Prompt user for input CSV file name
input_csv_file = input("Enter the input CSV file name (including extension): ")

# Prepare output CSV file name
output_csv_file = 'latitude_longitude_output.csv'

# Open output CSV file for writing
with open(output_csv_file, mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Country', 'Postal Code', 'Latitude', 'Longitude'])

    # Read data from input CSV file
    with open(input_csv_file, mode='r', newline='') as input_file:
        reader = csv.reader(input_file)
        rows = list(reader)
        total_rows = len(rows)
        start_time = time.time()
        rows_processed = 0
        for row in rows:
            rows_processed += 1
            country = row[0]
            postal_code = row[1]
            try:
                location_info = geolocator.geocode(f"{postal_code}, {country}")
                if location_info:
                    latitude = location_info.latitude
                    longitude = location_info.longitude
                    print(f"Successfully processed: {country}, {postal_code}. Latitude: {latitude}, Longitude: {longitude}")
                    writer.writerow([country, postal_code, latitude, longitude])  # Write data to output CSV file
                else:
                    print(f"No data found for {country}, {postal_code}. Writing '---' instead.")
                    writer.writerow([country, postal_code, "---", "---"])  # Write '---' if no data found
            except GeocoderTimedOut:
                print(f"Geocoding service timed out for {country}, {postal_code}. Writing '---' instead.")
                writer.writerow([country, postal_code, "---", "---"])  # Write '---' if geocoding timed out
            remaining_time = estimate_time_to_finish(total_rows, rows_processed, start_time)
            print(f"Approximate time until finishing: {remaining_time:.2f} seconds")
        print("All rows processed.")

print("Geocoding finished.")
