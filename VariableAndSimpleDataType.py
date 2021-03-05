# Chapter 2
print("Hello python world")
message = "hello python world"
print(message)
message = "hello python crush course "
print(message)
# message = "the name error"
# print(mesage)

name = 'ada lovelace'
print(name.title())
# in the title method every word will be capital letter
print(name.lower())
print(name.upper())

# Using variables in strings
first_name = "Jahed"
last_name = "hossen"
full_name = f"{first_name} {last_name}"
# f" " is call the f-strings
print(full_name)

print(f"Hello ,{full_name.title()}!")

message = f"Hello, {full_name.upper()}! Jebon"
print(message)
# \t is for white space
print("\tPython")
#\t is for white space and \n is for new line
print('languages:\n\tPython\n\tC\n\tJavaScript')
favorite_language ="  Python"
favorite_language = favorite_language.rstrip()
#rstrip method keep the white space in string
print(favorite_language)
bad_language = ' Ruby '
bad_language = bad_language.lstrip()
print(bad_language)

