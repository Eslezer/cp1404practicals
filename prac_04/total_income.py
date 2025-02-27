"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

#
# def main():
#     """Display income report for incomes over a given number of months."""
#     incomes = []
#     months = int(input("How many months? "))
#
#     for month in range(1, months + 1):
#         income = float(input(f"Enter income for month {month}: "))
#         incomes.append(income)
#
#     print(f"\nIncome Report\n-------------")
#     total = 0
#     for month in range(1, months + 1):
#         income = incomes[month - 1]
#         total += income
#         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
#
#
# main()

def main():
    """display income report for incomes over a given number of months"""
    incomes = []
    num_months = int(input("How many months? "))  # Renamed from 'months' to 'num_months'

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes, num_months)  # Call the new function to print the report


def print_income_report(incomes, num_months):
    """print the income report."""
    print(f"\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
