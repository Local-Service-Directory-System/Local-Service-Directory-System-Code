workers = []

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

    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    barangay = input("Enter barangay: ")
    zone = input("Enter zone: ")
    profession = input("Enter profession: ")
    

    while True:
        try:
            hourRate = int(input("Enter hourly rate: "))
            break
        except ValueError:
            print("Invalid input. Try Again")

    while True:
        try:
            contact = int(input("Enter contact number: "))
            break
        except ValueError:
            print("Invalid input. Try Again")

    socialMedia = input("Social Media Account (ex. Facebook Juan Cruz): ")

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

#DISPLAY ALL WORKERS-------------------------------------------------

def displayWorkers():

    if len(workers) == 0:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("No workers found.")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        return

    print("\n====SERVICE PROVIDERS====")

    for i, worker in enumerate(workers):
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"\nWorker #{i+1}")
        print("Name:", worker["firstName"], worker["lastName"])
        print("Barangay:", worker["barangay"])
        print("Zone:", worker["zone"])
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Profession:", worker["profession"])
        print("Hourly Rate:", worker["hourRate"])
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Contact Number:", worker["contact"])
        print("Social Media Account:", worker["socialMedia"])

#SEARCH WORKER------------------------------------------------------

def searchWorker():
    insertionSort()
    target = input("Enter expertise/profession to search: ")
    result = binarySearch(target)
    if result != -1:
        worker = workers[result]
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\nWorker Found")
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
    else:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Worker not found.")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

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
                try:
                    contact = int(input("Enter new contact number: "))
                    break
                except ValueError:
                    print("Invalid input. Try Again")

            socialMedia = input("New Social Media Account (ex. Facebook Juan Cruz): ")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Worker updated successfully.")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            return
        
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Worker not found.")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")



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
#MENU---------------------------------------------------------------------

while True:
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
        addWorker()

    elif choice == "2": #Hire workers
        while True:
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
        while True:
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
