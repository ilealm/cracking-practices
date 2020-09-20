# EXCERSISES ON COUNTER LIBRARY
from collections import Counter

clothes = Counter()
print(clothes)  # an empty object


# this creates a dict from all distinct elements and in the value is the # of ocurrencies.
text = "The red tinny fox in the forest."
print('\n\nCreate a counter from an input text:', text)
cntr_letters = Counter(text)
print("\ncntr_letters ....")
print(cntr_letters)

# Another way to create a conter, from a list
cntr_colors = Counter()
colors=['blue','blue','blue', 'yellow','yellow','yellow','yellow','yellow' ,'pink','pink', 'pink', 'salmon','salmon', 'red']
print('\nColor list:', colors)
for color in colors:
    cntr_colors[color] += 1
print('Color counter', cntr_colors)



# I can create a counter from a dict
cntr_votes = Counter({"spaguetti": 3, "salmon": 1, "sushi": 4})
print("\n\ncntr_votes", cntr_votes)


# I can create a counter directly, w/o keys as a variables
cntr_pets = Counter(cats=1, dogs=8, fishes=2)
print(cntr_pets)


# Access value of a key
print("\n\nNumber of cats:", cntr_pets["cats"])

# Delete an element
print('\n\nDelete and element, from:')
print(cntr_letters)
del cntr_letters[' ']
print('to delete white space ')
print(cntr_letters)


# Change the value of an element
print("\n\nOriginal value of fhises to:", cntr_pets["fishes"])
cntr_pets["fishes"] = 1
print("Changing the value of fhises to:", cntr_pets["fishes"])


# Display the element the number of times it have it value. It returns a list
# list(c.elements())
print("\n\nDisplay the element the number of times it have it value.")
print(list(cntr_letters.elements()))



# Display the SUM of the values
print('\n\nSum of pets')
print(cntr_pets)
print(sum(cntr_pets.values()))



# Display the MOST common. It returns a TUPLE, where each position is in the order
print("\n\nMost common")
common = cntr_letters.most_common(3)
print(common)
# BC returns a tupple, the 2nd arg. in the array is 0=key, 1=value
print("The 2nd most common key is")
print(common[1][0])
print("The 2nd most common value is")
print(common[1][1])

# remove zero and negative counts
cntr_chores = Counter({'Mop':0, 'Dishes':3, 'Paint':-4, 'Wather':0, 'Kitchen': 3})
print('\nAll chores: ', cntr_chores)
cntr_chores += Counter()
print('\nJust positive: ', cntr_chores)


# Display the last common
print("\n\nDisplay the last common")
n = 3 # the number of less common
print(cntr_letters.most_common()[:-n-1:-1])


# SUBTRACT
# if both dict contains the same keys, it will be substracred
# THE SUBSTACT REMAINS IN THE FIRST DICT. If an element is in b, but not A, will be appeing as negative
cntr_votes = Counter({"spaguetti": 3, "salmon": 1, "sushi": 4, "milkshake": 3})
cntr_votes2 = Counter({"spaguetti": 2, "salmon": 0, "sushi": 1, "donut": 3})
cntr_votes.subtract(cntr_votes2)
print("\n\nSubstracting votes", cntr_votes)


# Create a LIST with only the keys of the dict  USES []
print("\nList of a key", list(cntr_pets))

# Create a SET with only the keys of the dict. USES {}
print("\nList of a key", set(cntr_pets))

# Create a DICT with only the keys of the dict. USES {KEY:VALUE}
print("\nList of a key", dict(cntr_pets))

# Returns a list, and on each position is a tuple with key at the first ele, and value in the 2nd
lst_items = cntr_votes.items()
print("\n\nCounter transformed into items:  ", lst_items)
# print(lst_items.dict_items)


# SORT elements
print('\n\nSORTED elements')
print('original letters', cntr_letters)
print('\n\nsorted in alphabetical order', sorted(cntr_letters))


if __name__ == "__main__":
    pass
