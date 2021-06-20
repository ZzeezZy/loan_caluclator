import argparse
import math

# D = (P / n) + i * (P - ((P * (m - 1)) / n)
# d = mth differentiated payment
# P = the loan principal for both
# i = nominal interest rate. i / (12 * 100) used in everything
# n = number of payments in number of month used in interest, annuity payment and principal
# m = current repayment month


parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
parameters = [args.type, args.payment, args.principal, args.periods, args.interest]
if args.type is None:
    print("Incorrect parameters")
    exit()
if args.type == 'diff' and args.payment is not None:
    print("Incorrect parameters")
    exit()
if args.interest is None or args.interest < 0:
    print("Incorrect parameters")
    exit()
if len(parameters) < 4:
    print("Incorrect parameters")
    exit()

if args.type == 'diff':
    P = args.principal
    i = float(args.interest / (12 * 100))
    n = args.periods
    aggregate_payment = 0
    m = 1
    while m <= n:
        D = math.ceil((P / n) + i * (P - ((P * (m - 1)) / n)))
        print(f"Month {m}: payment is {D}")
        aggregate_payment += D
        m += 1
    over_payment = aggregate_payment - P
    print(f"Overpayment = {over_payment}")

elif args.type == 'annuity':
    if args.periods is None:

        p = int(args.principal)
        a = int(args.payment)
        i = args.interest / 1200
        n = math.ceil(math.log((a / (a - i * p)), (1 + i)))
        y = n // 12
        months = math.ceil(n % 12)
        if n % 12 != 0:
            print(f"It will take {y} years and {months} months to repay this loan!")
        else:
            print(f"It will take {y} years to repay this loan!")
        overpayment = (n * a) - p
        print(f"Overpayment = {overpayment}")

    elif args.payment is None:
        P = args.principal
        n = args.periods
        i = float(args.interest / (12 * 100))
        a = round(math.ceil(P * (i * math.pow((1 + i), n)) / ((math.pow((1 + i), n)) - 1)))
        print(f"Your monthly payment = {a}!")
        over_payment = (a * n) - P
        print(f"Overpayment = {over_payment}")

    elif args.principal is None:
        a = int(args.payment)
        i = float(args.interest / (12 * 100))
        n = int(args.periods)
        P = round((a / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))), 2)
        print(f"Your loan principal = {P}!")
        over_payment = (a * n) - P
        print(f"Overpayment = {over_payment}")
