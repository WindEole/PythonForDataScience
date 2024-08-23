from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)

Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())

print(Joffrey.__dict__)

###########

# print(King.mro())  # Affiche le Method Resolution Order de la classe King
# print(Joffrey.__repr__)
# print(Joffrey.__str__)

###########

# La classe King doit hériter de la méthode create_lannister. Test :

# king_instance = King.create_lannister("Jojo", True)
# print(king_instance.__dict__)
