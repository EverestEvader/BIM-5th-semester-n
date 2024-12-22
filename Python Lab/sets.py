#create sets in python having 4 items each. such that it has atleast two items in common
set1={1,2,3,4,5}
set2={2,4,6,8,9}

#display the items at index 1 & 3 of both sets 
print (f"items at index 1 & 3 are :",list(set1)[1], list(set1)[3])
print (f"items at index 1 & 3 are :",list(set2)[1], list(set2)[3])

#Check either '2' is present in set or not (membership function)
print(2 not in set1)

#add new item of your choice in a set
set1.add(10)
print (set1)

#Remove any item of your choice from a set
set1.remove(5)

#create a new set by combining new set
set3 = set1.union(set2)
print (f"New set by combinig set1 and set2:",set3)

#delete the item of new set3 , print it then also delete set 
set3.clear()
print (set3)
del set3

#show the union, intersection, difference, symmetric difference, isdisjoint, subset and superset operators
a=set1.union(set2)
b=set1.intersection(set2)
c=set1.difference(set2)
d=set1.symmetric_difference(set2)
e=set1.isdisjoint(set2)
f=set1.issubset(set2)
g=set1.issuperset(set2)
print ("Union:",a)
print ("Intersection:", b)
print ("Difference:",c)
print ("symmetric_difference:",d)
print ("isdisjoint:",e)
print ("Subset:",f)
print ("Superset:",g)