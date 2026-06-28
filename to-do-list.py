#To-do-list

print("===========TO-DO-TASK==========")
tasks=[]
while True:
    
    print("1.VIEW tasks")
    print("2.ADD tasks")
    print("3.REMOVE tasks")
    print("4.Exit")
    choice=int(input("Enter your choice"))

    if choice==1:

        if len(tasks)==0:
            print("There is no task avalible")

        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
    elif choice==2:
        value=input("Enter tasks")
        tasks.append(value)
        print("tasks successfully added")
    
    elif choice==3:
        if len(tasks)==0:
            print("There is no task avalible")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])

            number=int(input("Enter number"))
            if number>=1 and number<=len(tasks):
                removed_ele=tasks.pop(number-1)
                print(f"removed task '{ removed_ele}' ")
            else:
                print("invalid number")
    elif choice==4:
        print("thank you for using to-do-list app") 
        break
    else:
        print("invalid choice")     


