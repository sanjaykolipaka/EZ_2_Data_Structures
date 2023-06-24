def enqueue():
    if len(queue) == n:
        print("queue is Full!")
    else:
        element = input("Enter Element")
        queue.append(element)
        print(queue)
        
def dequeue():
    if not queue:
        print("Stack is empty")
    else:
        e = queue.pop(0)
        print(e,"removed")
        print(queue)
        
queue = []
n = int(input("enter the size of the queue"))
while True:
    print("Select the Operation  1.enqueue  2.dequeue  3.Quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("Enter the  correct Option")

        
