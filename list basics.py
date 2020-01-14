#lists

friends = ["Catriona", "Lucy", "Orla", "Keri"]
me = ["Melissa", 22] # Lists can contain any data type in any element

## Accessing Elements

# Outputs all of friends to console
print(friends) # ['Catriona', 'Lucy', 'Orla', 'Keri']

# Outputs the fourth element from the friends list
print(friends[3]) # Keri

# Outputs from the back of list
print(friends[-1]) # Keri
print(friends[-2]) # Orla
print(friends[-3]) # Lucy
print(friends[-4]) # Catriona

# Outputs all elements after the second
print(friends[1:]) # ['Lucy', 'Orla', 'Keri']

# Output range second element and third element, does not include [3]
print(friends[1:3]) # ['Lucy', 'Orla']


## Modifiying Elements

friends[1] = "Eimear" # Change Lucy to Eimear
print(friends[1]) # Eimear
