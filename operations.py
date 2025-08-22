import read
import write
import datetime
lands=[]

#Function to display all available lands for renting purpose
def display_available_lands():
    lands = read.load_lands_from_file('lands.txt')
    if lands:
        print("Available Lands:")
        for land in lands:
            if land['status'] == 'Available':
                print(f"Kitta Number: {land['kitta_number']}, City/District: {land['city_district']}, Land Faced: {land['land_faced']}, Anna: {land['anna']}, Price: {land['price']}")
    else:
        print("No lands available or issue with file loading.")

#Function that lets the user rent available lands and also updates the text file
def rent_land(kitta_number, customer_name, duration):
    #using try except for exception handling in the program during execution
    try:
        lands = read.load_lands_from_file('lands.txt')
        for land in lands:
            if land['kitta_number'] == kitta_number and land['status'] == 'Available':
                land['status'] = 'Not Available'
                write.write_lands_to_file('lands.txt', lands) #updates the text file changing the status of land
                generate_rent_invoice(land, customer_name, duration)#calling generate_rent_invoice function to generate a bill text file
                prnt_bills_rent(land, customer_name, duration)#calling prnt_bills_rent to print bill on screen for user after renting a land 
                break
        else:
            print(f"Land with Kitta Number {kitta_number} is not available for rent.")
    except FileNotFoundError: #helps to handle the file not found error smoothly
        print("Error: File not found. Please check the file path.")
    except Exception as e: #helps to catch and fix general exceptions by displaying and error message
        print(f"Error renting land: {e}")
        
def return_land(kitta_number, customer_name, duration):
    try:
        lands = read.load_lands_from_file('lands.txt')
        for land in lands:
            if land['kitta_number'] == kitta_number and land['status'] == 'Not Available':
                land['status'] = 'Available'
                write.write_lands_to_file('lands.txt', lands)#updates the text file changing the status of land
                generate_return_invoice(land, customer_name, duration) #calling generate_return_invoice function to generate a bill text file
                prnt_bills_return(land, customer_name, duration)#calling prnt_bills_return to print bill on screen for user after returning a land 
                break
        else:
            print(f"Land with Kitta Number {kitta_number} is not currently rented.")
    except FileNotFoundError: #helps to handle the file not found error smoothly
        print("Error: File not found. Please check the file path.")
    except Exception as e: #helps to catch and fix general exceptions by displaying and error message
        print(f"Error returning land: {e}")

        
''' The following functions contain codes to print bills for users after returning or renting and also to generate an invoice text file after each transaction hepling TechnoPropoerty Nepal keep proper track through text files'''

def prnt_bills_rent(land, customer_name, duration):#function to print bills of rented land on screen
    total_amount = land['price'] * duration #calculation of total amount
    invoice_name = f"rent_invoice_{land['kitta_number']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    print(f"Rent Invoice\n")
    print(f"--------------------------------------------------------------------------------\n")
    print(f"Kitta Number: {land['kitta_number']}\n")
    print(f"City/District: {land['city_district']}\n")
    print(f"Land Faced: {land['land_faced']}\n")
    print(f"Anna: {land['anna']}\n")
    print(f"Customer Name: {customer_name}\n")
    print(f"Rent Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Rent Duration (months): {duration}\n")
    print(f"Total Amount: Rs. {total_amount}\n")
    print(f"--------------------------------------------------------------------------------\n")
    print(f"Rent invoice generated: {invoice_name}")

def prnt_bills_return(land, customer_name, duration):#function to print bills of returned land on screen
    total_amount = land['price'] * duration#calculation of total amount
    invoice_name = f"return_invoice_{land['kitta_number']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    print(f"Return Invoice\n")
    print(f"--------------------------------------------------------------------------------\n")
    print(f"Kitta Number: {land['kitta_number']}\n")
    print(f"City/District: {land['city_district']}\n")
    print(f"Land Faced: {land['land_faced']}\n")
    print(f"Anna: {land['anna']}\n")
    print(f"Customer Name: {customer_name}\n")
    print(f"Return Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Rent Duration (months): {duration}\n")
    print(f"Total Amount: Rs. {total_amount}\n")
    print(f"--------------------------------------------------------------------------------\n")
    print(f"Return invoice generated: {invoice_name}")

def generate_rent_invoice(land, customer_name, duration): #function to write in the invoice text file and generate a bill in that file after renting
    total_amount = land['price'] * duration
    invoice_name = f"rent_invoice_{land['kitta_number']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt" #datetime.now is used to create a new unique id of Bill each time a transaction occurs
    with open(invoice_name, 'w') as file:
        file.write(f"Rent Invoice\n")
        file.write(f"Kitta Number: {land['kitta_number']}\n")
        file.write(f"City/District: {land['city_district']}\n")
        file.write(f"Land Faced: {land['land_faced']}\n")
        file.write(f"Anna: {land['anna']}\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Rent Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Rent Duration (months): {duration}\n")
        file.write(f"Total Amount: Rs. {total_amount}\n")
    print(f"Rent invoice generated: {invoice_name}")
    
def generate_return_invoice(land, customer_name, duration): #function to write in the invoice text file and generate a bill in that file after returning
    total_amount = land['price'] * duration
    invoice_name = f"return_invoice_{land['kitta_number']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt" #datetime.now is used to create a new unique id of Bill each time a transaction occurs
    with open(invoice_name, 'w') as file:
        file.write(f"Return Invoice\n")
        file.write(f"Kitta Number: {land['kitta_number']}\n")
        file.write(f"City/District: {land['city_district']}\n")
        file.write(f"Land Faced: {land['land_faced']}\n")
        file.write(f"Anna: {land['anna']}\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Rent Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Rent Duration (months): {duration}\n")
        file.write(f"Total Amount: Rs. {total_amount}\n")
    print(f"Return invoice generated: {invoice_name}")
