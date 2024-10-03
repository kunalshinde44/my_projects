def task():
    tasks=[]
    print("       ****WELCOME TOTASK MANAGEMET SYSTEM****          ")


    total_task=int(input("Enter the no of tasks to you have to add :"))
    for i in range(1,total_task+1):
        task_name=input("Enter task  =")
        tasks.append(task_name)


    print("Todays tasks are",tasks)

    while True:
        operation=int(input("Enter 1-Add \n2-Update \n3-Delete \n4-View \n5-Exit/Stop/n"))
        if operation==1:
            add=input("Enter task that you want to add =")
            tasks.append(add)
            print("Task is Added successfully")



        elif operation==2:
            update_val=input("Enter the task name you want to update =")
            if update_val in tasks:
                up = input("Enter new tas=")
                ind = tasks.index(update_val)
                tasks[ind]=up
                print("Updated Task Successfully")

        elif operation==3:
            del_val = input("Which value you want to Delete =")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del (ind)
                print("Task has been Deleted....")

        elif operation==4:
            print("Total task = ",tasks)

        elif  operation==5: 
            print("Closing the program......")

        else:
            print(" INVALID INPUTE")







task()
