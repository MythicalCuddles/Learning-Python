
is_female = True

if(is_female):
    print("is_female is true")
else:
    print("is_female is false. i feel sorry for you")

if not(is_female):
    print("is_female is false, but not.")
else:
    print("is_female is true, but not.")


is_cute = True

if is_female or is_cute:
    print("hey qt")
else:
    print("maybe one day :)")


if is_female and is_cute:
    print("life goals")
elif is_female or is_cute:
    print("goals")
else:
    print("maybe one day")
