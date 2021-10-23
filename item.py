import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount, class attribute
    all = []

    def __init__(self, name: str, price: float, quantity= 0):

        # run validations to the received arguments
        # used to check if there is a match of what is happening to your expectation
        assert price >= 0, f"Price {price} is not greater or equal to zero!" # new Python 3 string representation
        assert quantity >= 0, f"Price {quantity} is not greater or equal to zero!"

        #assign self objects
        self.__name = name #makes the name private, once instantiated, cannot be changed and is not seen
        self.price = price
        self.quantity = quantity

        # Action to execute

        Item.all.append(self) # add each new instance to the list

    @property
    #Property decorator = make a read-only attribute
    def name(self):
        return self.__name

    @name.setter #allow users to set a new value for name again
    def name(self, newName):
        if len(newName) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = newName

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    #decorator, a quick way to change the behavior, makes the next line a class method here
    @classmethod
    def instantiate_from_csv(cls): #class reference passed as the first object
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) #read our content as a list of dictionaries
            items = list(reader) #convert reader into a list
        
        for item in items: #get items from a list getting them by key
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    #never sending the first argument as the object, regular function that just receives arguments, a like isolate func
    @staticmethod
    def is_integer(num):
        # We will count out the float that are point zero
        
        #built in function, will enter if is a float
        if isinstance(num, float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): #get class name
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})" # represents the list of all instances in a nice way