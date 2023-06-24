def push_element():
    if len(stc) == n:
        print("Stack is Full!")
    else:
        element = input("Enter Element")
        stc.append(element)
        print(stc)
        
def pop_element():
    if not stc:
        print("Stack is empty")
    else:
        e = stc.pop()
        print(e,"removed")
        print(stc)
        
stc = []
n = int(input("enter the size of the stack"))
while True:
    print("Select the Operation  1.push  2.pop  3.Quit")
    choice = int(input())
    if choice == 1:
        push_element()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the  correct Option")

        
