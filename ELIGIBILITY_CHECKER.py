# creating the algorithm
print("Enter only 'Y' for yes and 'N' for no (remember to write the keywords in capital)")
MC = input("Do you have a medical certificate: ")
if (MC == "Y"):
    print("You are eligible for writing the exam.")
elif (MC == "N"):
    Att = int(input("Enter your attendance in percentage: "))
    if (Att > 75):
        print("You are eligible for writing the exam.")
    else:
        print("You are not eligible for writing the exam.")
else:
    print("Please use the proper keywords for Yes or No")