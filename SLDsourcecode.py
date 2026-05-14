try:
    with open("SLD.txt", "x") as file:
        print("File Sucesfully Created")
except FileExistsError:
    print("File Exist Already")

personInfo = []

def personalInfo():
    while True:
        print("--=Personal Information=--")
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
            contact = int(input("Enter contact number: "))
        except:
            print("Numbers Only. Please try AGain!")
            continue
        dateBirth = int(input("Enter Birthday (mm/dd/yyyy): "))
        try:
            gender = input("Enter gender (Male/Female): ")
        except:
            print("Male of Female inputs only. Please Try Again!")
            continue
#---------------------------------------------------------------------------
        print("\n--=Location and Professional Info=--")
        try:
            city = input("Enter City: ")
        except:
            print("Letters only. Please Try Again")
            continue
        try:
            province = input("Enter province: ")
        except:
            





    personInfos = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "service": service,
        "contact": contact,
        "dateBirth": dateBirth,
        "gender": gender
    }

    personInfo.append(personInfos)

    with open("SLD.txt", "a") as file:
        file.write(str(provider) + "\n")

    print("Information saved succesfully")


