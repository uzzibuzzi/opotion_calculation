# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 11:43:20 2021

@author: vollmera
"""
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


22/20

Winpercent/(((optionPrice-optionPrice*lossValue)/optionPrice)*100)



class KoCalc:
    def __init__(self,price):
        self.StockPrice=price       
        self.KnockOut=self.StockPrice*0.65
        self.lossValue=0.6
        self.targetValue=self.StockPrice*1.1
        
        
    def setTarget(self,target):
        self.targetValue=target
        
    def calc(self):
        self.KoPercent=((self.StockPrice-self.KnockOut)/self.StockPrice)*100
        self.optionPrice=(self.StockPrice-self.KnockOut)*0.1
        self.sellIt_undelyingAt=max(self.StockPrice*0.7,self.KnockOut)
        self.OptionLossLimit=(self.sellIt_undelyingAt-self.KnockOut)*0.1
  
    def findOption(self):
        print(self.KnockOut)) 
        
  
        
kbx=KoCalc(87)
        
        
    