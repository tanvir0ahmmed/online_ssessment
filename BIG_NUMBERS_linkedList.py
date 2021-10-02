""" a = input()
b = input() """
a = "9999"
b = "99"
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

len_a = len(a)
len_b = len(b)
i=0
head = None
#create linked list of input a
while(i<len_a):
    ob = Node(a[i])
    if head == None:
        head = ob
        num_a = head
    else:
        head.next = ob
        ob.prev = head
        head = ob
        num_a = head
    i+=1
head = None
i=0
#create linked list of input b
while(i<len_b):
    ob = Node(b[i])
    if head == None:
        head = ob
        num_b = head
    else:
        head.next = ob
        ob.prev = head
        head = head.next
        num_b = head   
    i+=1   
c = 0
head = None
# Make sum and create linked list of result
while(num_a or num_b):
    if num_a and num_b:
        x = int(num_a.data)
        y = int(num_b.data)
    elif num_a:
        x = int(num_a.data)
        y = 0
    else:
        y = int(num_b.data)
        x = 0

    summ = (x+y+c)%10
    c = (x+y+c)//10
    ob = Node(summ)
    if head == None:
        head = ob
    else:
        head.next = ob
        ob.prev = head
        head = ob
        start = ob
    if num_a: num_a = num_a.prev
    if num_b: num_b = num_b.prev

if c != 0:
    ob = Node(c)
    head.next = ob
    ob.prev = head
    head = ob
    start = ob
#print result
while(start):
    print(start.data,end='')
    start = start.prev
print()
