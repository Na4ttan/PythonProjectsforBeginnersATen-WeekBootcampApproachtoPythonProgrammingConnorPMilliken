'''
# using the title method to capitalize a string
name = "john smith"
print(name.title())

name = name.title()
print(name.lower())
print(name.upper())

# replacing an exclamation point with a period
words = "Hello there!"
print(words.replace("!", "."))

# finding the starting index of our searched term
s = "Look over that way"
print(s.find("over"))

# removing white space with strip
name = "    john    "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#converting a string into a list of words
s = "These words are separated by spaces"
print(s.split(" "))


#THURSDAY EXERCISES
exercise1 = "uppercase"
print(exercise1.upper())

help(" ".strip()) 

exercise2 = "$$John Smith"
print(exercise2.lstrip("$"))
'''

#Friday Project: Printing Receipts.

# create a product and price for three items
p1_name, p1_price = "books", 49.95
p2_name, p2_price = "computer", 579.99
p3_name, p3_price = "monitor", 124.89

# create a company name and information 
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# declare ending message
message = "Thanks for shopping with us today!"

# create a top border
print("*" * 50)

# print company information first, using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

# print a line between sections
print("=" * 50)

#print out header for section of items
print("\tProduct Name\tProduct Price")

# create a print ststement for each product
print("\t{}\t\t${}".format(p1_name.title(), p1_price))
print("\t{}\t\t${}".format(p2_name.tilte(), p2_price))
print("\t{}\t\t${}".format(p3_name.title(), p3_price))