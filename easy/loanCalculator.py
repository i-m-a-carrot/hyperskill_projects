import math
import argparse

parser = argparse.ArgumentParser()

# > python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
parser.add_argument("--type", type=str)
parser.add_argument("--principal",type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)

args = parser.parse_args()

def check_negative(value):
    for i in loan_info:
        if i < 0:
            return True

def pay_monthly(loanInfo):
    add_monthly =[]
    i = loan_info[2] / (12 * 100)
    for x in range(1,loan_info[1]+1):
        calc = (loan_info[0] / loan_info[1]) + ( i * (loan_info[0] - ((loan_info[0] * (x-1))/loan_info[1])))
        result = math.ceil(calc)
        add_monthly.append(result)
    return add_monthly

def get_annuity_payment(value):
    result = math.ceil(loan_info[0] * (i * math.pow(1+i,loan_info[1]))/(math.pow(1+i,loan_info[1])-1))
    return result

if args.type == "diff" or args.type == "annuity":
    if args.type ==  "diff" and args.payment is not None:
        print("Incorrect parameters")
    else:
        if args.interest is None:
            print("Incorrect parameters")
        else:
            if args.type == "diff":
                loan_info = [args.principal, args.periods, args.interest]
                value = check_negative(loan_info)
                if value == True:
                    print("Incorrect paramters")
                else:
                    result = pay_monthly(loan_info)
                    for  z, x in enumerate(result):
                        print(f"Month {z}: payment is {x}")
                    print(f"\nOverpayment = {sum(result) - loan_info[0]}")
            elif args.type == "annuity":
                if args.payment is not None:
                    if args.periods is not None:
                        loan_info = [args.payment, args.periods, args.interest]
                        i = loan_info[2] / (12 * 100)
                        result = loan_info[0] /((i * math.pow(1+i,loan_info[1]))/(math.pow(1+i,loan_info[1])-1))
                        print(f"Your loan principal = {math.floor(result)}!")

                        over_payment = (args.payment * args.periods) - result
                        print(f"Overpayment = {math.ceil(over_payment)}")

                    else:
                        loan_info = [args.principal, args.payment, args.interest]
                        i = loan_info[2]/(12*100)
                        result = math.log(loan_info[1] / (loan_info[1] - i * loan_info[0]), 1 + i)
                        cal_years = math.ceil(result) // 12
                        cal_months = math.ceil(result) % 12

                        check_years = "year"
                        check_month = "month"

                        if cal_years > 1:
                            check_years = "years"
                        if cal_months > 1:
                            check_months = "months"
                        if math.ceil(cal_months) == 12:
                            extra = math.ceil(cal_months) // 12
                            cal_years += extra
                            cal_months = 0

                        if math.ceil(cal_months) > 0:
                            print(f"It will take {int(cal_years)} {check_years} and {math.ceil(cal_months)} {check_months} to replay this loan!")
                        else:
                            print(f"It will take {int(cal_years)} {check_years} to replay this loan!")
                        over_payment = (loan_info[1] * math.ceil(result)) - loan_info[0]
                        print(f"Overpayment = {over_payment}")

                else:
                    loan_info = [args.principal, args.periods, args.interest]
                    value = check_negative(loan_info)
                    if value == True:
                        print("Incorrect parameteres")
                    else:
                        i = loan_info[2] / (12 * 100)
                        result = get_annuity_payment(loan_info) 
                        print(f"Your annuity payment = {result}!")
                        over_payment = (result * loan_info[1]) - loan_info[0]
                        print(f"Overpayment = {over_payment}")
else:
    print("Incorrect parameters")

