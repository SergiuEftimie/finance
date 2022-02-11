import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import random

x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5 = [],[],[],[],[],[],[],[],[],[],[],[]
amount_series=[]
min_inflation_rate = 1
max_inflation_rate = 3
min_interest_rate = 1
max_interest_rate = 8
nominal_amount = 4800
years = 30

def generate_inflation_rate_series(min_inflation_rate, max_inflation_rate, years):
    inflation_rate = []
    for year in range(years):
        inflation_rate.append(random.randrange(min_inflation_rate,max_inflation_rate+1)/100)
    print (inflation_rate)
    return inflation_rate

def generate_interest_rate_series(min_interest_rate, max_interest_rate,years):
    interest_rate = []
    for year in range(years):
        interest_rate.append(random.randrange(min_interest_rate,max_interest_rate+1)/100)
    print (interest_rate)
    return interest_rate

inflation_rate_series = generate_inflation_rate_series(min_inflation_rate, max_inflation_rate, years)

interest_rate_series = generate_interest_rate_series(min_interest_rate, max_interest_rate, years)

def calculate_inflation(year):
    p = 1
    for i in range(year):
        # print (inflation_rate_series[i])
        am = 1+inflation_rate_series[i]
        p = p * am
    return p

def generate_nominal_compounding(amount, interest_rate):
    am = 0
    for year in range(len(interest_rate)):
        amount = amount + amount * interest_rate[year]
        am += amount
        y.append(am)
        amount_series.append(am)
        x.append(year+1)
    # print (am)
def generate_nominal_compounding_manipulation(amount, interest_rate):
    am = 0
    for year in range(len(interest_rate)):
        amount = amount + amount * max_interest_rate/100
        am += amount
        y4.append(am)
        x4.append(year+1)

def generate_inflation_adjusted_compounding(amount_series):
    for year in range(len(amount_series)):
        i = (amount_series[year]/calculate_inflation(year+1))
        print(i)
        y1.append(i)
        x1.append(year+1)
    print("inflation adjusted compounding")

def generate_inflation_adjusted_deposit():
    for year in range(len(amount_series)):
        i = (year+1)*nominal_amount/calculate_inflation(year+1)
        print(i)
        y2.append(i)
        x2.append(year+1)
    print("inflation adjusted deposit")
    
def generate_deposit():
    amo = 0
    for year in range(len(amount_series)):
        amo = amo + nominal_amount
        # print(amo)
        y3.append(amo)
        x3.append(year+1)

generate_nominal_compounding(nominal_amount, interest_rate_series)
generate_nominal_compounding_manipulation(nominal_amount, interest_rate_series)
generate_inflation_adjusted_compounding(amount_series)
generate_inflation_adjusted_deposit()
generate_deposit()

# plt.plot(x, y, color='blue',label = "Nominal Gains")
# plt.plot(x1, y1, color='green',label = "Inflation Adjusted Nominal Gains")
# plt.plot(x2, y2, color='red',label = "Inflation Adjusted Deposit")
# plt.plot(x3, y3, color='black',label = "Nominal Deposit")
plt.plot(x4, y4, color='brown',label = "Ce zic ei ca o sa castigi")
plt.plot(x, y, color='blue',label = "Ce castigi in conditii reale")
plt.plot(x1, y1, color='green',label = "Ce castigi in conditii reale (ajustat la inflatie)")
plt.plot(x3, y3, color='black',label = "Cat platesti cu bani fizici")
plt.plot(x2, y2, color='red',label = "Valoarea banilor pe care ii platesti (tinand cont de inflatie)")
# plt.plot(x2, y2, color='blue',label = "OVB gains adj for inflation")
# plt.plot(x1, y1, color='red',label = "Investment adj for inflation")
# plt.plot(x3, y3, color='black',label = "Nominal investment")
# plt.plot(x4, y4, color='purple',label = "Nominal investment plus")
# plt.plot(x5, y5, color='red',label = "OVB gains when you adjust the amount to the inflation")
# setting x and y axis range


plt.ylim(0,600000)
plt.xlim(0,30)
plt.xlabel('Years')
plt.ylabel('Amount')
plt.title('Investment')
plt.legend()
plt.grid()
plt.show()