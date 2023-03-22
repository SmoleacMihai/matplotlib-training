import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.interpolate import make_interp_spline
import numpy as np
import datetime as DT
from matplotlib.dates import date2num


def task1():
    X = [0, 50]
    Y = [value * 3 for value in X]
    plt.plot(X, Y)
    plt.title("Task 1")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task2():
    X = [1, 2, 3]
    Y = [2, 4, 1]
    plt.plot(X, Y)
    plt.margins(x=0)
    plt.title("Task 2")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task3():
    with open("text.txt") as f:
        mylist = f.read().splitlines()
    f.close()

    x = [int(row.split(' ')[0]) for row in mylist]
    y = [int(row.split(' ')[1]) for row in mylist]

    plt.plot(x, y)
    plt.margins(x=0)
    plt.title("Task 3")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task4():
    df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
    df.plot()
    plt.show()


def task5():
    x = [10, 20, 30]
    y = [20, 40, 10]
    x1 = [10, 20, 30]
    y1 = [40, 10, 30]

    plt.plot(x, y, label="line 1")
    plt.plot(x1, y1, label="line 2", color="green")
    plt.margins(x=0, y=0)
    plt.legend()
    plt.title("Task 5")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task6():
    x = [10, 20, 30]
    y = [20, 40, 10]
    x1 = [10, 20, 30]
    y1 = [40, 10, 30]

    plt.plot(x, y, label="line1-width-3", color="blue", lw=3)
    plt.plot(x1, y1, label="line2-width-5", color="red", lw=5)
    plt.margins(x=0, y=0)
    plt.legend()
    plt.title("Task 6")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task7():
    x = [10, 20, 30]
    y = [20, 40, 10]
    x1 = [10, 20, 30]
    y1 = [40, 10, 30]

    plt.plot(x, y, ":", label="line1-dotted-width-3", color="blue", lw=3)
    plt.plot(x1, y1, "--", label="line2-dashed-width-5", color="red", lw=5)
    plt.margins(x=0, y=0)
    plt.legend()
    plt.title("Task 7")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task8():
    x = [1, 4, 5, 6, 7]
    y = [2, 6, 3, 6, 3]

    plt.plot(x, y, "-.", color="r", lw=3, marker='o', markerfacecolor='blue', markersize=12)
    # plt.margins(x=0, y=0.5)
    # Set the y-limits of the current axes.
    plt.ylim(1, 8)
    # Set the x-limits of the current axes.
    plt.xlim(1, 8)
    plt.title("Task 8")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task9():
    x = [0, 50]
    y = [0, 150]

    plt.plot(x, y)
    # Set the y-limits of the current axes.
    plt.ylim(1, 200)
    # Set the x-limits of the current axes.
    plt.xlim(1, 100)
    plt.title("Task 9")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task10():
    x = [2, 3, 5, 6, 8]
    y = [1, 5, 10, 18, 20]
    x1 = [3, 4, 6, 7, 9]
    y1 = [2, 6, 12, 20, 22]

    plt.plot(x, y, "*", markerfacecolor='blue')
    plt.plot(x1, y1, "o", markerfacecolor='red')

    plt.title("Task 10")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def task11():
    t = np.arange(0., 5., 0.2)

    # green dashes, blue squares and red triangles
    plt.plot(t, t, 'g--', t, t ** 2, 'bs', t, t ** 3, 'r^', t, t ** 1.5, "*:")
    plt.title("task 11")
    plt.show()


