### Geospatial Analysis Script Highlights:

- **Author:** Script written fully by ChatGPT 3.5, prompting and testing managed by Filip Giermek

- **Functionality:** This Python script enhances business warehouse data for geospatial analysis by appending latitude and longitude coordinates based on country and postal code information.
  
- **Libraries Used:**
  - **csv:** Handles CSV file reading and writing.
  - **geopy:** Utilizes Nominatim geocoding service for converting postal codes to latitude and longitude coordinates.
  
- **User Interaction:** Prompts the user to input the name of the CSV file containing country and postal code data.

- **Output Format:** Generates an output CSV file with added latitude and longitude columns.

- **Error Handling:**
  - Handles geocoding timeouts gracefully by writing '---' for latitude and longitude.
  - Provides progress updates and estimates the time remaining until completion.

**Example Input:**

| Country      | Postal Code |
|--------------|-------------|
| Deutschland  | 86647       |
| Deutschland  | 68309       |
| Weissrussland| 220073      |
| Deutschland  | 58119       |

**Example Output:**

| Country      | Postal Code | Latitude     | Longitude    |
|--------------|-------------|--------------|--------------|
| Deutschland  | 86647       | 48.60456226  | 10.718009917894737 |
| Deutschland  | 68309       | 49.51148949277017  | 8.527517391121258 |
| Weissrussland| 220073      | 53.91085271464435  | 27.50985049456067 |
| Deutschland  | 58119       | 51.35629565481893  | 7.570239698639587 |
