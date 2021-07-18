#Welcome message
print("Welcome to Access The Marks (ATM)")

#defining the main function
def main():
    
#loction of source of data, it is opened in read mode
    F=open("C:\\Users\\Sai Sudhir S\\Documents\\NU ICP\\file2.txt","r")
    
    L=F.readlines()
    
    #Empty dictionary is created
    D={}
    
    #lines are split into separate lists
    for line in L:
        data= line.split()
        
        #roll number has been assigned to the first element of the list
        rollno=data[0]
        
        #empty list is created
        marklist=[]
        
        #marks are added to the list
        for m in data[1:]:
            marklist.append(int(m))
    
        #roll number tagged to marks
        D[rollno]=marklist
    
    #input taken from user for roll number and coverted to upper case
    n=(input("roll number to retrieve: ")).upper()
    
    #Self expanatory stats are printed for output
    numofrecords=len(D[n])
    print(D[n])
    print("Total is",sum(D[n]))
    print("Number of records is",numofrecords)
    print("Average is", sum(D[n])/numofrecords)     
    
    #list is sorted by default it is acending order
    (D[n]).sort()
    print("Marks in ascending order:", D[n])
    
    #list is sorted after reversing the sort function
    (D[n]).sort(reverse=True)
    print("Marks in descending order:", D[n])
    
    #maximum and minimum marks of student are printed for output
    print("max is : ", max(D[n]))
    print("min is : ", min(D[n]))
    
    #if statement is used for determining pass or fail
    if  min(D[n])  >= 34:
        print("Result: PASS")
    else:
        print("Result: FAIL")
    
    #printing section break
    print("-----------------------")
    
    F.close()
    end()

#ending statements program    
def end():
    
    restart=input("Do you want to query again?(Y/N):").lower()
    
    #printing section break
    print("-----------------------")
    if restart == "y":
        main()
    elif restart =="n":
        
        #closing message
        print("Thank you for using ATM")
        exit()        
    else:
        print("Wrong input")
        end()

#start of program    
main()
