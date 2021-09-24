# accounting app
# Date: 5/6/2020
# Edited Date: 9/23/2021
# Author: Matthew Mckenney 

class Interest():
  '''
  
  '''

  def __init__(self, **kwargs):
    self.principal = kwargs['principal']
    self.interest_rate = kwargs['interest_rate']
    self.time = kwargs['time']
    self.n = kwargs['n']

  def rate(self):
    return self.interest_rate/100

  def simple_interest(self):
    return round(self.principal * (1 + self.rate() * self.time),2)

  def compound_interest(self):
    return round(self.principal * (1 + (self.rate() / self.n)) ** (self.n * self.time), 2)

  def apy(self):
    return round(((1 + (self.rate() / self.n)) ** self.n ) - 1,2)
