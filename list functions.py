 
friends = ["Catriona", "Lucy", "Orla", "Keri"]
lucky_numbers = [1, 17, 19, 22, 42]

# Printing out a list
print(friends) # ['Catriona', 'Lucy', 'Orla', 'Keri']

## Add Elements

friends.append("Eimear") # Add another element
print(friends) # ['Catriona', 'Lucy', 'Orla', 'Keri', 'Eimear']

friends.extend(lucky_numbers) # Add another list
print(friends) # ['Catriona', 'Lucy', 'Orla', 'Keri', 'Eimear', 1, 17, 19, 22, 42]

friends.insert(1, "Jim") # Add Jim into element [1]
print(friends) # ['Catriona', 'Jim', 'Lucy', 'Orla', 'Keri', 'Eimear', 1, 17, 19, 22, 42]

friends.remove("Jim")
print(friends) # ['Catriona', 'Lucy', 'Orla', 'Keri', 'Eimear', 1, 17, 19, 22, 42]

friends.clear() # Empty the list
print(friends) # []

friends.pop() # Removes the last element in the list
print(friends) # []

print(friends.index("Keri")) # returns index of "Keri"

print(friends.count("Catriona")) # returns the number of times the element appears in the list

friends.sort() # Sort the list in ascending order

friends.reverse()

friends2 = friends.copy()
