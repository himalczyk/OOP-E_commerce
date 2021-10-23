#OOP

#Why classes ? Logically group our data and function to easily re use and build up on method = function associated with a class
#Class is a blueprint to create instances

#Instance variables contain data that is unique for each instance

#init is a constructor, initialize

class Employee:
    #init method, if we create a method within a class they receive the instance as the first argument automatically, thats why 'self'
    def __init__(self, first, last, pay): #argument, the instance is passed automatically so we can leave self, but need to proivde others
        #initialize, create methods within a class, this becomes the first instance within a class automatically, 'self'
        self.first = first
        self.last = first
        self.pay = first
        self.email = first + '.' + last + '@company.com'
        #whenever i say that 'self' is the instance, when we set self.first = first, its the same that saying that emp_1.first = 'Dawid', except now instead of doing that manually, its going to be done automatically when we create our employee objects

        def fullname(self): #each method within a class automatically takes the instance as the first argument
            return '{} {}'.format(self.first, self.last)

#the init method will be run automatically
#employee 1 will be passed as 'self' and then set those arguments

emp_1 = Employee('Dawid', 'Michalczyk', 50000) #this is a unique instance of the class employee
emp_2 = Employee('test', 'user', '60000') #this is also a unique instance of the class employee

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) #method called 'fullname()'
#these do exactly the same
print(Employee.fullname(emp_1)) #emp_1 is 'self' here