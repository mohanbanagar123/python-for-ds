class listmanager:
    def __init__(self):
        self.elements=[]

    def append(self,x):
        self.elements.append(x)

    def removel(self,num):
        self.elements.remove(num)

    def display(self):
        print("the element are:",self.elements)

list1=listmanager()
while(1):
    print('Menu')
    print("1.Append\n2.Delete\n3.display\n4.exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        x=input("enter the value to be inserted:").split()
        for i in x:
            list1.append(int(i))

    elif choice==2:
        num=int(input("enter the value to be deleted:"))
        list1.removel(num)

    elif choice==3:
        list1.display()
    else:
        break
