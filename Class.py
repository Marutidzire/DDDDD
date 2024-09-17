# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
classnum=int(input("How many classes are you taking"))
array=[]
for i in range(classnum):
    j=input("what is your letter grade")
    if j.isdigit():
        print("Please put a letter grade")
    else:
        if j=="A":
            array.append(4)
        elif j=="B":
            array.append(3)
        elif j=="C":
            array.append(2)
        elif j=="D":
            array.append(1)
        elif j=="F":
            appay.append(0)
        else:
            print("Enter a valid letter")
sum=0
            
for i in range(len(array)):
    sum=sum+array[i]
    print("Sum")
    
