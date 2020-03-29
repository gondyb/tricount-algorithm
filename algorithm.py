# Data structure:
# Col 1 is to Benjamin, col 2 to Valentin, col 3 to Gaston
benjamin_debt = [0, 1000, 2000, 5000]
valentin_debt = [3000, 0, 9000, 4000]
gaston_debt = [7000, 3500, 0, 2000]
theo_debt = [1000, 3000, 2000, 0]

total_debt = [
    benjamin_debt,
    valentin_debt,
    gaston_debt,
    theo_debt
]

total_credit = [[0, 0, 0, 0] for x in range(len(total_debt))]

for i in range(0, len(total_debt)):
    debt = total_debt[i]
    for j in range(0, len(debt)):
        total_credit[j][i] += debt[j]

print("Total debt:")
print(total_debt)

print("Total credit:")
print(total_credit)

def compute_total_amount(debt, credit):
    return sum(debt) - sum(credit)

total_amount = [0 for x in range(len(total_debt))]

for i in range(len(total_debt)):
    total_amount[i] = compute_total_amount(total_debt[i], total_credit[i])

print("Total amount:")
print(total_amount)
print("\n")

def pay_recursive(amount):
    max_debt = max(amount)
    max_credit = min(amount)

    max_debitor = amount.index(max_debt)
    max_creditor = amount.index(max_credit)

    if (amount[max_debitor] == 0 and amount[max_creditor] == 0):
        return 0

    minimum = min(abs(amount[max_creditor]), abs(amount[max_debitor]))

    amount[max_creditor] += minimum
    amount[max_debitor] -= minimum

    print(max_debitor, " owes ", max_creditor, " ", minimum)

    pay_recursive(amount)

print("Algorithm start")
pay_recursive(total_amount)