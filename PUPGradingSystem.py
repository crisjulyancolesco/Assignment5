print("To see your equivalent mark, kindly input your Grade Percentage.")

Grade = float(input("Grade Percentage: "))

if Grade >=97 and Grade <= 100:
    print("Grade Mark: 1.0")
    print("Description: Excellent")
    print("Congratulations! Your hard work pays off!")
else:
    if Grade >= 94 and Grade <= 96:
        print("Grade Mark: 1.25")
        print("Description: Excellent")
        print("Congratulations! Your hard work pays off!")
    else:
        if Grade >= 91 and Grade <= 93:
            print("Grade Mark: 1.5")
            print("Description: Very Good")
            print("Good job! Keep it up!")
        else:
            if Grade >= 88 and Grade <= 90:
                print("Grade Mark: 1.75")
                print("Description: Very Good")
                print("Good job! Keep it up!")
            else:
                if Grade >= 85 and Grade <= 87:
                    print("Grade Mark: 2.0")
                    print("Description: Good")
                    print("Well done! You can do it!")
                else:
                    if Grade >= 82 and Grade <= 84:
                        print("Grade Mark: 2.25")
                        print("Description: Good")
                        print("Well done! You can do it!")
                    else:
                        if Grade >= 79 and Grade <= 81:
                            print("Grade Mark: 2.5")
                            print("Description: Satisfactory")
                            print("Nice! Give your fullest next time!")
                        else:
                            if Grade >= 76 and Grade <= 78:
                                print("Grade Mark: 2.75")
                                print("Description: Satisfactory")
                                print("Nice! Give your fullest next time!")
                            else:
                                if Grade == 75:
                                    print("Grade Mark: 3.0")
                                    print("Description: Passing")
                                    print("Passing grades is still passed! Good luck next time!")
                                else:
                                    if Grade >= 65 and Grade <= 74:
                                        print("Grade Mark: 5.0")
                                        print("Description: Failure")
                                        print("There's always another chance. Make sure to make use of it to the fullest! Good luck! ")
                                    else:
                                        if Grade ==0:
                                            print("Grade Mark: Inc.")
                                            print("Description: Incomplete")
                                            print("Nice Try! Work Harder next time! Good luck!")

                                            