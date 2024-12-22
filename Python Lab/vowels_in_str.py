stringin = input("Enter a string: ")
vowels = "aeiorAEIOU"
vowels_count = 0
for char in stringin:
    if char in vowels:
        vowels_count = vowels_count + 1
print(f"No of vowels in {stringin} :", vowels_count)
 