class Calc:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first+self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first-self.second
        return result
    def div(self):
        result = self.first/self.second
        return result
def main():
    calc = CalcUI(int(input("첫번째 수 : ")),int(input("두번째 수 :")))
    print(calc.first)
    print(calc.second)
    print("{} + {} = {}".format(calc.first , calc.second , calc.sum()))
    print("{} - {} = {}".format(calc.first , calc.second , calc.sub()))
    print("{} * {} = {}".format(calc.first , calc.second , calc.mul()))
    print("{} / {} = {}".format(calc.first , calc.second , calc.div()))
