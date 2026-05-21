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
        currentName = workers[mid]["firstName"].lower()

        if currentName == target.lower():
            return mid

        elif currentName < target.lower():
            low = mid + 1

        else:
            high = mid - 1

    return -1
#ADD WORKER--------------------------------------------------------

def addWorker():

    print("\n=== Post Application ===")

    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    barangay = input("Enter city: ")
    zone = input("Enter province: ")
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
            if str(contact)[0] == '0' and str(contact)[1] == '9' and len(str(contact)) == 11:
                break
        except ValueError:
            print("Invalid input. Try Again")

    while True:
        socialMedia = input("Social Media Account (ex. Facebook Juan Cruz): ")
        if socialMedia.isdigit:
            print("Invalid input. Try Again")
            continue
        else:
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

    print("Worker added successfully.")

#DISPLAY ALL WORKERS-------------------------------------------------

def displayWorkers():

    if len(workers) == 0:
        print("No workers found.")
        return

    print("\n====SERVICE PROVIDERS====")

    for i, worker in enumerate(workers):

        print(f"\nWorker #{i+1}")
        print("Name:", worker["firstName"], worker["lastName"])
        print("Barangay:", worker["barangay"])
        print("Zone:", worker["zone"])
        print("Profession:", worker["profession"])
        print("Hourly Rate:", worker["hourRate"])
        print("Contact Number:", worker["contact"])
        print("Social Media Account:", worker["socialMedia"])

#SEARCH WORKER------------------------------------------------------

def searchWorker():
    insertionSort()
    target = input("Enter first name to search: ")
    result = binarySearch(target)
    if result != -1:
        worker = workers[result]
        print("\nWorker Found")
        print("Name:", worker["firstName"], worker["lastName"])
        print("Barangay:", worker["barangay"])
        print("Zone:", worker["zone"])
        print("Profession:", worker["profession"])
        print("Hourly Rate:", worker["hourRate"])
        print("Contact Number:", worker["contact"])
        print("Social Media Account:", worker["socialMedia"])
    else:
        print("Worker not found.")


#UPDATE WORKER----------------------------------------------------------

def updateWorker():
    target = input("Enter first name to update: ")
    for worker in workers:
        if worker["firstName"].lower() == target.lower():
            print("\n--=Enter new information=--")
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
            return
        
    print("Worker not found.")


#REMOVE WORKER-------------------------------------------------
def removeWorker():
    target = input("Enter first name to remove: ")
    for worker in workers:
        if worker["firstName"].lower() == target.lower():
            workers.remove(worker)
            print("Worker removed successfully.")
            return

    print("Worker not found.")

#MENU---------------------------------------------------------------------

while True:
    print("╔═════════════════════════════════╗")
    print("║\n=== LOCAL SERVICE DIRECTORY ===║")
    print("║═════════════════════════════════║")
    print("║1. Post Application              ║")
    print("║2. Hire Workers                  ║")
    print("║3. Admin Options                 ║")
    print("║4. Exit                          ║")
    print("╚═════════════════════════════════╝")

    choice = input("Enter choice: ")

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
