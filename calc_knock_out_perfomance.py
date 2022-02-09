# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 11:43:20 2021

@author: vollmera
"""
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText


StockPrice=87
target_value=88
KnockOut=77#StockPrice*0.65                #meist so 30 % diff
lossValue=0.6               # stop loss limit ca 40%



KoPercent=(StockPrice-KnockOut)/StockPrice*100
optionPrice=(StockPrice-KnockOut)*0.1
sellIt_undelyingAt=max(StockPrice*0.7,KnockOut)

OptionLossLimit=(sellIt_undelyingAt-KnockOut)*0.1


StockLimit=10*(optionPrice*lossValue+KnockOut*0.1)  # sell at latest at loss value 


earning=((target_value-KnockOut)*0.1)-optionPrice

Winpercent=100*(earning/optionPrice)

print("your checking stockprize {:.2f} and KO {:.2f} difference is  {:.1f}%".format(StockPrice,KnockOut,KoPercent))

print("prize for option {:.2f} first re order {:.2f}  second reorder {:.2f} ".format(optionPrice,optionPrice*0.95,optionPrice*0.9))

print("limits to sell on option is {:.2f} underlying value is {:.2f}".format(optionPrice*lossValue,StockLimit))
riskReword=Winpercent/(((optionPrice-optionPrice*lossValue)/optionPrice)*100)
print("win  {:.1f}%  and risk {:.1f}% reward at {:.1f}".format(Winpercent,100*(1-(lossValue)),riskReword))

# hier mus nioch richtig gerechent werden was ist riskio und chance möglihckeit



class KoCalc:
    def __init__(self,price):
        self.StockPrice=price       
        self.KnockOut=self.StockPrice*0.65
        self.lossValue=0.65
        self.targetValue=self.StockPrice*1.1
        
        
    def setTarget(self,target):
        self.targetValue=target
    
    def set_KO(self,target):
        self.KnockOut=target
        
    def calc(self):
        self.KoPercent=((self.StockPrice-self.KnockOut)/self.StockPrice)*100
        self.optionPrice=(self.StockPrice-self.KnockOut)*0.1
        self.sellIt_undelyingAt=max(self.StockPrice*0.7,self.KnockOut)
        self.OptionLossLimit=(self.sellIt_undelyingAt-self.KnockOut)*0.1
        # stock limit must be checked for ko and max choosen loss value
        self.StockLimit=10*(self.optionPrice*self.lossValue+self.KnockOut*0.1)  # sell at latest at loss value 
        
        
    def valueOption(self,value):
        self.calc()
        self.earning=100+((((value-self.KnockOut)*0.1)-self.optionPrice)/(self.optionPrice))*100
        if (value < self.KnockOut):
            self.earning=0
        return self.earning
    
    def findOption(self):
        print("Option to buy",self.optionPrice)
        print("KO ",self.KnockOut)
        print("stop loss ",self.StockLimit)
        print(StockPrice,KnockOut,KoPercent)
        
    def draw_earning(self,band):
        x_value=[]
        y_value=[]
        for a in range(int(self.StockPrice*(1-(band/100))),int(self.StockPrice*(1+(band/100))),1):
                x_value.append(a)
                y_value.append(self.valueOption(a))
        plt.axhline(y=100, color='g', linestyle='-')
        plt.axvline(x=self.StockLimit,color="r")
        plt.axvline(x=self.targetValue,color="g") 
       # plt.text(0,0,"hgjj",verticalalignment='top')
        plt.scatter(x_value, y_value)        
        
        
        
kb=KoCalc(100)

kb.set_KO(60)
kb.setTarget(115)
kb.draw_earning(15)

kb.valueOption(110)
kb.findOption()