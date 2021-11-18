print("If u want to know what stage are you going through now.")
print("Put your age and I'll tell you.")

Age = int(input("What is your age? "))

if Age >=0 and Age <= 12:
    print("Life Stage: Kid")
    print("Hey Kid! Enjoy being a Kid, it's worth it.")
else:
    if Age >=13 and Age <= 17:
        print("Life Stage: Teen")
        print("This is where the struggles begins, Goodluck and stay positive always!")
    else:
        if Age ==18:
            print("Life Stage: Debut")
            print("You're one way to go to become an Adult, Be ready!")
        else:
            if Age >=19:
                print("Life Stage: Adult")
                print("How's your Adult life? Always be happy and live your life to the fullest!")