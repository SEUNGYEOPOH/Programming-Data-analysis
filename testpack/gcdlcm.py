class GcdLcm:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def gcd(self):
        gcd_num=max([i for i in range(1,self.num1+1) if self.num1%i==0 and self.num2%i==0])
        return gcd_num
    def lcm(self):
        lcm_num=min([z for z in range(1,self.num1*self.num2+1) if z%self.num1==0 and z%self.num2==0])
        return lcm_num