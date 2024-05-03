age=int(input("Entrer le numero: "))
majorite=18

condition=age>majorite
if condition:
    print("Condition set")

if age > majorite:
    print("je suis majeur!")
elif age == majorite:
    print("Tout juste majeur depuis aujourd'hui")
else:
    print("je suis mineur..")
print("J'ai",age,"ans")