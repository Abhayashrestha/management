# Importing custom python files for operations, reading, and writing
import operations
import read
import write

#An empty list to store land data
lands=[]

'''Main interface for the program where functions from different files are called and used to create a functioning user interface for renting and returning land ''' 
def main():
    file_path = 'lands.txt'
    read.load_lands_from_file(file_path) #loads existing land data from file into list by calling fulction from read file

    while True:
        print("\nTechnoPropertyNepal Land Renting System")
        print("1. Display Available Lands")
        print("2. Rent Land")
        print("3. Return Land")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            operations.display_available_lands() #Option to display all available lands from operations file
        elif choice == '2':
            while True:
                try:
                    kitta_number = input("Enter the Kitta Number of the land to rent: ")
                    customer_name = input("Enter the customer name: ")
                    duration = int(input("Enter the rent duration (in months): "))
                    operations.rent_land(kitta_number, customer_name, duration) #Calling rent_land function from operations file
                except Exception as e: #helps to catch and fix general exceptions by displaying and error message
                    
                    print(f"Enter a valid value: {e}")
                
                more_rent= input("Do you wish to rent more land? Y or N") #Choice between renting more land or not
                if more_rent == 'y':
                    continue #goes back to the beginning of while loop
                else:
                    print("ThankYou for renting")
                    break
        elif choice == '3':
            kitta_number = input("Enter the Kitta Number of the land to return: ")
            customer_name = input("Enter the customer name: ")
            duration = int(input("Enter the rent duration (in months): "))
            operations.return_land(kitta_number, customer_name, duration) #Calling return_land function from operations file
        elif choice == '4':
            print("Thank you for using TechnoPropertyNepal Land Renting System!")
            break
        else:
            print("Invalid choice. Please try again.")

main()#Calling main function
