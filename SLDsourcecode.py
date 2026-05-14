try:
    with open("SLD.txt", "x") as file:
        print("File Sucesfully Created")
except FileExistsError:
    print("File Exist Already")

personInfo = []

def personalInfo():
    while True:
        print("Personal Information")
        try:
            firstName = input("Enter First Name: ")
        except:
            print("Letters Only. Please Try Again!")
            continue
        try:
            lastName = input("Enter Last Name: ")
        except:
            print("Letters Only. Please Try Again!")
            continue
        email = input("Enter email: ")
        try:
            contact = input("Enter contact number: ")
        except:
            print("Numbers Only. Please try AGain!")
            continue
        dateBirth = input("Enter Birthday (mm/dd/yyyy): ")
        try:
            gender = input("Enter gender (Male/Female): ")
        except:
            print("Male of Female inputs only. Please Try Again!")
            continue




    personInfos = {
        "firstName" = firstName,
        "lastName" = lastName,
        "email" = email,
        "service" = service,
        "contact" = contact,
        "dateBirth" = dateBirth,
        "gender" = gender
    }

    personInfo.append(personInfos)

    with open("SLD.txt", "a") as file:
        file.write(str(provider) + "\n")

    print("Provi")
