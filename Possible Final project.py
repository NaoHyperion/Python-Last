def menu():
    print("Welcome to my password generator & checker")
    inputone = (input("Where will you go first? 1 = Generator and 2 = Checker "))

    if inputone == "1":
        generator()
    elif inputone == "2":
        checker()
    else:
        print("That is not one of the options.")

def generator():
    import random
    import string

    size = int(input("How many characters would you like your password to be (Max 50): "))
    charac = string.printable
    finalpass = "".join(random.choice(charac) for i in range(size))
    if size >50:
        print("That is too many characters, please give a number between 1 and 50!")
        
    print(f"Your new password is {finalpass}")

    done = input("would you like to try again? y/n: ")

    if done == "y":
        generator()
    elif done == "n":
        whatnowcheck2()
        

    


def checker():
    import string
    print("Welcome to the password checker!")
    specialsym = string.punctuation
    passinput = (input("Firstly, Enter what your current password is!: "))
    gotsym = False
    truth_val = 0
    totalchar = 0

    print(" Password Checklist!")
    print("______________________")


    # uppercases
    for letter in passinput:
        if letter.isupper():
            letter = True
            print("Contains uppercase letter(s)!")
            truth_val =+ 1
            break
        elif letter.isupper():
            letter = False
            print("This password doesn't contain any uppercase letter(s)!")
    #lowercase
    for letter in passinput:
        if letter.islower():
            letter = True
            truth_val =+ 1
            print("Contains lowercasee letter(s)!")
            break
        elif letter.islower():
            letter = False
            print("This password doesn't contain any lowercase letter(s)!")

    for numb in passinput:
        if numb.isdigit():
            numb = True
            truth_val =+ 1
            print("This password has number(s)!")
            break
        
        elif not any(num.isdigit() for num in passinput):
            print(" There must be at least one number in your password!")
            break
    #symbols
    for char in passinput:
        if char in specialsym:
            gotsym = True
            truth_val =+ 1
            break
    if gotsym:
        print("This password has special symbol(s)")
    else:
        print("There are no special symbol(s)")

    # lenth of password
    for char in passinput:
        totalchar += 1
        if totalchar >= 12:
            print(" This password meets or surpasses the length requirement")
            truth_val =+ 1
            break
        elif totalchar <12:
            print("This should have more than 12 characters")
            break
            # Is the password considered strong
        if truth_val <0:
            print("This password is not strong at all")
        elif truth_val == 1 or truth_val == 2:
            print("This password is weak")
        elif truth_val == 3 or truth_val == 4:
            print("This password is of medium strength")
        else:
            print("This is a strong password!")
    
    whatnowcheck1()
        
def whatnowcheck1():
    lastselect = input(" Would you like to try agian = 1 return to menu = 2 or go to generator = 3  ")
    if lastselect == "1":
        checker()
        
    elif lastselect == "2":
        menu()
    elif lastselect == "3":
        generator()
    else:
        print("That is not an option")

def whatnowcheck2():
    lastselect = input(" Would you like to return to menu = 1 or go to checker = 2  ")
    if lastselect == "1":
        generator()
        
    elif lastselect == "2":
        menu()
    else:
        print("That is not an option")











    #if passinput == true:
        #print("That's a safe password!") 
    #elif passinput == false:
        #print("That password is not safe!")


menu()