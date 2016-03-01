class Node(object):
    def __init__(self,cargo=None):
        self.cargo=cargo
        self.next=None
    def __str__(self):
        return str(self.cargo)
class Student(object):
    def __init__(self,name='Someman',surname='Somemanovich'):
        self.name=name
        self.surname=surname
    def __str__(self):
        return (self.name+self.surname)
    def __cmp__(self,other):
        return cmp(self.surname+self.name,other.surname+other.name)
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.length=0
    def add(self,elem):
        if self.head==None:
            self.head=Node(elem)
            self.length+=1
        elif self.head.cargo>elem:
            t= Node(elem)
            t.next=self.head
            self.head=t
            self.length+=1
        else:
            self.insert(self.head,elem)
            self.length+=1
    def insert(self,node,elem):
        if node.cargo<elem:
            if node.next==None or node.next.cargo>elem:
                t=Node(elem)
                t.next=node.next
                node.next=t
            else:
                self.insert(node.next ,elem)
    def __str__(self):
        res='LL ='
        node=self.head
        while node:
            res+=str(node)+' '
            node=node.next
        return res
l=LinkedList() 
while True:
    x= raw_input('----->')
    l.add(x)
    print l
    
