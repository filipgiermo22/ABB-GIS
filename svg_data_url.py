import base64

def create_data_url(svg_file_path):
    # Read the SVG file
    with open(svg_file_path, 'rb') as f:
        svg_content = f.read()
    
    # Encode the SVG content using Base64
    encoded_svg = base64.b64encode(svg_content).decode('utf-8')
    
    # Construct the Data URL
    data_url = f'data:image/svg+xml;base64,{encoded_svg}'
    
    return data_url

def main():
    svg_file_path = input("Enter the path to your SVG file: ")
    data_url = create_data_url(svg_file_path)
    print("Data URL for the SVG file:")
    print(data_url)

if __name__ == "__main__":
    main()
