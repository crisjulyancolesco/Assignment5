print("To see your equivalent mark, kindly input your Grade Percentage.")

Grade = float(input("Grade Percentage: "))
Grades = round(Grade)

if Grades >=97 and Grades <= 100:
    print("Grade Mark: 1.0")
    print("Description: Excellent")
    print("Congratulations! Your hard work pays off!")
else:
    if Grades >= 94 and Grades <= 96:
        print("Grade Mark: 1.25")
        print("Description: Excellent")
        print("Congratulations! Your hard work pays off!")
    else:
        if Grades >= 91 and Grades <= 93:
            print("Grade Mark: 1.5")
            print("Description: Very Good")
            print("Good job! Keep it up!")
        else:
            if Grades >= 88 and Grades <= 90:
                print("Grade Mark: 1.75")
                print("Description: Very Good")
                print("Good job! Keep it up!")
            else:
                if Grades >= 85 and Grades <= 87:
                    print("Grade Mark: 2.0")
                    print("Description: Good")
                    print("Well done! You can do it!")
                else:
                    if Grades >= 82 and Grades <= 84:
                        print("Grade Mark: 2.25")
                        print("Description: Good")
                        print("Well done! You can do it!")
                    else:
                        if Grades >= 79 and Grades <= 81:
                            print("Grade Mark: 2.5")
                            print("Description: Satisfactory")
                            print("Nice! Give your fullest next time!")
                        else:
                            if Grades >= 76 and Grades <= 78:
                                print("Grade Mark: 2.75")
                                print("Description: Satisfactory")
                                print("Nice! Give your fullest next time!")
                            else:
                                if Grades == 75:
                                    print("Grade Mark: 3.0")
                                    print("Description: Passing")
                                    print("Passing grades is still passed! Good luck next time!")
                                else:
                                    if Grades >= 65 and Grades <= 74:
                                        print("Grade Mark: 5.0")
                                        print("Description: Failure")
                                        print("There's always another chance. Make sure to make use of it to the fullest! Good luck! ")
                                    else:
                                        if Grades ==0:
                                            print("Grade Mark: Inc.")
                                            print("Description: Incomplete")
                                            print("Nice Try! Work Harder next time! Good luck!")