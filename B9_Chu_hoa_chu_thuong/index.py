input_string = input()

has_upper = sum(1 for char in input_string if char.isupper())
has_lower = sum(1 for char in input_string if char.islower())

if has_lower >= has_upper:
    print(input_string.lower())
else:
    print(input_string.upper())
