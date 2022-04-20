from os import system, name

# ensure that 'tee program output to debug output window' is unchecked... >Tools>Options>Python>Debugging
def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')


def gradebook():
    # copy over gradebook and create functions calcAverage and calcLetterGrade
    def calcAverage(numberOfEntries):

        c = 1
        gradeSum = 0

        while (c <= numberOfEntries):
            try:
                grades = float(input("Grade "+str(c)+": "))
                if grades < 0 or grades > 100:
                    raise ValueError
                else:
                    gradeSum += grades
                    c += 1
            except ValueError:
                print("Invalid decimal value. Grade entered must be between 0 and 100.")
                system("pause")

        avgGrade = round((gradeSum/(c-1)),2)
        return avgGrade

    def calcLetterGrade(decimalGrade):
        if decimalGrade >= 90:
            print("You've earned an A this semester! Excellent work!")
        elif decimalGrade >= 80:
            print("You've earned a B this semester. Nicely done!")
        elif decimalGrade >= 70:
            print("You've earned a C this semester. Keep studying!")
        elif decimalGrade >= 60:
            print("You've earned a D this semester. There is much room for improvement.")
        else:
            print("You've earned an F this semester. See me after class.")

    print("Calculate Average Grade")
    print("=========================\n")

    entries = float(input("Enter the number of grades you would like to enter: "))

    avgGrade = calcAverage(entries)
    print("Average Grade:", str(avgGrade))
    calcLetterGrade(avgGrade)
    system("pause")
    clear()


def payrollCalc():
    # copy over payrollCalc and create function calcPay
    def calculatePay(name, hours, rate):
        if hours > 40:
            totalPay = round((hours*rate+((hours-40)*(r*1.5))),2)
        else:
            totalPay = round((hours*rate),2)
    
        return totalPay

    print("Payroll Admin Pro")
    print("===============\n")

    n = input("Enter employee name: ")
    h = round(float(input("Enter hours worked: ")))
    r = float(input("Enter employee pay rate: $"))

    totalPay = calculatePay(n,h,r)
    print(n+" has earned $"+str(totalPay)+" this pay period. Nice work!")
    system("pause")
    clear()


def drivingExpenses():
    # copy over drivingExpenses and create function calcTripExp
    def calculateTrip(miles, costPerGallon, mpg, parkingFees, tollFees):
        totalCost = costPerGallon*(miles/mpg)+(parkingFees+tollFees)
        totalCost = round(totalCost, 2)
        return totalCost

    print("Driving Expenses Pro")
    print("===============\n")

    miles = float(input("How many miles have you driven? "))
    costPerGallon = float(input("Enter the cost per gallon of gas: "))
    mpg = float(input("How many miles per gallon does your car average? "))
    parkingFees = float(input("Enter the total amount spent on parking: "))
    tollFees = float(input("Enter the total amount spent on tolls: "))

    totalCost = calculateTrip(miles, costPerGallon, mpg, parkingFees, tollFees)
    print("The total driving expenses for this trip are $"+str(totalCost))
    system("pause")
    clear()


def exit():
    print("Thanks for using this App. Goodbye.")


def error():
    print("Error: Unrecognized Entry -- try again")
    system("pause")
    clear()


choice=""
while(choice != 'd'):
    print("My Apps")
    print("==========\n")
    print("a) Run the gradebook calculator 'Gradebook Pro'")
    print("b) Run the payroll calculator 'Payroll Admin Pro'")
    print("c) Run the driving expenses calculator 'Driving Expenses Pro'")
    print("d) QUIT\n\n")
    choice = input("Select the application that you would like to run: ")
    if(choice == 'a'):
        gradebook()
    elif(choice == 'b'):
        payrollCalc()
    elif(choice == 'c'):
        drivingExpenses()
    elif(choice == 'd'):
        exit()
    else:
        error()
