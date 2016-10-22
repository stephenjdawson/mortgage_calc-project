# Simple mortgage calculator
import argparse
import math
import sys
from tabulate import tabulate

def main():
    args = parse_args(sys.argv[1:])
    loan = args.loan
    rate = args.rate
    term = args.term

    monthly_payment = calc_monthly_payment(loan, rate, term)
    total_paid = calc_total_payment(monthly_payment, term)
    print("")
    print("Loan Principal: ${:,.2f}".format(loan))
    print("Interest Rate: {:}%".format(rate))
    print("Ammortization Term: {:} years".format(term))
    print("Total Number of Payents: {:}".format(term * 12))
    print("Monthly Payment: ${:,.2f}".format(monthly_payment))
    print("Total Amount to be Paid: ${:,.2f}".format(total_paid))
    print("Total Interest to be Paid: ${:,.2f}".format(total_paid - loan))
    print("")
    print("Ammortization Schedule:")
    print("")
    print_table(create_table_values(term, loan, monthly_payment, rate))


def calc_monthly_payment(principal, interest, term):
    """Given a principal, interest, and term, calculate monthly payment amount
    """
    # monthly interest rate
    month_interest = interest/(100 * 12)
    # number of payments
    payment_num = term * 12
    # calculate monthly payment
    monthly_payment = principal * (month_interest/(1-math.pow((1+month_interest), (-payment_num))))
    return round(monthly_payment,2)

def calc_total_payment(monthly_payment, term_years):
    """Given a monthly payment and term in years, calculate total amount to be paid
    """
    total_paid = monthly_payment * term_years * 12
    return round(total_paid,2)

def calc_interest_for_month(principal, monthly_payment, rate):
    """Given a principal amount and total payment amount, calculate the interest paid
    """
    interest_this_month = principal * (rate/100) / 12
    return round(interest_this_month,2)

def create_table_values(term, principal, monthly_payment, rate):
    table_values = []
    remaining_principal = principal
    for year in range(1, term+1):
        for month in range(1, 12+1):
            interest_this_month = calc_interest_for_month(remaining_principal, monthly_payment, rate)
            # get the lesser of principal to be paid this month by calculation or
            # remaining_principal (this covers the case where principal owing in the
            # last month is less than the standard calculation figures)
            principal_this_month = min(monthly_payment - interest_this_month, remaining_principal)
            remaining_principal = remaining_principal - principal_this_month
            # store values in order:
            # payment number, interest, principal, balance
            tv_payment_no = "Year {:}, Month {:}".format(year, month)
            tv_interest = "${:>8,.2f}".format(interest_this_month)
            tv_principal = "${:>9,.2f}".format(principal_this_month)
            tv_balance = "${:>11,.2f}".format(remaining_principal)
            table_values.append([tv_payment_no, tv_interest, tv_principal, tv_balance])
    return table_values

def print_table(table_values):
    """Given a list of values to be printed, print the mortgage table
    """
    print(tabulate(table_values, headers=['Payment', 'Interest', 'Principal', 'Balance'], tablefmt='orgtbl'))

def parse_args(args):
    parser = argparse.ArgumentParser(description='Simple mortgage table calculator.')
    parser.add_argument('loan', type=float, help='total amount of the loan')
    parser.add_argument('rate', type=float, help='interest rate (no percentage symbol)')
    parser.add_argument('term', type=int, help='loan term in years')
    return parser.parse_args()


def __init__():
    return

if __name__ == '__main__':
    main()
