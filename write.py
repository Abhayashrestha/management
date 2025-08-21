file_path = 'lands.txt'
def write_lands_to_file(file_path, lands): #updates the text file as per the commands when called in operations.py
    with open(file_path, 'w') as file:
        for land in lands:
            line = f"{land['kitta_number']}, {land['city_district']}, {land['land_faced']}, {land['anna']}, {land['price']}, {land['status']}\n"
            file.write(line)
