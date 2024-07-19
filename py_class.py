class Calculator:
   def __init__(self):
        print('welcom in our calculator')
      
   
   def sum(self,x,y):
        print(x+y)

   def mul(self,x,y):
        print(x*y)

class Sicentific(Calculator):
   def power(self,x,y):
        return x**y
    
x = Sicentific(mom)
x.sum(5,6)
x.mul(2,3)