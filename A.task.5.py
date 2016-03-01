# STUDENT: Shynggys Sabyrkhan
# GROUP: 1EN04C
# TASK: Task5 problem A
import pickle


def saveToFile(students):
    f = open("telephoneBook.pck", "w")
    pickle.dump(students, f)
    f.close()

    
def readFromFile(students):
    try:
        f = open("telephoneBook.pck", "r")
        data = pickle.load(f)
        for d in data:
            students.append(d)
        f.close()
    except IOError, m:
        print "No data!", m


def printMenu():
    print """
*************************
1. Show all contacts
2. Insert new contact
3. Find contact
4. Exit
*************************
"""

    
def findContacts(students):
    print """
#########################################################
"""
    contact = raw_input("Enter contact name: ")
    print "Following contacts have", "‘"+contact+"’:"
    for i in students:
        if contact.lower() in i.lower():
            print i
    print """
#########################################################
"""

def addContact(students):
    print """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
    name = raw_input("Enter contact name: ")
    phone_number = input("Enter contact telephone: " )
    students.append(name+" : "+str(phone_number))
    print "Your contact is saved…"
    print """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

    
def showList(students):
    print """
+++++++++++++++++++++++++++++++++++++
"""
    for st in sorted(students):
        print st
    print "That is all…"
    print """
+++++++++++++++++++++++++++++++++++++
"""


print "Welcome to Telephone book!"
print "Select one of the following:"

        
s = []
readFromFile(s)
while True:
    printMenu()
    try:
        choice = input("Enter your choice: ")
    except SyntaxError, m:
        print "No Such fucntion", m
        continue
    except NameError, m:
        print "No such function:", m
        continue
    print "Your choice:", choice
    if choice == 1:
        showList(s)
    elif choice == 2:
        addContact(s)
    elif choice == 3:
        findContacts(s)
    elif choice == 4:
        break
saveToFile(s)
print "Good Bye!"
