#initialize dictionary of your choice having atleast 3/3 elements
shoes = {
    "Brand":"Nike",
    "Model":"Air Jordan 1 Lost and found",
    "Year":2023
}
#print items of dictionary
print (shoes)
#print any tiem of your choice
print (shoes["Brand"])

#print keys only of dictionary
for key in shoes:
    print (key)

#print only values of dictionary
for value in shoes.values():
    print (value)

#print all key value pair of dictionary
for key, value in shoes.items():
    print (f"{key} : {value}")

#change the value of any item using key
shoes["Year"]=2024
print(shoes)

#add an item in an existing dictionary
shoes["Color"]="Black"
print (shoes)

#delete an item from existing dictionary
del shoes["Brand"]
print (shoes)

#empty the dictionary and delete it
shoes.clear()
print (shoes)

#loop through the values in dictionary and print each values
for values in shoes.values():
    print(values)
#create a copy of dictioary and print it
shoes_copy=shoes.copy()
print(shoes_copy)

""""
jacket ={
    "Brand":"Arctryex",
    "Model":"Gortex",
    "Year":2023
}"""
