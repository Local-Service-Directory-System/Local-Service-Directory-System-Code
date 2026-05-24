workers = []

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
            if str(contact)[0] == '0' and str(contact)[1] == '9' and len(str(contact)) == 11:
                break
        except ValueError:
            print("Invalid input. Try Again")

    while True:
        socialMedia = input("Social Media Account (ex. Facebook Juan Cruz): ")
        if socialMedia.isdigit():
            print("Invalid input. Try Again")
            continue
        else:
            break

    for worker in workers:
        if worker["firstName"].lower() == firstName.lower() and worker["lastName"].lower() == lastName.lower() and worker["contact"] == contact:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Worker already exists.")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
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
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\nWorker Found")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        for worker in result:
            worker = workers[worker]
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
            print("Leave BLANK if NO CHANGES")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            newFirstName = input("New first name: ")
            if newFirstName.strip() != "":
                worker["firstName"] = newFirstName

            newLastName = input("New last name: ")
            if newLastName.strip() != "":
                worker["lastName"] = newLastName

            newBarangay = input("New barangay: ")
            if newBarangay.strip() != "":
                worker["barangay"] = newBarangay

            newZone = input("New zone: ")
            if newZone.strip() != "":
                worker["zone"] = newZone

            newProfession = input("New profession: ")
            if newProfession.strip() != "":
                worker["profession"] = newProfession
                
#---------------------------HOUR RATE-----------------------
            while True:
                newHourRate = input("New hourly rate: ")

                if newHourRate == "":
                    break

                try:
                    worker["hourRate"] = int(newHourRate)
                    break
                except ValueError:
                    print("Invalid input. Try Again")

#------------------------CONTACT NUMBER----------------------
            while True:
                newContact = input("Enter contact number: ")

                if newContact.strip() == "":
                    break

                if str(newContact)[0] == '0' and str(newContact)[1] == '9' and len(str(newContact)) == 11:
                    worker["contact"] = int(newContact)
                    break
                else:
                    print("Invalid input. Try Again")
                
#-----------------------SOCIAL MEDIA ACCOUNT----------------------
            while True:
                newSocialMedia = input("Social Media Account (ex. Facebook Juan Cruz): ")

                if newSocialMedia.strip() != "":
                    break
                
                if newSocialMedia.isdigit():
                    print("Invalid input. Try Again")
                    continue

                else:
                    worker["socialMedia"] = newSocialMedia
                    break   
    
    
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
            return
            
            
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
