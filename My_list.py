my_list = []    #An empty list is created

#Append elements under study in order
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)           #15 is inserted in the second position

my_list.extend([50, 60, 70])    #these 3 elements are extended to my_list

my_list.pop()                   #since pop () removes the last element when undefined, 70 is removed

my_list.sort()                 #elements under study are sorted out

print(my_list.index(30))