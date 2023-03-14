# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:04:33 2022

@author: vollmera
"""
#is there an way to optimse riks to invest money to ko distance
# Question
# is it better to risk 300€ as 100% withe KO xx
# or better put 1000€ and risk 30% => 300€ wit KO xx+1

hebel=10
risk_amount=300
money=1000


kurs=100

taget_hebel=10

kurs-kurs*0.9

def calc_ko(kurs,target_lever):
    return kurs*(1-(target_lever/100))
    

calc_ko(100,50)