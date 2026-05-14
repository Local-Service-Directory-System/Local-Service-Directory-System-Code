

def findWorker():
    with open("SLD.txt", "r") as file:
        worker = input("")
        for line in file:
            if worker in line:
                print(line)
    worker = input("Search(by job title or location): ")
    if worker in line:
        print(line)
    else:
        print(" No avvaialble worker in the moment.")