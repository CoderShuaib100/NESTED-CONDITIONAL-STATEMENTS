# creating the algorithm
print("Enter '1' for bike and '2' for car '3' for cycle nothing else should be entered. \n 1 = Bike \n 2 = Car \n 3 = Cycle")
choice = int(input("Enter your choice: "))
if (choice == 1):
    print("Select any one \n Enter '1' for HONDA and '2' for BMW nothing else should be entered. \n 1 = HONDA \n 2 = BMW")
    bike = int(input("Enter your choice: "))
    if (bike == 1):
        print("You have selected HONDA")
    elif (bike == 2):
        print("You have selected BMW")
    else:
        print("Enter the proper keywords '1,2 or 3'")
elif (choice == 2):
    print("Select any one \n Enter '1' for TATA and '2' for ROLLS ROYCE nothing else should be entered. \n 1 = TATA \n 2 = ROLLS ROYCE")
    car = int(input("Enter your choice: "))
    if (car == 1):
        print("You have selected TATA")
    elif (car == 2):
        print("You have selected ROLLS ROYCE")
    else:
        print("Enter the proper keywords '1,2 or 3'")
elif (choice == 3):
    print("Select any one \n Enter '1' for HERCULES and '2' for MONTRA nothing else should be entered. \n 1 = HERCULES \n 2 = MONTRA")
    cycle = int(input("Enter your choice: "))
    if (cycle == 1):
        print("You have selected HERCULES")
    elif (cycle == 2):
        print("You have selected MONTRA")
    else:
        print("Enter the proper keywords '1,2 or 3'")
else:
        print("Enter the proper keywords '1,2 or 3'")
