# lib/owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Return all pets belonging to this owner"""
        return self._pets

    def add_pet(self, pet):
        """Validate and add a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        pet.owner = self  # assign this owner to the pet
        if pet not in self._pets:
            self._pets.append(pet)

    def get_sorted_pets(self):
        """Return pets sorted by name"""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        Pet.all.append(self)

        # Assign owner if provided
        if owner:
            owner.add_pet(self)
