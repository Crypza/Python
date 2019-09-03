# variabler för att komma ihåg namn och ålder

# läsa in namn

name = input("Skriv ditt namn här: ")

# läsa in ålder

age = int(input("Skriv din ålder här: "))

# skriva ut om du är 18 eller inte

if age > 17:
    print("Legal")
else:
    print("Illegal")
    exit()

# skriva ut hej namn och du är x gammal

print("Hej", name, ".")
print("Du är", age, "år gammal.")

