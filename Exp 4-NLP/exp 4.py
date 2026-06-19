noun = input("Enter noun: ")

if noun.endswith("y"):
    plural = noun[:-1] + "ies"
else:
    plural = noun + "s"

print("Plural form:", plural)
