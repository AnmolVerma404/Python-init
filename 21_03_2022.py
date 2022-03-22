# 1st While loop
i = 1
while i<10:
    # print(i,"Welcome to the University ")
    # print(i," ")
    i+=1
    if(i==6):
        break
    
# 2nd Continue Keyword
i = 1
while i<10:
    i+=1
    if(i==6):
        continue
    # print(i," ")
# 3rd 1-10 using while loop and use a edge statement so that you can run a block of code once the condition is no longer true using else statement
i = 1
while(i<=10):
    if(i==1):
        print("Start",i)
    else:
        print(i)
    i+=1