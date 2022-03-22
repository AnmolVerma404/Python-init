# 1st
age = int(input("Enter age: "))
if age >= 18:
    print("You can cast a vote.")
else:
    print("You are not eligible.")
# 2nd
# 60%attend,60%marksMidTerm,60%FinalExamM2ark
attendence = int(input("Enter attendence(%): "))
marksMidTerm = int(input("Enter Mid Term marks(%): "))
marksFinal = int(input("Enter Final Term marks(%): "))
if attendence > 60:
    if marksMidTerm > 60:
        if marksFinal > 60:
            print("Passed")
        else:
            print("Failed")
    else:
        print("Failed")
else:
    print("Failed")
