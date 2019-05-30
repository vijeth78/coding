
#inheritance 
class employee: 
    raise_mul = 1.10
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
        self.email = name + "@gmail.com"
    
    def fullname(self):
        return ('{}'.format(self.name))
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_mul = amount 
        
    @classmethod
    def from_string(cls, emp_str):
        name, pay= emp_str.split('-')
        return cls(name, pay)
       
    @staticmethod    
    def workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
class engineer(employee):
    raise_mul = 1.5 
    
    def __init__(self, name, pay, proglang):
        super().__init__(name,pay)
        self.proglang = proglang 
        
        
class manager(employee):
    def __init__(self, name, pay, proglang, emplo=None):
        super().__init__(name,pay)
        if emplo is None:
            self.emplo = []     #empty list 
        else:
            self.emplo = emplo 
            

    def add_emp(self,emp):
        if emp not in self.emplo:
            self.emplo.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.emplo:
            self.emplo.remove(emp)

    def print_emp(self):
        for emp in self.emplo:
            print("Empl:", emp.fullname())
            #print("Empl:", emp.name)
    
        
emp1= engineer("ravi", 10000, "Cpp")
emp2= engineer("raj", 20000, "Python")
print("emp1.proglang", emp1.proglang)

mgr1 = manager("Gopal", 50000, "Java", [emp1])
print("emp1.proglang", emp1.proglang)
#print("mgr1.fullname", mgr1.fullname())

mgr1.add_emp(emp2) 
#print(mgr1.empl.name)
print(mgr1.name)
mgr1.print_emp()
mgr1.remove_emp(emp1)
mgr1.print_emp()
######



  
############
############

#decorator property getter setter  
class employee: 

    raise_mul = 1.10
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
        
# without decorator property, email doesnt update with every user change     
    @property
    def fullname(self):
        return ('{} - fullname'.format(self.name))
        
    @fullname.setter
    def fullname(self,name):
        self.name = name 
        
    @fullname.deleter
    def fullname(self):
        print('delete_name')
        self.name = None 

    def raise_amt(self):
        self.pay = int(self.pay*self.raise_mul)
     
    @property   
    def email(self):
        return ('{}@gmail.com'.format(self.name))


         
emp1= employee("ravi", 1000)
emp2= employee("raj", 1500)

emp1.name   = 'Govind'
emp1.name   = 'german'

print(emp1.email)
print(emp1.name)
print(emp1.fullname)      #using fullname as an atttibute
del emp1.fullname
print(emp1.name)
print(emp1.fullname)

#############
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
        
print
print(emp_1 + emp_2)
print(len(emp_1))

print(repr(emp_1)            # = print(emp_1)
print(str(emp_1)
