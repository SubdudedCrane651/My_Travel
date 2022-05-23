import matplotlib.pyplot as plt

plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

global menuchoice
menuchoice = False

global spent
spent = []
for n in range(5):
    spent.append(0)


def graph(spent):
    types = ['airfare', 'tansport', 'hotel', 'food', 'misc']
    y_pos = np.arange(len(types))
    plt.bar(y_pos, spent, align='center', alpha=0.5)
    plt.xticks(y_pos, types)
    plt.ylabel('Amount')
    plt.title('Total spent on trip to Walt Disney World')
    plt.tight_layout()
    plt.savefig("Figure1.png")
    plt.show()


def Save(date, type, amount):
    with open('travel.csv', 'a+') as File:
        File.write("\"" + date + "\"," + "\"" + type + "\"," + amount + "\n")


def Type():
    print("""        1-Airfaire
        2-Transport
        3-Hotel
        4-Food
        5-Misc""")
    type = int(input("Type :"))

    switcher = {
        1: "airfare",
        2: "transport",
        3: "hotel",
        4: "food",
        5: "misc",
    }
    return switcher.get(type)


def Calculate():
    data = pd.read_csv("travel.csv")
    #types=["airfare","transport","hotel","food","misc"]
    #data2=pd.DataFrame(data, index=types)
    if menuchoice:
        print(data.to_string())
    #newdata=data2.sort_index()
    #print(newdata)
    #sumval = data.sum('index' == 'amount')
    #print(sumval)
    total = 0
    airfare_total = 0
    transport_total = 0
    hotel_total = 0
    food_total = 0
    misc_total = 0
    budget = {
        "total": 2613.86,
        "airfare": 570.20,
        "transport": 80,
        "hotel": 0,
        "food": 1420,
        "misc": 543.66
    }

    for index, row in data.iterrows():
        if row['type'] == 'airfare':
            airfare = row['amount']
            airfare_total = airfare_total + airfare
            spent[0] = airfare_total
        if row['type'] == 'transport':
            transport = row['amount']
            transport_total = transport_total + transport
            spent[1] = transport_total
        if row['type'] == 'hotel':
            hotel = row['amount']
            hotel_total = hotel_total + hotel
            spent[2] = hotel_total
        if row['type'] == 'food':
            food = row['amount']
            food_total = food_total + food
            spent[3] = food_total
        if row['type'] == 'misc':
            misc = row['amount']
            misc_total = misc_total + misc
            spent[4] = misc_total

    for i in range(len(data)):
        amount = data.loc[i, 'amount']
        total = total + amount
    print("You have spent " + "${:,.2f}".format(airfare_total) + " in airfare")
    print("You have spent " + "${:,.2f}".format(transport_total) +
          " in transport")
    print("You have spent " + "${:,.2f}".format(hotel_total) + " in hotel")
    print("You have spent " + "${:,.2f}".format(food_total) + " in food")
    print("You have spent " + "${:,.2f}".format(misc_total) + " in misc")
    print("You have spent a total of " + "${:,.2f}".format(total))
    print()
    print("You have " + "${:,.2f}".format(budget["airfare"] - airfare_total) +
          " left over for airfare")
    print("You have " +
          "${:,.2f}".format(budget["transport"] - transport_total) +
          " left over for transport")
    print("You have " + "${:,.2f}".format(budget["hotel"] - hotel_total) +
          " left over for hotel")
    print("You have " + "${:,.2f}".format(budget["food"] - food_total) +
          " left over for food")
    print("You have " + "${:,.2f}".format(budget["misc"] - misc_total) +
          " left over for misc")
    print("You have a total " + "${:,.2f}".format(budget["total"] - total) +
          " left over in the budget")

    graph(spent)


if __name__ == '__main__':
    os.system('clear')
    print("""1-Add
2-Calulate""")
    choice = int(input("Choose :"))
    if choice == 2:
        Calculate()
    else:
        print("Enter date,type and amount")
        date = input("Enter" " date MM/DD/YYYY: ")
        type = Type()
        amount = input("Enter amount :")
        Save(date, type, amount)
        menuchoice = True
        Calculate()
""
