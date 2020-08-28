import math
import argparse


def differentiated_payment(p, n, i):
    s = 0
    for month in range(1, n + 1):
        d_pay = math.ceil(p / n + i * (p - p * (month - 1) / n))
        print(f'Month {month}: paid out {d_pay}')
        s += d_pay
    print(f"\nOverpayment = {s - p}")


def annuity_periods(pr, an_payment, i):
    # formula for number of months
    n = math.ceil(math.log(an_payment / (an_payment - i * pr), 1 + i))
    print(f'You need {"" if n // 12 == 0 else str(n // 12) + " year"}{"s" if n // 12 > 1 else ""}'
          f'{" and " if n // 12 > 0 and n % 12 > 0 else ""}'
          f'{"" if n % 12 == 0 else str(n % 12) + " month"}{"s" if n % 12 > 1 else ""}'
          f' to repay this credit!')
    print(f"Overpayment = {an_payment * n - pr}")


def annuity_payment(pr, n, i):
    # formula for annuity payment
    an_payment = pr * i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)
    print(f'Your annuity payment = {math.ceil(an_payment)}!')
    print(f"Overpayment = {math.ceil(an_payment) * n - pr}")


def annuity_principal(an_payment, n, i):
    # formula for principal
    pr = an_payment / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
    print(f'Your credit principal = {math.floor(pr)}!')
    print(f"Overpayment = {an_payment * n - math.floor(pr)}")


# with argparse
parser = argparse.ArgumentParser(description="that's it")
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int, default=0)
parser.add_argument('--periods', type=int, default=0)
parser.add_argument('--interest', type=float, default=0)
parser.add_argument('--payment', type=int, default=0)
args = parser.parse_args()
per = 0
pay = 0
prin = 0
if args.type == 'diff':
    if args.principal > 0 and args.periods > 0 and args.interest > 0:
        differentiated_payment(args.principal, args.periods, args.interest / 1200)
    else:
        print('Incorrect parameters')
elif args.type == 'annuity':
    if args.principal > 0:
        pay += 1
        per += 1
    if args.periods > 0:
        pay += 1
        prin += 1
    if args.interest > 0:
        pay += 1
        prin += 1
        per += 1
    if args.payment > 0:
        per += 1
        prin += 1
    if per == 3:
        annuity_periods(args.principal, args.payment, args.interest / 1200)
    elif pay == 3:
        annuity_payment(args.principal, args.periods, args.interest / 1200)
    elif prin == 3:
        annuity_principal(args.payment, args.periods, args.interest / 1200)
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')

# without argparse
# import sys
# principal = -1
# periods = -1
# payment = -1
# interest = -1
# def dif_check(sequence):
#     global principal, periods, interest
#     c = 0
#     if sequence[1][:12] == '--principal=' and int(sequence[1][12:]) > -1:
#         principal = int(sequence[1][12:])
#         c += 1
#     if sequence[2][:10] == '--periods=' and int(sequence[2][10:]) > -1:
#         periods = int(sequence[2][10:])
#         c += 1
#     if sequence[3][:11] == '--interest=' and float(sequence[3][11:]) > -1:
#         interest = float(sequence[3][11:]) / 1200
#         c += 1
#     if c == 3:
#         return True
#     else:
#         return False
#
# def an_check(sequence):
#     global principal, periods, payment, interest
#     a_p = 0
#     pr = 0
#     n = 0
#     # i didn't take possibility of several same parameters, i just hope there won't be it
#     # (i only thought up adding additional variables, but that's just too long)
#     for parameter in sequence:
#         if parameter[:len('--principal=')] == '--principal=':
#             principal = int(parameter[len('--principal='):])
#             a_p += 1
#             n += 1
#         if parameter[:len('--payment=')] == '--payment=':
#             payment = int(parameter[len('--payment='):])
#             pr += 1
#             n += 1
#         if parameter[:len('--periods=')] == '--periods=':
#             periods = int(parameter[len('--periods='):])
#             a_p += 1
#             pr += 1
#         if parameter[:len('--interest=')] == '--interest=':
#             interest = float(parameter[len('--interest='):]) / 1200
#             a_p += 1
#             pr += 1
#             n += 1
#     if a_p == 3:
#         return 'payment'
#     if pr == 3:
#         return  'principal'
#     if n == 3:
#         return 'period'
#     else:
#         return False
#
#
# args = sys.argv[1:]
# if args[0][7:] == 'diff':
#     if len(args) == 4:
#         if dif_check(args):
#             differentiated_payment(principal, periods, interest)
#         else:
#             print('Incorrect parameters')
#     else:
#         print('Incorrect parameters')
#
# elif args[0][7:] == 'annuity':
#     if len(args) == 4:
#         res = an_check(args)
#         if res == 'payment':
#             annuity_payment(principal, periods, interest)
#         elif res == 'principal':
#             annuity_principal(payment, periods, interest)
#         elif res == 'period':
#             annuity_periods(principal, payment, interest)
#         else:
#             print('Incorrect parameters')
#     else:
#         print('Incorrect parameters')
# else:
#     print('Incorrect parameters')
