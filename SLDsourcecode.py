try:
    with open("SLD.txt", "x") as file:
        print("File Sucesfully Created")
except FileExistsError:
    print("File Exist Already")

personInfo = []

def personalInfo():
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
            except:
                print("Please enter a valid contact number.")
                continue
        while True:
            try: 
                dateBirth = input("Enter Birthday (mm/dd/yyyy): ")
            except:
                print("Please enter a valid birthdate.")
                continue

        gender = input("Enter gender (Male/Female): ")

#clear screen
#------------------------------------------------------------
        print("\nLocation and Professional Info")
        city = input("Enter City: ")

        province = input("Enter province: ")
        while True:
            try: 
                zipCode = int(input("Enter Zip Code (####): "))
            except:
                print("Please enter a valid zip code.")
                continue

        profTitle = input("Enter Professional Title (ex. Electrician): ")
        while True:
            try: 
                hourRate = int(input("Enter your hourly rate: "))
            except:
                print("Enter valid hourly rate.")
#clear screen
#----------------------------------------------------------------
        print("\n--=Work Experience (in a Company)=--")
        print("Enter N/A if not applicable\n")

        jobTitle = input("Enter job title (company position or): ")
        companyName = input("Enter company name: ")
        while True:
            try: 
                dateStart = int(input("Enter date started (Year): "))
            except:
                print("Please enter a valid year")
                continue
        while True:
            try:
                dateEnded = int(input("Enter date ended (Year): "))
            except:
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
            "jobTitle": jobTitle,
            "companyName": companyName,
            "dateStart": dateStart,   
            "dateEnded": dateEnded
        }
        try:
            personInfo.append(personInfos)

            with open("SLD.txt", "a") as file:
                file.write(str(personInfos) + "\n")

            print("Information saved succesfully")
        except:
            print("An error occured.")
            

        return

personalInfo()