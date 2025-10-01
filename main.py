def get_name():
    name = input("What's your name? ")
    length = len(name)

    if length >= 3:
        print("Wow, what a short name!")
    else:
        print("Wow, that's a nice name!")

    print("Hi, " + name)

def get_age():
    age = int(input("How old are you? "))

    if age <= 10:
        print("Wow! You're still very young!")
    else:
        if age <= 24:
            print("Nice! You must be still in school or college!")
        else:
            if age <= 40:
                print("Cool! You are average age!")
            else:
                print("You are pretty old.")

def assist():
    print("Okay, how can I assist you? Would you like to:\n1. Make me tell you a joke\n2. Give you a riddle\n3. Exit")
    choice = int(input("Pick an option (1-3): "))

    if choice == 1:
        print("Why did the computer get cold?")
        print("Because it left its Windows open!!")
    if choice == 2:
        print("I have no life but I can die. What am I?\nA battery.")
    if choice == 3:
        print("Goodbye. Nice chatting with you.")

get_name()
get_age()
assist()
