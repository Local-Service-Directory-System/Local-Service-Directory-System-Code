try:
    with open("SLD.txt", "x") as file:
        print("File Sucesfully Created")
except FileExistsError:
    print("File Exist Already")


personInfo = []

def postApplication():
        print("\nPersonal Information")
        firstName = input("Enter First Name: ")
        
        lastName = input("Enter Last Name: ")
        
        while True:
            email = input("Enter email: ")
            if "@" in email and "." in email:
                break
            else:
                print("Invalid email. Please try again.")
                continue

        while True:
            try:
                contact = int(input("Enter contact number: "))
                break
            except ValueError:
                print("Please enter a valid contact number.")
                continue
        while True:
            dateBirth = input("Enter Birthday (mm/dd/yyyy): ")

            if "/" in dateBirth:
                break
            else:
                print("Please enter a valid birthdate.")

        gender = input("Enter gender (Male/Female): ")

#clear screen
#------------------------------------------------------------
        print("\nLocation and Professional Info")
        city = input("Enter City: ")

        province = input("Enter province: ")
        while True:
            try: 
                zipCode = int(input("Enter Zip Code (####): "))
                break
            except ValueError:
                print("Please enter a valid zip code.")
                continue

        profTitle = input("Enter Professional Title (ex. Electrician): ")

        while True:
            try: 
                hourRate = int(input("Enter your hourly rate: "))
                break
            except ValueError:
                print("Enter valid hourly rate.")

        employType = input("Enter Work Type (Full Time/Part Time/Freelance/Contract): ")
#clear screen
#----------------------------------------------------------------
        print("\n--=Work Experience (in a Company)=--")
        print("Enter N/A if not applicable\n")

        jobTitle = input("Enter job title (company position or): ")
        companyName = input("Enter company name: ")
        while True:
            try: 
                dateStart = int(input("Enter date started (Year): "))
                break
            except ValueError:
                print("Please enter a valid year")
                continue
        while True:
            try:
                dateEnded = int(input("Enter date ended (Year): "))
                break
            except ValueError:
                print("Please enter a valid date.")

#clear screen

        personInfos = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "contact": contact,
            "dateBirth": dateBirth,
            "gender": gender,
            "city": city,
            "province": province,
            "zipCode": zipCode,
            "profTitle": profTitle,
            "hourRate": hourRate,
            "employType": employType,
            "jobTitle": jobTitle,
            "companyName": companyName,
            "dateStart": dateStart,   
            "dateEnded": dateEnded
        }
        try:
            with open("SLD_FILE", "a") as file:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writerow(record)
                print("\n  ✓ Application saved successfully!")
        except Exception as e:
            print(f"\nError saving application: {e}")

        return

def findWorkers():
    print("--=Search Workers=--")

    searchJob = input("Enter Job Title: ").lower()
    searchType = input("Enter Type of Worker (Full Time/Part Time/Freelance/Contract): ")
    searchLoc = input("Enter Location: ").lower()

    while True:
        try:
            minExperience = int(input("Enter Minimum Experience: "))
            break
        except ValueError:
            print("Invalid Input. Please Try Again")
            continue

    while True:
        try:
            minRating = int(input("Enter Minimum Rating: "))
            break
        except ValueError:
            print("Invalid Input. Please Try Again.")
            continue

    found = False

    with open("SLD.txt", "r") as file:
        for worker in file:
            data = worker.strip().split(",")

            firstName = data[0]
            lastName = data[1]
            profTitle = data[2]
            city = data[3]
            province = data[4]
            experience = int(data[5])
            rating = float(data[6])
            hourRate = data[7]
            employType = data[8]

            if (
                searchJob in profTitle.lower()
                and searchType in employType.lower()
                and searchLoc in city.lower()
                and experience >= minExperience
                and rating >= minRating
            ):

                print("\n===== WORKER FOUND =====")
                print("Name:", firstName, lastName)
                print("Profession:", profTitle)
                print("Employment Type:", employmentType)
                print("Location:", city)
                print("Experience:", experience, "years")
                print("Rating:", rating)
                print("Hourly Rate:", hourRate)

                found = True

    if not found:
        print("\nNo matching workers found.")



    
