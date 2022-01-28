# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:49:53 2022

@author: vollmera
"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

N = norm.cdf


ticker="BAYN.DE"
strike =55
riskFreeRate=0.1
kurs = 51
restTime = 1
sigma = 0.3


def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)

def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)





def BS_Call_p(S, K, T, r, sigma):
    return BS_CALL(S, K, T, r, sigma)*(1-BS_CALL(S, K, T, r, sigma))

"""
S Effect on Option Value
Here we will hold constant all the variables except the current stock price S and examine how the value of calls and puts change. 

"""
K=kurs
r=riskFreeRate
T=restTime
S = np.arange(60,140,0.1)

calls = [BS_CALL(s, K, T, r, sigma) for s in S]
puts = [BS_PUT(s, K, T, r, sigma) for s in S]
plt.plot(S, calls, label='Call Value')
plt.plot(S, puts, label='Put Value')
plt.xlabel('$S_0$')
plt.ylabel(' Value')
plt.legend()


"""
σ Effect on Black-Scholes Value
As we would expect, when we hold the other variables constant, and increase the volatility parameter both calls and puts increase in value, in what appears to be a linear fashion as shown below.

"""

K_ = kurs
r=riskFreeRate
T=restTime
Sigmas = np.arange(0.1, 1.5, 0.01)
S = strike

calls = [BS_CALL(S, K, T, r, sig) for sig in Sigmas]
puts = [BS_PUT(S, K, T, r, sig) for sig in Sigmas]
plt.plot(Sigmas, calls, label='Call Value')
plt.plot(Sigmas, puts, label='Put Value')
plt.xlabel('$\sigma$')
plt.ylabel(' Value')
plt.legend()


"""
Effect of Time on Black-Scholes Price
 
ime we increase the uncertainty regarding the future price. 
"""
K_ = kurs
r=riskFreeRate
T=restTime
S = strike


T = np.arange(0, 2, 0.01)
sigma = 0.3

calls = [BS_CALL(S, K, t, r, sigma) for t in T]
puts = [BS_PUT(S, K, t, r, sigma) for t in T]
p_calls= [BS_Call_p(S, K, t, r, sigma) for t in T]



plt.plot(T, calls, label='Call Value')
plt.plot(T, puts, label='Put Value')

#plt.plot(T, p_calls, label='gradient Value')


plt.xlabel('$T$ in years')
plt.ylabel(' Value')
plt.legend()


""" standart deviaton and problem of the model
"""


import pandas_datareader.data as web
import pandas as pd
import datetime as dt
from datetime import date
import numpy as np
import matplotlib.pyplot as plt


today = date.today()
start = dt.datetime(2010,1,1)    
end =today
symbol = 'BAYN.DE' ###using Apple as an example
source = 'yahoo'
data = web.DataReader(symbol, source, start, end)
data['change'] = data['Adj Close'].pct_change()
data['rolling_sigma'] = data['change'].rolling(20).std() * np.sqrt(255)


data.rolling_sigma.plot()
plt.ylabel('$\sigma$')
plt.title(str(ticker)+'AAPL Rolling Volatility')




def sigmoid(value):
    s=1/(1+np.exp(-value))
    return (s)


def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))
abc=np.linspace(1,100)

abc=np.linspace(-10,10,100)
aaa=sigmoid(abc)
bbb=sigmoid_p(abc)

plt.scatter(abc,aaa)
plt.scatter(abc,bbb)
