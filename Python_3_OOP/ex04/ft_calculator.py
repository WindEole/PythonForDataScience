# DECORATEUR STATICMETHOD :
# Les méthodes décorées avec @staticmethod n'ont pas accès aux attributs de
# l'instance (self) ni de la classe (cls). Utile pour les fonctions qui n'ont
# besoin d'aucun accès aux attributs de la classe ou de l'instance. Ces
# méthodes peuvent être appelées sur la classe sans créer d'instance.
# Elles ne reçoivent pas automatiquement les arguments self ou cls.

class calculator:
    """Calculator Class.

    Class that do calculation (dot product, addition, subtraction) of two
    vectors of the same size.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors.

        The dot product of two vectors is the multiplication element-wise,
        followed by the sum of the products.
        """
        return print(f"Dot product is: {sum(x * y for x, y in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise."""
        return print(f"Add Vector is : {[x + y for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors element-wise."""
        return print(f"Sous Vector is: {[x - y for x, y in zip(V1, V2)]}")
