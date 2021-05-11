
work_list = []
def my_list():
    
    n = int(input("Please input index number : "))  
    m = int(input("Enter List Number : "))
    work_list.insert(n, m)
    print(work_list)
    m = int(input("Please enter the number that you want to remove : "))
    work_list.remove(m)
    print("Remove list" , work_list)
    a = int(input("Please enter the number that you want to Add in the last. : "))
    work_list.append(a)
    a = int(input("Please enter the number that you want to Add in the last. : "))
    work_list.append(a)
    a = int(input("Please enter the number that you want to Add in the last. : "))
    work_list.append(a)
    a = int(input("Please enter the number that you want to Add in the last. : "))
    work_list.append(a)
    print("append list" , work_list)
    work_list.pop()
    print("Pop list" , work_list)
    work_list.reverse()
    print("Reverse list" , work_list)

my_list()    

