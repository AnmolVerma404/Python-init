# 1st
for x in "vellore":
    pass
    # print(x)
# 2nd
sports = ["badminton","cricket","basketball","footbal"]
for str in sports:
    pass
    # print(str) # pass acts as a placeholder, so there code can be placed in future
# 3rd Write down a for loop to exit when the value of string is baskeball
for str in sports:
    if(str=="basketball"):
        break
    # print(str)
# 4th
for str in sports:
    if(str == "cricket"):
        continue
    # print(str)
# 5th
for x in range (2,9):
    pass
    # print(x)
# 6th
for x in range(1,25,3):
    pass
    # print(x)
# 7th Print the numbers ranging from 0 to 10 and also pring a message when loop has ended
for i in range(1,11):
    print(i)
    if(i==10):
        print("Your loop has been ended")