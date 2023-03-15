char1 = input("Entrez une phrase")
char2 = input("Entrez une autre phrase")

if char1 == char2:
    print("1")
else:
    char2 = char2.replace('*', '[a-z]*')
    import re
    if re.match(char2, char1):
        print("1")
    else:
        print("0")
