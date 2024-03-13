### Geospatial Analysis Script Highlights:

- **Author:** Script written fully by ChatGPT 3.5, prompting and testing managed by Filip Giermek

- **Functionality:** This repository contains Python scripts aimed at enhancing business warehouse data for geospatial analysis
  -  **gis.py** by appending latitude and longitude coordinates based on country and postal code information
  -  **svg_data_url** by converting SVG files to Base64-encoded data URLs, for usage in IconMap plugin
  
- **Libraries Used:**
  - **csv:** Handles CSV file reading and writing.
  - **geopy:** Utilizes Nominatim geocoding service for converting postal codes to latitude and longitude coordinates.
  - **base64**: Provides functionality for encoding SVG images into Base64 format for use in Power BI.
  
- **User Interaction:** Prompts the user to input the name of the CSV file containing country and postal code data, as well as the SVG file path for encoding.

- **Output Format:** The geospatial analysis script generates an output CSV file with added latitude and longitude columns, while the SVG encoding script produces a Base64-encoded data URL for the SVG file.

- **Error Handling:**
  - Handles geocoding timeouts gracefully by writing '---' for latitude and longitude.
  - Provides progress updates and estimates the time remaining until completion.
  - The SVG encoding script ensures proper handling of file reading and encoding errors.

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

For SVG Encoding Script:

This Python script facilitates the conversion of SVG files into Base64-encoded data URLs. It accepts the path to an SVG file as input and produces a Data URL that can be directly embedded into HTML or CSS, enabling seamless integration of SVG images into Power BI reports using the IconMap plugin or similar features. This functionality enhances the visualization capabilities of Power BI by allowing the use of custom SVG images alongside geospatial data analysis.
