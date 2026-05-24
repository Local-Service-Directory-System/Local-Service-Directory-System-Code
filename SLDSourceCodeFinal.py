
#TO CLEAR
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


#TO SAVE FILE
import json

def saveToFile():
    with open("workersfile.json", "w") as f:
        json.dump(workers, f, indent=4)

def loadFromFile():
    global workers
    try:
        with open("workersfile.json", "r") as f:
            workers = json.load(f)
    except FileNotFoundError:
        workers = []

loadFromFile()

#INSERTION SORT FUNCTION-------------------------------------------

def insertionSort():

    for i in range(1, len(workers)):
        current = workers[i]
        j = i - 1
        while j >= 0 and workers[j]["firstName"].lower() > current["firstName"].lower():
            workers[j + 1] = workers[j]
            j -= 1
        workers[j + 1] = current

    print("Workers sorted successfully.")

#BINARY SEARCH FUNCTION------------------------------------------------

def binarySearch(target):

    low = 0
    high = len(workers) - 1

    while low <= high:
        mid = (low + high) // 2
        currentProf = workers[mid]["profession"].lower()

        if currentProf == target.lower():
            return mid

        elif currentProf < target.lower():
            low = mid + 1

        else:
            high = mid - 1

    return -1
#ADD WORKER--------------------------------------------------------

def addWorker():

    print("\n=== Post Application ===")

    while True:
        firstName = input("Enter first name: ").strip()
        if firstName == "" or not firstName.replace(" ", "").isalpha():
            print("Invalid first name. Try Again")
            continue
        firstName = firstName.title()
        break

    while True:
        lastName = input("Enter last name: ").strip()
        if lastName == "" or not lastName.replace(" ", "").isalpha():
            print("Invalid last name. Try Again")
            continue
        lastName = lastName.title()
        break

    while True:
        barangay = input("Enter barangay: ").strip()
        if barangay == "":
            print("Invalid input. Try Again")
            continue
        barangay = barangay.title()
        break

    zone = input("Enter zone: ").strip().title()

    while True:
        profession = input("Enter profession: ").strip()
        if profession == "" or not profession.replace(" ", "").isalpha():
            print("Invalid profession. Try Again")
            continue
        profession = profession.title()
        break
        
    while True:
        try:
            hourRate = int(input("Enter hourly rate($): "))
            break
        except ValueError:
            print("Invalid input. Try Again")

    while True:
        contact = input("Enter contact number: ").strip()
        if contact[:2] == '09' and len(contact) == 11 and contact.isdigit():
            contact = int(contact)
            break
        print("Invalid input. Try Again")
        

    while True:
        socialMedia = input("Social Media Account (ex. Facebook Juan Cruz): ")
        if socialMedia.strip() == "" or socialMedia.strip().isdigit():
            print("Invalid input. Try Again")
        else:
            socialMedia = socialMedia.title()
            break


    worker = {
        "firstName": firstName,
        "lastName": lastName,
        "barangay": barangay,
        "zone": zone,
        "profession": profession,
        "hourRate": hourRate,
        "contact": contact,
        "socialMedia": socialMedia
    }

    workers.append(worker)

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Worker added successfully.")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    input("Press Enter to continue...")
    saveToFile()

#DISPLAY ALL WORKERS-------------------------------------------------

def displayWorkers():

    if len(workers) == 0:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("No workers found.")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        return

    print("\n====SERVICE PROVIDERS====")
    for i, worker in enumerate(workers):
        print(f"#{i+1} {worker['firstName']} {worker['lastName']} — {worker['profession']}")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    while True:
        try:
            choice = int(input("Enter worker number to view details (0 to go back): "))
            if choice == 0:
                return
            elif 1 <= choice <= len(workers):
                worker = workers[choice - 1]
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"Worker #{choice}")
                print("Name:", worker["firstName"], worker["lastName"])
                print("Barangay:", worker["barangay"])
                print("Zone:", worker["zone"])
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("Profession:", worker["profession"])
                print("Hourly Rate:", worker["hourRate"])
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("Contact Number:", worker["contact"])
                print("Social Media Account:", worker["socialMedia"])
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                hire = input("Do you want to hire this worker? (y/n): ")
                if hire.lower() == "y":
                    cls()
                    print(f"\nWorker chosen: {worker['firstName']} {worker['lastName']}")
                    print(f"A message has been sent. Please refer to 0{worker['contact']} for more communication and contact.")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                else:
                    print("\nSorry, this worker was not the perfect fit. Please press Enter to go back to menu.")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                input("Press Enter to continue...")
                return
            else:
                print("Invalid number. Try Again")
        except ValueError:
            print("Invalid input. Try Again")

        input("Press Enter to continue...")

