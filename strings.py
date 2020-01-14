# set phrase string
phrase = "MythicalCuddles"

# print phrase to console
print(phrase)

# print phrase with string to console
print(phrase + " is cute")

# convert string to lowercase
print(phrase.lower())

# convert string to uppercase
print(phrase.upper())

# check if string is lowercase
print(phrase.islower())

# check if string is uppercase
print(phrase.isupper())

# convert string to uppercase and check
print(phrase.upper().isupper())

# get length of string
print(len(phrase))

# get the second character in string
print(phrase[1])



# string with all characters
string = "quick brown fox jumps over the lazy dog"

# using string as defined above, print "Melissa"
print(string[18].upper() + string[24] + string[31] + string[2] + string[20] + string[20] + string[32])

# get index of the letter (18, 24, 31)
print(string.index("m"))
print(string.index("e"))
print(string.index("l"))

# gets index of the first character of string (12)
print(string.index("fox"))


# replace dog with cat and print
print(string.replace("dog", "cat"))
