class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self, other):
        if(self.a>other.a):
            return "ob1 is less then ob2"
        else:
            return "ob2 is less then ob1"
        
    def __eq__(self, other20):
        if(self.a == other20.a):
            return "Both are equal"
        else:
            return "Both are not equal"
        

        
obj1 = A(2)
obj2 = A(3)
print("Passed Values:", obj1.a, obj2.a)
print(obj1 < obj2)

obj3 = A(4)
obj4 = A(4)
print("Passed Values:", obj3.a, obj4.a)
print(obj3 == obj4)