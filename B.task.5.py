# STUDENT: Shynggys Sabyrkhan
# GROUP: 1EN04C
# TASK: Task5 problem B
import random
import string

def bananas(height):
    if height >= 2:
        num = 0
        for j in range (2, height+1):
            num += j
        l = []
        for k in range(1, num+1):
            l = l +[random.randint(1, 9)]
        return l
    else:
        return "The End!" 
def drawTree(size, list1):
    if size <= 1:
        return
    else:
        first = 0
        last = 1
        for i in range(1, size+1):
            space = ((size-1)*4+1-((i-1)*4+1))/2
            if i == 1:
                print " "+(" " * space) + "M"
            else:
                print " "+(" " * (space + 1)) + (i-1) * ("/ \ ")
                print (" " * space),
                for j in range(first, last+1):
                    print str(list1[j]) + "  ",
                print
                first = last + 1
                last += i + 1
def listEditorLeft(list_prev, size):
    list_index = []
    list_new = []
    w = 1
    del_list = [0]
    for i in range(3, size + 2):
        del_list.append(w)
        w += i
    first = 0
    for i in del_list[2:]:
        for j in range(first, i):
            list_index.append(j)
            first = i+1
        
    for i in list_index:
        list_new += [list_prev[i]]
    del list_new[0:2]
    return list_new


def listEditorRight(list_prev, size):
    list_new = []
    list_index = []
    for i in range(len(list_prev)):
        list_index.append(i)
    w = 0
    del_list = []
    for i in range(2, size + 1):
        del_list.append(w)
        w += i
    del_list.append(1)
    for i in del_list:
        list_index.remove(i)
    for i in list_index:
        list_new += [list_prev[i]]
    return list_new
def numberOfBananas(list_num, choice):
    if choice == 'l':
        return list_num[0]
    elif choice == 'r':
        return list_num[1]

    
        
    
##        ((s-1)*4+1-((k-1)*4+1))/2      Consider as number of spaces












print """Welcome to Monkey and Bananas game!
Soon you will see banana tree. Monkey starts from top of the tree
and climb down and collects bananas. Your task is select such route
so Monkey will collect bananas as much as possible. Good Luck!"""
sum = 0
while True:
    try:
        n = input("Enter size of Tree: ")
    except SyntaxError:
        print "Enter just number "
        continue
    except NameError:
        print "Number should be entered "
        continue
    if type(n) == int:
        break
l = bananas(n)
drawTree(n, l)
n_l = l
##n_l = listEditorLeft(l, n)
##drawTree(n-1, n_l)
for f in range(n-1, 0, -1):

    choice = raw_input("Enter L or R to select route: ")
    choice = string.lower(choice)
    while choice not in 'rl':
        if len(choice) > 1:
            print "Enter exactly one letter!"
        else:
            print "Enter R or L"
        choice = raw_input("Enter L or R to select route: ")
        choice = string.lower(choice)
    
    sum += numberOfBananas(n_l, choice)
    print "Monkey has "+str(sum)+" bananas![and maximum is ]"
    if choice == 'l':
        n_l = listEditorLeft(n_l, f+1)
        drawTree(f, n_l)
    elif choice == 'r':
        n_l = listEditorRight(n_l, f+1)
        drawTree(f, n_l)

##if maxPossible(n_l) != sum:    
##    print "The End! Monkey has total "+str(sum)+" bananas!"
##elif maxPossible(n_l) == sum:
##    print "The End! Monkey has total "+str(sum)+" bananas!"
##    print "[Congratulations! You are really good!]"
##        
print "The End! Monkey has total "+str(sum)+" bananas!"



