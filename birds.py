data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]

def question1():
    total = 0
    for total in range(0,len(data)):
        total = total
    print("Question 1. The total amount of sites are:", total)

def question2():
    for vogels in data:
        vogels = data[6][1]
    print("Question 2. The amount of birds on site 7 is:", vogels)

def question3():
    for vogels in data:
        vogels = data[-1][1]
    print("Question 3: Total number of birds counted on the last site is:", vogels)

def question4():
    total_birds = sum([site[1] for site in data])
    print(f"Question 4: The total number of birds counted accross all sites are {total_birds}")

def question5():
    total_birds = sum([site[1] for site in data]) / len([site[1] for site in data])
    print("Question 5: The average number of birds is :",round(total_birds))

def question6():
    # for site in data if site[0][0] == "C":
    #     print(site)
    total_birds = sum([site[1] for site in data if site[0][0] == "C"])
    print(f"Question 6: The total number of birds counted accross sites C are {total_birds}")

def runcode():
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()

runcode()

