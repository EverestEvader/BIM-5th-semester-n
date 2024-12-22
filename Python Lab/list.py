list1=['apple','ball','car','dog','egg']
print("Display the elements in the list without 'a' in it")
newlist=[x for x in list1 if 'a' not in x]
print (newlist)
print("Display the elements of the list in reverse order")
list1.sort(reverse = True)
#list.sort()
print (list1)
print("Copy the elements of list and display it")
newlist=list(list1)
print (newlist)