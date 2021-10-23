from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity= 0, broken_phones=0):
        # Call to super function to have access to all attributes / methods from the parent class
        super().__init__(
            name, price, quantity
        )

        # run validations to the received arguments
        # used to check if there is a match of what is happening to your expectation
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal to zero!"

        #assign self objects
        self.broken_phones = broken_phones