class Car:
    def __init__(self,n,p):
        self.name = n
        self.price = p
    

    def show (self):
        print (f'{self.name} costs {self.price}')


c1 = Car ('pride',100)
c2 = Car ('benz', 800)

c1.show()
c2.show()
