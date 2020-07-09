# Write a class to hold player information, e.g. what room they are in
# currently.


# Variable to hold current location?
class Player:
    def __init__(self, position):
        self.position = position

    def __str__(self):
        return str(self.position)

