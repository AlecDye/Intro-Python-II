from inventory import Inventory

# Implement a class to hold room information. This should have name and
# description attributes.

# extend room with list/inventory
class Room(Inventory):
    def __init__(
        self, name, description, items=None, n_to=None, s_to=None, e_to=None, w_to=None
    ):
        super().__init__(items)
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        return self.name + self.description