#SEARCH WORKER------------------------------------------------------

def searchWorker():
    insertionSort()
    target = input("Enter expertise/profession to search: ")
    result = binarySearch(target)
    if result != -1:
        cls()
        worker = workers[result]
        print("\nWorker Found!!!")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Name:", worker["firstName"], worker["lastName"])
        print("Barangay:", worker["barangay"])
        print("Zone:", worker["zone"])
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Profession:", worker["profession"])
        print("Hourly Rate:", worker["hourRate"])
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Contact Number:", worker["contact"])
        print("Social Media Account:", worker["socialMedia"])
        hire = input("Do you want to hire this worker? (y/n): ")
        if hire.lower() == "y":
                    cls()
                    print(f"\nWorker chosen: {worker['firstName']} {worker['lastName']}")
                    print(f"A message has been sent. Please refer to 0{worker['contact']} for more communication and contact.")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        else:
            print("\nSorry, this worker was not the perfect fit. Please press Enter to go back to menu.")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    else:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("No available workers at the moment.")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    input("Press Enter to continue...")

#UPDATE WORKER----------------------------------------------------------

def updateWorker():
    target = input("Enter first name to update: ")
    for worker in workers:
        if worker["firstName"].lower() == target.lower():
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("\nWorker Found")
            print("\n--=Enter new information=--")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            worker["firstName"] = input("New first name: ")
            worker["lastName"] = input("New last name: ")
            worker["barangay"] = input("New barangay: ")
            worker["zone"] = input("New zone: ")
            worker["profession"] = input("New profession: ")

            while True:
                try:
                    worker["hourRate"] = int(input("New hourly rate: "))
                    break
                except ValueError:
                    print("Invalid input. Try Again")
            print("Worker updated successfully.")

            while True:
                contact = input("Enter contact number: ").strip()
                if contact[:2] == '09' and len(contact) == 11 and contact.isdigit():
                    contact = int(contact)
                    break
                print("Invalid input. Try Again")

            while True:
                socialMedia = input("Social Media Account (ex. Facebook Juan Cruz): ")
                if socialMedia.isdigit():
                    print("Invalid input. Try Again")
                else:
                    break
    
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Worker updated successfully.")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            return
        
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Worker not found.")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    input("Press Enter to continue...")

    saveToFile()
#REMOVE WORKER-------------------------------------------------
def removeWorker():
    target = input("Enter first name to remove: ")
    for worker in workers:
        if worker["firstName"].lower() == target.lower():
            workers.remove(worker)
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Worker removed successfully.")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Worker not found.")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    saveToFile()

    input("Press Enter to continue...")


#MENU---------------------------------------------------------------------
loadFromFile()
while True:
    cls()
    print("╔═══════════════════════════════╗")
    print("║=== LOCAL SERVICE DIRECTORY ===║")
    print("║═══════════════════════════════║")
    print("║1. Post Application            ║")
    print("║2. Hire Workers                ║")
    print("║3. Admin Options               ║")
    print("║4. Exit                        ║")
    print("╚═══════════════════════════════╝")

    choice = input("Enter choice: ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    if choice == "1": #Post Aplication
        cls()
        addWorker()

    elif choice == "2": #Hire workers
        while True:
            cls()
            print("---= HIRE WORKERS =---")
            print("╔════════════════════╗") 
            print("║1. Search Worker    ║")
            print("║2. Display Workers  ║")
            print("║3. Back             ║")
            print("╚════════════════════╝")


            choiceTwo = input("Enter choice: ")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            if choiceTwo == "1":
                searchWorker()
        
            elif choiceTwo == "2":
                displayWorkers()

            elif choiceTwo == "3":
                break

            else:
                print("Invalid Input. Try Again")

    elif choice == "3":
        adminPassword = "IloveUSTP!"  #PASS NI NATO
        enteredPassword = input("Enter admin password to access operations: ")
        if enteredPassword != adminPassword:
            print("Incorrect admin password.")
            input("Press Enter to go back to menu..")
            continue
        while True:
            cls()
            print("---== ADMIN OPTIONS ==---")
            print("╔═══════════════════════╗") 
            print("║1. Update Worker Data  ║")
            print("║2. Remove Worker       ║")
            print("║3. Back                ║")
            print("╚═══════════════════════╝")

            choiceThree = input("Enter choice: ")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            if choiceThree == "1":
                updateWorker()

            elif choiceThree == "2":
                removeWorker()

            elif choiceThree == "3":
                break

            else:
                print("Invalid Input. Try Again")
    elif choice == "4":

        print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")
        print("Thank you for using our service. GoodBye")
        print("Exiting system...")
        print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")
        break

    else:
        print("Invalid Input. Try Again")