def task12():
    data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
            (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
            (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
            (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
            (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]

    x = [date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]

    fig = plt.figure()

    graph = fig.add_subplot(111)

    # Plot the data as a red line with round markers
    graph.plot(x, y, 'r-o')

    # Set the xtick locations
    graph.set_xticks(x)

    # Set the xtick labels
    graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
    )
    plt.margins(x=0)
    plt.show()


def task13():
    data = [(DT.datetime.strptime('03-10-16', "%d-%m-%y"), 772.559998),
            (DT.datetime.strptime('04-10-16', "%d-%m-%y"), 776.429993),
            (DT.datetime.strptime('05-10-16', "%d-%m-%y"), 776.469971),
            (DT.datetime.strptime('06-10-16', "%d-%m-%y"), 776.859985),
            (DT.datetime.strptime('07-10-16', "%d-%m-%y"), 775.080017)]

    x = [date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]

    fig = plt.figure()

    graph = fig.add_subplot(111)

    # Plot the data as a red line with round markers
    graph.plot(x, y, 'r-o')

    # Set the xtick locations
    graph.set_xticks(x)

    # Set the xtick labels
    graph.set_xticklabels(
        [date.strftime("%d-%m-%y") for (date, value) in data]
    )
    plt.margins(x=0)
    plt.grid(which="major", color="b", linestyle="--", linewidth=0.5)
    # plt.grid(axis='x') la y analogic
    plt.show()


def task14():
    data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
            (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
            (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
            (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
            (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]

    x = [date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]

    fig = plt.figure()

    graph = fig.add_subplot(111)

    # Plot the data as a red line with round markers
    graph.plot(x, y, 'r-o')

    # Set the xtick locations
    graph.set_xticks(x)

    # Set the xtick labels
    graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
    )

    # naming the x axis
    plt.xlabel('Date')
    # naming the y axis
    plt.ylabel('Closing Value')
    # giving a title
    plt.title('Closing stock value of Alphabet Inc.')
    # Turn on the minor TICKS, which are required for the minor GRID
    plt.minorticks_on()

    # Customize the major grid
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    # Customize the minor grid
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    # Turn off the display of all ticks.
    plt.tick_params(which='both',  # Options for both major and minor ticks
                    top='off',  # turn off top ticks
                    left='off',  # turn off left ticks
                    right='off',  # turn off right ticks
                    bottom='off')  # turn off bottom ticks
    plt.show()


def task15():
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.020, left=0.020, top=0.900, right=0.800)

    plt.subplot(2, 1, 1)
    plt.xticks(()), plt.yticks(())

    plt.subplot(2, 3, 4)
    plt.xticks(())
    plt.yticks(())

    plt.subplot(2, 3, 5)
    plt.xticks(())
    plt.yticks(())

    plt.subplot(2, 3, 6)
    plt.xticks(())
    plt.yticks(())

    plt.show()


def exercise1():
    df = pd.read_csv('company_sales_data.csv')
    profitList = df["total_profit"].tolist()
    monthList = df["month_number"].tolist()

    plt.plot(monthList, profitList, label="Month-wise Profit data of last year")
    plt.xlabel("Month number")
    plt.ylabel("Profit in dollar")
    plt.title('Company profit per month')

    plt.show()
    # print(df.to_string())


def exercise2():
    df = pd.read_csv('company_sales_data.csv')
    profitList = df["total_profit"].tolist()
    monthList = df["month_number"].tolist()

    plt.plot(monthList, profitList, "--r", lw=3, label="Month-wise Profit data of last year", marker="o",
             markerfacecolor='black')
    plt.legend(loc="lower right")
    plt.xlabel("Month number")
    plt.ylabel("Profit in dollar")
    plt.title('Company profit per month')

    plt.show()


def exercise3():
    df = pd.read_csv('company_sales_data.csv')
    arr = np.array(df.values)
    arr = np.transpose(arr)
    # listOfHeadears = list(df.columns)
    labelOptions = [
        "Face cream Sales Data",
        "Face Wash Sales Data",
        "ToothPaste Sales Data",
        "Bathing Soap Sales Data",
        "Bathing Soap Sales Data",
        "Moisturizer Sales Data",
    ]

    i = 0
    for salesData in arr[1:-2]:
        plt.plot(arr[0], salesData, label=labelOptions[i], marker='o', linewidth=3)
        i += 1

    plt.legend()
    plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
    plt.xlabel("Month number")
    plt.ylabel("Sales units in number")
    plt.title('Sales data')
    plt.show()


def exercise4():
    df = pd.read_csv('company_sales_data.csv')
    toothpasteList = df["toothpaste"].tolist()
    monthList = df["month_number"].tolist()
    # listOfHeadears = list(df.columns)
    # print(listOfHeadears)
    plt.plot(monthList, toothpasteList, "ob", label="Tooth paste Sales data")
    plt.legend()
    plt.grid(True, linewidth=1, linestyle="--")
    plt.xticks(monthList)
    plt.xlabel("Month number")
    plt.ylabel("Number of units sold")
    plt.title('Tooth paste Sales data')

    plt.show()


def exercise5():
    df = pd.read_csv('company_sales_data.csv')
    monthList = df['month_number'].tolist()
    faceCremSalesData = df['facecream'].tolist()
    faceWashSalesData = df['facewash'].tolist()

    plt.bar([a for a in monthList], faceWashSalesData, color="orange", width=0.25, label='Face Cream sales data', align='edge')
    plt.bar([a for a in monthList], faceCremSalesData, color="tab:blue", width=-0.25, label='Face Wash sales data', align='edge')
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.title(' Sales data')

    plt.xticks(monthList)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('Facewash and facecream sales data')
    plt.show()


def exercise6():
    df = pd.read_csv('company_sales_data.csv')
    monthList = df['month_number'].tolist()
    bathhingsoapSalesData = df['bathingsoap'].tolist()

    plt.bar([a for a in monthList], bathhingsoapSalesData,  label='Face Cream sales data',
            align='center')

    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.title(' Sales data')

    plt.xticks(monthList)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('Facewash and facecream sales data')
    plt.show()


def exercise7():
    df = pd.read_csv('company_sales_data.csv')
    profitList = df['total_profit'].tolist()
    labels = ['low', 'average', 'Good', 'Best']
    profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
    plt.hist(profitList, profit_range, label='Profit data')
    plt.xlabel('profit range in dollar')
    plt.ylabel('Actual Profit in dollar')
    plt.legend(loc='upper left')
    plt.xticks(profit_range)
    plt.title('Profit data')
    plt.show()


def exercise8():
    df = pd.read_csv('company_sales_data.csv')
    monthList = df['month_number'].tolist()

    labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
    salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(),
                 df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]
    plt.axis("equal")
    plt.pie(salesData, labels=labels, autopct='%1.1f%%')
    plt.legend(loc='lower right')
    plt.title('Sales data')
    plt.show()


def exercise9():
    df = pd.read_csv('company_sales_data.csv')
    monthList = df['month_number'].tolist()
    bathingsoap = df['bathingsoap'].tolist()
    faceWashSalesData = df['facewash'].tolist()

    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(monthList, bathingsoap, label='Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
    axarr[0].set_title('Sales data of  a Bathingsoap')
    axarr[1].plot(monthList, faceWashSalesData, label='Face Wash Sales Data', color='r', marker='o', linewidth=3)
    axarr[1].set_title('Sales data of  a facewash')

    plt.xticks(monthList)
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.show()


def exercise10():
    df = pd.read_csv('company_sales_data.csv')
    monthList = df['month_number'].tolist()

    faceCremSalesData = df['facecream'].tolist()
    faceWashSalesData = df['facewash'].tolist()
    toothPasteSalesData = df['toothpaste'].tolist()
    bathingsoapSalesData = df['bathingsoap'].tolist()
    shampooSalesData = df['shampoo'].tolist()
    moisturizerSalesData = df['moisturizer'].tolist()

    plt.plot([], [], color='m', label='face Cream', linewidth=5)
    plt.plot([], [], color='c', label='Face wash', linewidth=5)
    plt.plot([], [], color='r', label='Tooth paste', linewidth=5)
    plt.plot([], [], color='k', label='Bathing soap', linewidth=5)
    plt.plot([], [], color='g', label='Shampoo', linewidth=5)
    plt.plot([], [], color='y', label='Moisturizer', linewidth=5)

    plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData,
                  bathingsoapSalesData, shampooSalesData, moisturizerSalesData,
                  colors=['m', 'c', 'r', 'k', 'g', 'y'])

    plt.xlabel('Month Number')
    plt.ylabel('Sales unints in Number')
    plt.title('Alll product sales data using stack plot')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    # task10()
    # task11()
    # task12()
    # task13()
    # task14()
    # task15()
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()
    # exercise8()
    # exercise9()
    exercise10()