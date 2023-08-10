class Modification():
    def __init__(self, name, description):
        self.name = name
        self.description = description


class ArmorModification():
    def apply_to(self, shinobi):
        shinobi.health_limit += 30

    def remove_from(self, shinobi):
        shinobi.health_limit -= 30

class ChakraRegenerationModificacion(Modification):
    #Дописать