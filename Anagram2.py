# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


str1 = input("string1:")
str2 = input("string2:")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)
 
if sorted_str1 == sorted_str2:
     print("true")
else:
         print("false:")