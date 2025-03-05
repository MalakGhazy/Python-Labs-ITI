# Question 1 : Write a Python program to reverse a string. 

print("Hello,World!"[::-1])

# Question 2 : Write a Python program to check if a string is a palindrome (reads the same backward as forward). 

print("Hello,World!"=="Hello,World!"[::-1])
print("level"=="level"[::-1])

# Qusetion 3 : Write a Python program to remove duplicate characters from a string. 

a = list(set([1,2,3,4,1,2]));print(a)

# Question 4 : 4.Find the Longest Word in a String 
# Write a Python program to find the longest word in a given string. 
# text = "Python is a great programming language" 
# Output=programming 

print(max("Python is a great programming language".split(),key=len))

# Question 5 :Find Common Elements Between Two Tuples 
# Write a Python program to find common elements between two tuples. 

tuple1 = (1, 2, 3) 
tuple2 = (2, 3, 4) 
print(list(set(tuple1) & set(tuple2))) # & => Set Intersection

# Question 6 : Find the Maximum and Minimum Value in a Dictionary 
# Write a Python program to find the maximum and minimum value in a dictionary.  
my_dict = {"a": 10, "b": 20, "c": 5}  

print("Max =",max(my_dict.values()),"\nMin =",min(my_dict.values()))

# Question 7 : Write a Python program to merge two dictionaries. 
dict1 = {"a": 1, "b": 2} 
dict2 = {"c": 3, "d": 4} 

print (dict1 | dict2)

# 8- Find Common Keys in Two Dictionaries 
# Write a Python program to find common keys in two dictionaries. 
dict1 = {"a": 1, "b": 2, "c": 3} 
dict2 = {"b": 2, "c": 4, "d": 5} 
# #Output: {'b', 'c'} 

print(set(dict1)&set(dict2))


# ===========================================================  
# 9- takes a string and prints the longest 
# alphabetical ordered substring occured. 
# For example, if the string is 'abdulrahman' then the output is: 
# Longest substring in alphabetical order is: abdu 

s='abdulrahman'
longest = current = s[0]
for i in range(1,len(s)):
    if s[i]>=s[i-1]:
        current+=s[i]
    else:
        if len(current)>len(longest):
            longest=current
        current=s[i]

if len(current)>len(longest):
    longest=current

print("Longest substring in alphabetical order is:",longest)