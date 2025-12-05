from pakuri import Pakuri

class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakudex_list = []

    def get_size(self):
        return len(self.pakudex_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if (len(self.pakudex_list) > 0):
            return [pakuri.get_species() for pakuri in self.pakudex_list]
        return None

    def get_stats(self, species):
        if len(self.pakudex_list) != 0 and species in self.get_species_array():
            return [self.pakudex_list[self.get_species_array().index(species)].get_attack(), self.pakudex_list[self.get_species_array().index(species)].get_defense(), self.pakudex_list[self.get_species_array().index(species)].get_speed()]
        return None
    def sort_pakuri(self):
        #this is something I found off here https://docs.python.org/3/howto/sorting.html while trying to figure out the shortest way to write this
        self.pakudex_list.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        if len(self.pakudex_list) != 0 and species not in self.get_species_array() and len(self.pakudex_list) < self.capacity:
            self.pakudex_list.append(Pakuri(species))
            return True
        return False

    def evolve_species(self, species):
        if len(self.pakudex_list) != 0 and species in self.get_species_array():
            self.pakudex_list[self.get_species_array().index(species)].evolve()
            return True
        return False