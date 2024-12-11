#Q47
def readInteger():
    while True:
        try:
            integer = int(input("Please enter integer: "))
        except ValueError:
            print("Sorry, I didn't get it .")
            continue
        else:
            break

def readInteger():
    while True:
        try:
            integer = int(input("Please enter your age: "))
            return integer
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue