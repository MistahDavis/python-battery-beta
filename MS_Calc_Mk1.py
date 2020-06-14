# Money Saver Calculator
# Calculates the amount of money that can be saved a month depending on person's income
# Initial formula used will be Pascal's triangle or binomial coefficient
# formula --- n*(n+1)/2
import pprint as pp


class Calculator():

    def __init__(self):
        self.__months = {
            "Jan": 31,
            "Feb": 28,
            "Mar": 31,
            "Apr": 30,
            "May": 31,
            "Jun": 30,
            "Jul": 31,
            "Aug": 31,
            "Sep": 30,
            "Oct": 31,
            "Nov": 30,
            "Dec": 31,
        }
        self.result = 0
        # self.change = 0

    def tri_num(self, x):
        value = ((x * (x + 1)) / 2)
        return value

    def cents(self, n):
        if n >= int(30):
            cents = ((self.tri_num(9) * 3) * .10) + ((n % 30) * .10)
        elif n <= int(29):
            cents = ((self.tri_num(9) * 3) * .10)
        return cents

    def ms_calc_v1(self, in_month):
        month = self.__months.get(in_month)
        try:
            for days in range(1, int(month) + 1):
                if days % 10 == 0:  # divisible by 10
                    self.result = self.result + days
                    print("Day: " + str(days) + " Cash: " + "$" + "{:.2f}".format(self.result))
                else:
                    self.result = self.tri_num(days)
                    print("Day: " + str(days) + " Cash: " + "$" + "{:.2f}".format(self.result))
            change = self.cents(days)
            self.result = self.result + change
            print("Change: " + "{:.2f}".format(change))


            print("Final Result\n=============\n" + "Month: " + in_month + "\nDays: " + str(
                days) + "\nCash: " + "$" + "{:.2f}".format(self.result))
        except:
            print(
                "=" * 15 + "ERROR" + "=" * 15 + "\n" + in_month + " is an invalid Month. Please type month as the following.")
            print(', '.join(self.__months.keys()) + "\n" + "=" * 15 + "ERROR" + "=" * 15)

    def ms_calc_v2(self):
        for n in range(1, self.__cal_dict.get("Jan") + 1):
            if n % 10 == 0:  # divisible by 10
                self.result = self.result + n
                print("Day: " + str(n) + " Cash: " + "$" + "{:.2f}".format(self.result))
            else:
                self.change = (n * (n + 1) / 2) * .10
                self.result = (n * (n + 1) / 2) + self.change
                print("Day: " + str(n) + " Cash: " + "$" + "{:.2f}".format(self.result))


calc = Calculator()
calc.ms_calc_v1("Feb")
calc.ms_calc_v1("Fab")
calc.ms_calc_v1("Sep")
calc.ms_calc_v1("Oct")
# ms_calc_v2()

x = 7
print(calc.tri_num(x) * .10)