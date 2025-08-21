'''The block of code below reads data from the lands.txt file and stores it in the empty list lands'''
def load_lands_from_file(file_path):
    lands = []
    #File not found error handling using try except block
    try: 
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if len(data) == 6:
                    land = {
                        'kitta_number': data[0],
                        'city_district': data[1],
                        'land_faced': data[2],
                        'anna': int(data[3]),
                        'price': int(data[4]),
                        'status': data[5]
                    }
                    lands.append(land)
                else:
                    print(f"Issue with line in file: {line}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return lands
