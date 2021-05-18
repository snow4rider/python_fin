# accounting app
# Date: 5/6/2020
# Edited Date: 5/17/2021
# Author: Matthew Mckenney


# welcome message
def welcome():
    print("welcome to my accounting software")
    print()


# Compound Interest Formula
# A=P(1+(r/n)^nt
# A = Amount
# P = Principal
# r = interest rate
# n = number of times interest is compounded per unit 't'
# t = Time

def compound_interest(P, r, n, t):
    # returns future amount
    rate = r / 100
    return round(P * (1 + (rate / n)) ** (n * t), 2)


# Simple Interest Formula
# S = Prt
# P = Principal
# r = interest rate
# t = time

def simple_interest(P, r, t):
    # returns amount
    rate = r / 100
    return P * (1 + rate * t)


# Annual percentage Yield
# APY = ((1 + r/n)** n) -1
# r = stated annual interest rate
# n = number of times compounded

def apy(r, n):
    rate = r / 100
    return ((1 + (rate / n)) ** n) - 1
