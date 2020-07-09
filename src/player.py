from inventory import Inventory

# Write a class to hold player information, e.g. what room they are in
# currently.


# Variable to hold current location?
class Player(Inventory):
    def __init__(self, current_room, name=None, items=None):
        super().__init__(items)
        self.current_room = current_room
        self.name = name

    def __str__(self):
        return str(self.current_room)

