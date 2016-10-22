# I know these tests don't cover all the cases & aren't super clean.  They're here
# for learning other stuff, not really for testing the code well or in detail.

import unittest
import mortgage_calc

# def test_broken():
#     assert "expected val" == "something else"

# def test_success():
#     assert "expected val" == "expected val"

def test_calc_monthly_payment():
    loan_principal = 100000
    interest = 5.5
    term = 25
    assert mortgage_calc.calc_monthly_payment(loan_principal,interest,term) == 614.09

def test_calc_total_payment():
    monthly_payment = 1
    term = 1
    assert mortgage_calc.calc_total_payment(monthly_payment, term) == 12

def test_calc_interest_for_month():
    loan_principal = 10000
    monthly_payment = 858.37
    rate = 5.5
    expected_val = 45.83
    calc_val = mortgage_calc.calc_interest_for_month(loan_principal, monthly_payment, rate)
    assert expected_val == calc_val

def test_calc_table_values():
    expected_val = [['Year 1, Month 1', '$   45.83', '$   812.54', '$   9,187.46'],
                    ['Year 1, Month 2', '$   42.11', '$   816.26', '$   8,371.20'],
                    ['Year 1, Month 3', '$   38.37', '$   820.00', '$   7,551.20'],
                    ['Year 1, Month 4', '$   34.61', '$   823.76', '$   6,727.44'],
                    ['Year 1, Month 5', '$   30.83', '$   827.54', '$   5,899.90'],
                    ['Year 1, Month 6', '$   27.04', '$   831.33', '$   5,068.57'],
                    ['Year 1, Month 7', '$   23.23', '$   835.14', '$   4,233.43'],
                    ['Year 1, Month 8', '$   19.40', '$   838.97', '$   3,394.46'],
                    ['Year 1, Month 9', '$   15.56', '$   842.81', '$   2,551.65'],
                    ['Year 1, Month 10', '$   11.70', '$   846.67', '$   1,704.98'],
                    ['Year 1, Month 11', '$    7.81', '$   850.56', '$     854.42'],
                    ['Year 1, Month 12', '$    3.92', '$   854.42', '$       0.00']]
    calc_val = mortgage_calc.create_table_values(1, 10000, 858.37, 5.5)
    assert expected_val == calc_val

def test_print_table(capsys):
    mortgage_calc.print_table(mortgage_calc.create_table_values(1, 10000, 858.37, 5.5))
    out, err = capsys.readouterr()
    assert out == "| Payment          | Interest   | Principal   | Balance      |\n\
|------------------+------------+-------------+--------------|\n\
| Year 1, Month 1  | $   45.83  | $   812.54  | $   9,187.46 |\n\
| Year 1, Month 2  | $   42.11  | $   816.26  | $   8,371.20 |\n\
| Year 1, Month 3  | $   38.37  | $   820.00  | $   7,551.20 |\n\
| Year 1, Month 4  | $   34.61  | $   823.76  | $   6,727.44 |\n\
| Year 1, Month 5  | $   30.83  | $   827.54  | $   5,899.90 |\n\
| Year 1, Month 6  | $   27.04  | $   831.33  | $   5,068.57 |\n\
| Year 1, Month 7  | $   23.23  | $   835.14  | $   4,233.43 |\n\
| Year 1, Month 8  | $   19.40  | $   838.97  | $   3,394.46 |\n\
| Year 1, Month 9  | $   15.56  | $   842.81  | $   2,551.65 |\n\
| Year 1, Month 10 | $   11.70  | $   846.67  | $   1,704.98 |\n\
| Year 1, Month 11 | $    7.81  | $   850.56  | $     854.42 |\n\
| Year 1, Month 12 | $    3.92  | $   854.42  | $       0.00 |\n"

# doesn't work this way
# def test_parser():
#     parser = mortgage_calc.parse_args([10000, 5.5, 1])
#     assertTrue(parser.long)
#     expected_val = 'Namespace(loan=10000.0, rate=5.5, term=1)'
#     assert expected_val == parser
