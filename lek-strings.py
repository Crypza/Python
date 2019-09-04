# Strings
firstName = "tor"
middleName = ""
lastName = "eriksson"
nickName = "crypza"
year = "19"
domain = "elev.ga.ntig.se"
userName = firstName[0:3].lower() + lastName[0:3].lower() + year

email = firstName.lower()
email += "."
email += lastName.lower()
email += "@"
email += domain.lower()

print(email)




#print(userName)
#print(firstName[0:3].lower + lastName[0:3].lower + "19")


#print (firstName.isprintable())




tecken = """() parenteser
[] hakparanteser
{} måsvingar
: kolon5
; semicolon
\"\" dubbelfnuttar
\'\' enkelfnuttar
, komma"""


#print(tecken)
    