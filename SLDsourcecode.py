try:
    with open("SLD.txt", "x") as file:
        print("File Sucesfully Created")
except FileExistsError:
    print("File Exist Already")

def addProvider():
    with open("SLD.txt", "w") as file:
        providers = input("")



    