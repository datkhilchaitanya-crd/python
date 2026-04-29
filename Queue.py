class Queue:
    def __init__(self):
        self.queue = []

    def enque(self, item):
        self.queue.append(item)
        print(item, "enqueued into queue")

    def deque(self):
        if len(self.queue) == 0:
            print("Queue is Empty, Nothing to Dequeue")
            return None
        else:
            return self.queue.pop(0) 
    def display(self):
        print("Queue elements are:", self.queue)


q = Queue()

while True:
    print("""
    1. Enqueue
    2. Dequeue
    3. Display
    4. Exit
    """)

    choice = int(input("Enter an option: "))

    if choice == 1:
        item = input("Enter item to Enqueue: ")
        q.enque(item)

    elif choice == 2:
        removed = q.deque()
        if removed is not None:
            print("Dequeued element:", removed)

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Invalid choice")