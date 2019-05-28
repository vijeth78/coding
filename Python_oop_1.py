#Python practise OOP concepts
class employee: 
#pass- class with no attributes, members

    raise_mul = 1.10
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
    
    
    def fullname(self):
        print ('{}'.format(self.name))

    def raise_amt(self):
        self.pay = int(self.pay*self.raise_mul)
    
emp1= employee("ravi", 100)
emp2= employee("raj", 150)


#print(emp1.fullname())
emp1.fullname()
emp2.raise_amt()
print(emp2.pay)
####
#class method @classmethod
class employee: 
    raise_mul = 1.10
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
    
    
    def fullname(self):
        print ('{}'.format(self.name))
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_mul = amount 
        
    @classmethod
    def from_string(cls, emp_str):
        name, pay= emp_str.split('-')
        return cls(name, pay)
    
emp3_s = 'carrot-500'
new_emp3 = employee.from_string(emp3_s)
    
emp1= employee("ravi", 100)
emp2= employee("raj", 150)


#print(emp1.fullname())
#employee.set_raise_amt(1.4)
print("employee", employee.raise_mul)
#emp1.set_raise_amt(1.3)
#print("emp1", employee.raise_mul)
print(new_emp3.name)

##### staticmethod
class employee: 
    raise_mul = 1.10
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
    
    
    def fullname(self):
        print ('{}'.format(self.name))
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_mul = amount 
        
    @classmethod
    def from_string(cls, emp_str):
        name, pay= emp_str.split('-')
        return cls(name, pay)
#Check weekday, 5,6 are weekend        
    @staticmethod    
    def workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
emp3_s = 'carrot-500'
new_emp3 = employee.from_string(emp3_s)
    
emp1= employee("ravi", 100)
emp2= employee("raj", 150)

import datetime
date_my = datetime.date(2019,5,27)

print(employee.workday(date_my))
print(date_my)
####
print(help(emp1))

  
