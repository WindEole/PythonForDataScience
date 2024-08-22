from S1E7 import Baratheon, Lannister


# DIAMOND INHERITANCE :
# situation où une classe hérite de 2 classes héritières d'une classe commune.
# Cela peut créer des ambiguités dans la résolution des méthodes ou attributs
# hérités. En C++ : virtual. Mais en python : algo de resolution de méthode C3.

# SERIALISATION C3 = algo de resolution de methode
# python utilise l'algo de linéarisation C3 pour résoudre les conflits
# d'héritage de classe. C3 car Cohérente avec 3 propriétés :
#  - graphe de précédence cohérent :
#        respect de la hiérarchie d'héritage, en tenant compte de la relation
#        parent-enfant entre les classes.
#  - préservation de l'ordre de préséance local :
#        l'ordre des classes dans lequel elles sont spécifiées dans la
#        définition d'une classe doit être respecté dans l'ordre de résolution
#        des méthodes (MRO). Autrement dit, si une classe X hérite de A et B
#        dans cet ordre, alors A doit apparaître avant B dans le MRO de X.
#  - appliquant un critère de monotonie => PREVISIBILITE
#        La monotonie garantit que si une classe A apparaît avant une classe B
#        dans l'ordre de résolution des méthodes (MRO) d'une classe donnée,
#        alors A apparaîtra aussi avant B dans le MRO de toutes les
#        sous-classes de cette classe donnée.


class King(Baratheon, Lannister):
    """Representing the King Family."""

    # pas besoin de redefinir init, str ou repr -> utilise ceux de Baratheon

    def set_eyes(self, eyes: str) -> None:
        """Set the eye color for the King."""
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """Set the hair color for the King."""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self) -> str:
        """Get the hair color of the King."""
        return self.hairs
