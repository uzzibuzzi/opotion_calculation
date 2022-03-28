# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 11:43:20 2021

@author: vollmera
"""
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np



StockPrice=132
target_value=170
KnockOut=StockPrice*0.62                #meist so 30 % diff
lossValue=0.9               # stop loss limit ca 40%






class KoCalc:
    def __init__(self,price):
        self.StockPrice=price       
        self.KnockOut=self.StockPrice*0.65
        self.lossValue=0.9
        self.targetValue=170
        self.optionRatio=0.1
        
        
    def setTarget(self,target):
        self.targetValue=target
    
    def set_KO(self,target):
        self.KnockOut=target
        
    def calc(self):
        self.KoPercent=((self.StockPrice-(KnockOut))/self.StockPrice)*100
        self.optionPrice=(self.StockPrice-self.KnockOut)*self.optionRatio
        self.sellIt_undelyingAt=max(self.StockPrice* self.lossValue,self.KnockOut)
        self.OptionLossLimit=(self.sellIt_undelyingAt-self.KnockOut)*self.optionRatio
        # stock limit must be checked for ko and max choosen loss value
        self.StockLimit=(self.StockPrice*self.lossValue)  # sell at latest at loss value 
        #self.winrate=(self.valueOption(self.targetValue)-100)/(100-self.valueOption(self.StockLimit))
        self.sellPercent=((self.OptionLossLimit-self.optionPrice)/self.optionPrice)
        
    def valueOption(self,value):
        self.calc()
        self.earning=100+((((value-self.KnockOut)*self.optionRatio)-self.optionPrice)/(self.optionPrice))*100
        if (value < self.KnockOut):
            self.earning=0
        return self.earning
    
    def findOption(self):
        print("Option to buy",self.optionPrice)
        print("KO ",self.KnockOut)
        print("stop loss ",self.StockLimit)
        print(StockPrice,KnockOut,KoPercent)
        
    def draw_earning(self,band):
        """
        this draws the percenteace of the trade
        in a toleranz band in percetn arround the stockprices
        """
        
        x_value=np.linspace(self.StockPrice*(1-(band/100)),self.StockPrice*(1+(band/100)),30)
        y_value=[]
        for a in x_value:
                y_value.append(self.valueOption(a))
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)        
        ax.axhline(y=100, color='g', linestyle='-')
        ax.axvline(x=self.StockLimit,color="r",alpha=0.5)
        ax.axvline(x=self.targetValue,color="g") 
        ax.text(80,240," Option Price {:.2f} \n K.o Percent {:.2f}\n loss Limit {:.2f}% ".format(self.optionPrice,self.KoPercent,self.sellPercent*100),horizontalalignment='left',verticalalignment='top',fontsize=14, color='b')

        ax.scatter(x_value, y_value)    
        ax.grid(which='both')
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        #ylim(0,ymax)
        xmajor_ticks = np.arange(xmin,xmax, 20)
        xminor_ticks = np.arange(xmin,xmax, 5)
        ymajor_ticks = np.arange(ymin,ymax, 20)
        yminor_ticks = np.arange(ymin,ymax, 5)
        ax.set_xticks(xmajor_ticks)
        ax.set_xticks(xminor_ticks, minor=True)
        ax.set_yticks(ymajor_ticks)
        ax.set_yticks(yminor_ticks, minor=True)
        
        # And a corresponding grid
        ax.grid(which='both')
        
        # Or if you want different settings for the grids:
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        
        plt.show()
        
kb=KoCalc(StockPrice)

kb.set_KO(KnockOut)
kb.setTarget(target_value)



kb.draw_earning(50)
print("Stocklimit:",kb.StockLimit)
print("Stockprivcce : ",kb.StockPrice)
print("ko value : ",kb.KnockOut)

print(" loss in  : ",(kb.StockPrice- kb.StockLimit)/kb.StockPrice)
#print(kb.OptionLossLimit)


KoPercent=(StockPrice-KnockOut)/StockPrice*100
optionPrice=(StockPrice-KnockOut)*0.1
sellIt_undelyingAt=max(StockPrice*0.7,KnockOut)

OptionLossLimit=(sellIt_undelyingAt-KnockOut)*0.1
StockLimit=10*(optionPrice*lossValue+KnockOut*0.1)  # sell at latest at loss value 
earning=((target_value-KnockOut)*0.1)-optionPrice
Winpercent=100*(earning/optionPrice)
riskReword=Winpercent/(((optionPrice-optionPrice*lossValue)/optionPrice)*100)



print("your checking stockprize {:.2f} and KO {:.2f} difference is  {:.1f}%".format(StockPrice,KnockOut,KoPercent))
print("prize for option {:.2f} first re order {:.2f}  second reorder {:.2f} ".format(optionPrice,optionPrice*0.95,optionPrice*0.9))
print("limits to sell on option is {:.2f} underlying value is {:.2f}".format(optionPrice*lossValue,StockLimit))
print("win  {:.1f}%  and risk {:.1f}% reward at {:.1f}".format(Winpercent,100*(1-(lossValue)),riskReword))

# hier mus nioch richtig gerechent werden was ist riskio und chance möglihckeit





