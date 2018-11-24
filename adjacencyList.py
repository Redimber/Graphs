class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    def insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
class Graph:
    def __init__(self,size,):
        self.size = size
        self.instancelist = [ LinkedList() for i in range(self.size)]
        for i in range(size):
            self.instancelist[i].head = None
    def addEdge(self,src,dest):
        newNode = Node(dest)
        newNode.next = self.instancelist[src].head
        self.instancelist[src].head = newNode
        newNode = Node(src)
        newNode.next = self.instancelist[dest].head
        self.instancelist[dest].head = newNode
    def printGraph(self):
        for i in range(self.size):
            currentNode = self.instancelist[i].head
            print(i,end='')
            while(currentNode != None):
                print(" -> {} ".format(currentNode.data),end='')
                currentNode = currentNode.next
            print()
gr = Graph(5)
gr.addEdge(0,1)
gr.addEdge(0,4)
gr.addEdge(1,2)
gr.addEdge(1,3)
gr.addEdge(1,4)
gr.addEdge(2,3)
gr.addEdge(3,4)
gr.printGraph()



