class MathDojo:
    def __init__(self):
        pass
        self.result=0
    def Add_Number (self,number , *nums):
        for num in nums:
            number+=num
        self.result+= number 
        #print(f"the result of add is: {self.result} ")
        return self
    def Subtract_Nubmer(self,number,*nums):
        for num in nums:
            number+= num
            self.result-= number 
            return self
        
        #print(f"the  display result: {self.result} ")
    def Display(self):
        return  self.result

test_1= MathDojo()
test_2=MathDojo()
test_3=MathDojo()
test_4=MathDojo()
test_5=MathDojo()
test_6=MathDojo()
x=test_1.Add_Number(2).Add_Number(2,5,1).Subtract_Nubmer(3,2).Display()
print(x)

y=test_2.Add_Number(443,88).Subtract_Nubmer(10,10).Subtract_Nubmer(5,5).Display()
print(y)

z=test_3.Add_Number(77).Add_Number(88).Subtract_Nubmer(3,2).Display()
print(z)

test_4_1=test_4.Add_Number(1000).Subtract_Nubmer(10,10).Subtract_Nubmer(5,5).Display()
print(test_4_1)

