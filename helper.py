#When to use a static method and when to use a class method
#Static method vs class method

class Item:
    @staticmethod
    def is_integet():
        '''
        This should do something that has a relationship with the class, but not something that must be unique per instance
        '''

    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship with the class, but usually, those are used to manipulate different structure of data to instantiate object, like we have done with CSV.
        '''