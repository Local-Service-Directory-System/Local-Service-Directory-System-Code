
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

    for position in range(1, len(workers)):
        current = workers[position]
        worker = position - 1
        while worker >= 0 and workers[worker]["profession"].lower() > current["profession"].lower():
            workers[worker + 1] = workers[worker]
            worker -= 1
        workers[worker + 1] = current

    print("Workers sorted successfully.")

#BINARY SEARCH FUNCTION------------------------------------------------

def binarySearch(target):

    low = 0
    high = len(workers) - 1

    while low <= high:
        mid = (low + high) // 2
        currentProf = workers[mid]["profession"].lower()

        if currentProf == target.lower():
            
            matches = [mid]
            # Check for multiple matches
            left = mid - 1
            while left >= 0 and workers[left]["profession"].lower() == target.lower():
                matches.append(left)
                left -= 1
            
            right = mid + 1
            while right < len(workers) and workers[right]["profession"].lower() == target.lower():
                matches.append(right)
                right += 1

            matches.sort() 
            return matches # Return list of of matching workers
        
        elif currentProf < target.lower():
            low = mid + 1

        else:
            high = mid - 1

    return -1  # Not found
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

    for worker in workers:
        if worker["firstName"].lower() == firstName.lower() and worker["lastName"].lower() == lastName.lower() and worker["contact"] == contact:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Worker already exists. Please update worker details instead.")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            input("Press Enter to continue...")
            return


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
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Workers Found!")
        print("Total workers found:", len(result))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        for num, worker in enumerate(result, start=1):
            worker = workers[worker]
            print(f"Worker #{num}")
            print("══════════════════════════════")
            print("Name:", worker["firstName"], worker["lastName"])
            print("Barangay:", worker["barangay"])
            print("Zone:", worker["zone"])
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Profession:", worker["profession"])
            print("Hourly Rate:", worker["hourRate"])
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Contact Number:", worker["contact"])
            print("Social Media Account:", worker["socialMedia"])
            print("══════════════════════════════")  
            print()
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
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("No available workers at the moment.")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    input("Press Enter to continue...")

#UPDATE WORKER----------------------------------------------------------

def updateWorker():
    target = input("Enter first name to update: ")

    matchedWorkers = []
    for worker in workers:
        if worker["firstName"].lower() == target.lower():
            matchedWorkers.append(worker)

    if len(matchedWorkers) == 0:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Worker not found.")  
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        input("Press Enter to continue...") 
        return
    
    print("--==MATCHEDWORKER==--:")
    for num, worker in enumerate(matchedWorkers, start=1):
        print()
        print(f"Worker #{num}")
        print("══════════════════════════════")
        print("Name:", worker["firstName"], worker["lastName"]) 
        print("Barangay:", worker["barangay"])
        print("Zone:", worker["zone"])
        print("Profession:", worker["profession"])
        print("Hourly Rate:", worker["hourRate"])
        print("Contact Number:", worker["contact"])
        print("Social Media Account:", worker["socialMedia"])

    while True:
        try: 
            choice = int(input("Enter 1 to continue update, 0 to go back: "))
            if choice == 0:
                return
            elif 1 <= choice <= len(matchedWorkers):
                worker = matchedWorkers[choice - 1]
            else:
                print("Invalid number. Try Again")
                continue
        except ValueError:
            print("Invalid input. Try Again")

                
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\n--=Enter new information=--")
        print("Leave BLANK if NO CHANGES")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        newFirstName = input(f"New first name (current: {worker['firstName']}): ")
        if newFirstName.strip() != "":
            worker["firstName"] = newFirstName.title()

        newLastName = input(f"New last name (current: {worker['lastName']}): ")
        if newLastName.strip() != "":
            worker["lastName"] = newLastName.title()

        newBarangay = input(f"New barangay (current: {worker['barangay']}): ")
        if newBarangay.strip() != "":
            worker["barangay"] = newBarangay.title()

        newZone = input(f"New zone (current: {worker['zone']}): ")
        if newZone.strip() != "":
            worker["zone"] = newZone.title()

        newProfession = input(f"New profession (current: {worker['profession']}): ")
        if newProfession.strip() != "":
            worker["profession"] = newProfession.title()
                
#---------------------------HOUR RATE-----------------------
        while True:
            newHourRate = input(f"New hourly rate (current: {worker['hourRate']}): ")

            if newHourRate == "":
                break

            try:
                worker["hourRate"] = int(newHourRate)
                break
            except ValueError:
                print("Invalid input. Try Again")

#------------------------CONTACT NUMBER----------------------
        while True:
            contact = input(f"Enter contact number (current: {worker['contact']}): ")
            if contact.strip() == "":
                break
            elif contact[:2] == '09' and len(contact) == 11 and contact.isdigit():
                worker["contact"] = int(contact)
                break
            else:
                print("Invalid input. Try Again")

#-----------------------SOCIAL MEDIA ACCOUNT----------------------
        while True:
            newSocialMedia = input(f"Social Media Account (current: {worker['socialMedia']}): ")

            if newSocialMedia.strip() == "":
                break
                
            elif newSocialMedia.strip().isdigit():
                print("Invalid input. Try Again")
                continue

            else:
                worker["socialMedia"] = newSocialMedia.title()
                break   
    
    
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Worker updated successfully.")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        input("Press Enter to continue...")

        saveToFile()
        return
#REMOVE WORKER-------------------------------------------------
def removeWorker():
    target = input("Enter first name to remove: ") 
    
    matchedWorkers = []
    for worker in workers:
        if worker["firstName"].lower() == target.lower():
            matchedWorkers.append(worker)

    if len(matchedWorkers) == 0:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Worker not found.")  
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        input("Press Enter to continue...") 
        return
    
    cls()
    print("\n--==MATCHEDWORKER==--:")
    for num, worker in enumerate(matchedWorkers, start=1):
        print()
        print(f"Worker #{num}")
        print("══════════════════════════════")
        print("Name:", worker["firstName"], worker["lastName"]) 
        print("Barangay:", worker["barangay"])
        print("Zone:", worker["zone"])
        print("Profession:", worker["profession"])
        print("Hourly Rate:", worker["hourRate"])
        print("Contact Number:", worker["contact"])
        print("Social Media Account:", worker["socialMedia"])

    while True:
        try: 
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            choice = int(input("Enter worker number to remove (0 to go back): "))
            if choice == 0:
                return
            elif 1 <= choice <= len(matchedWorkers):
                worker = matchedWorkers[choice - 1]
                confirm = input(f"Are you sure you want to remove {worker['firstName']} {worker['lastName']}? (y/n): ")
                if confirm.lower() == "y":
                    workers.remove(worker)
                    prin()
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    print("Worker removed successfully.")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    input("Press Enter to continue...")
                    saveToFile()
                    return
                else:
                    print("Worker removal cancelled.")
                    input("Press Enter to continue...")
                    return
            else:
                print("Invalid number. Try Again")
                continue
        except ValueError:
            print("Invalid input. Try Again")


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
        loadFromFile()
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
