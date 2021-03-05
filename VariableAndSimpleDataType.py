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
# Syntax Error use " ' ' "
message ="use single quation's inside of the double quation's then it will not be error"
print(message)
# Task 
message = ("Hello Eric,would  you like to learn some Python today?")
print(message)

name = "jahed"
print(name.title())
print(name.upper())
print(name.lower())

the_Quote = '   Albert Einstein once said, "A person who never made a    \nmistake never tried anything new"'
print(the_Quote)

famouse_person = "Albert Einstein"

message = f"Hello {famouse_person}, would you like to learn some Python today ?"

print(message)
message = f"Hello {famouse_person.title()}, would you like to learn some Python today ?"

print(message)

message = f"Hello {famouse_person.upper()}, would you like to learn some Python today ?"

print(message)

the_Quote = f'   {famouse_person} once said, "A person who never made a    \nmistake never tried anything new"'
print(the_Quote)

name="jahed h"
name = name.lstrip()
print(name)
name =".Jahed"
name = name.rstrip()
print(name)
print(2+2)
first = 2
second =2.5
third =3
print("the integer number is ",first + third )
print("the float number is {second}")
underscope_with_number = 20_00_000
print(underscope_with_number)
x,y,z = 10,30,20
print(y)

# Constants
MAX_NUM =5000
print(MAX_NUM)

# The Zen of Python
# The Zen of Python, by Tim Peters Beautiful is better than ugly. 
quot = "Simple is better than complex. "
quot2 ="Complex is better than complicated." 
quot3 = "Readability counts."
quot4 =  "There should be one-- and preferably only one --obvious way to do it."
quot5 = " Now is better than never. You could spend the rest of your life learning all the intricacies of Python and of programming in general, but then you’d never complete any proj-ects. Don’t try to write perfect code; write code that works, and then decide whether to improve your code for that project or move on to something new.As you continue to the next chapter and start digging into more involved topics, try to keep this philosophy of simplicity and clarity in mind. Experienced programmers will respect your code more and will be happy to give you feedback and collaborate with you on interesting projects."

print(quot5)
