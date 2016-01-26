# Annual credit card interest and balance calculator

# Just alter example numbers for following three variables (0.2 = 22%, 0.04 = 2%)

balance = 3242
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Initializes months and running total

month = 1
totalPaid = 0

while month < 13:
  print 'Month: ' + str(month)
  minimum_monthly_payment = (monthlyPaymentRate * balance)
  balance = (balance - (balance * monthlyPaymentRate)) * (1 + (annualInterestRate / 12))
  print 'Minimum monthly payment: ' + str(round(minimum_monthly_payment, 2))
  print 'Remaining balance: ' + str(round(balance, 2))
  month += 1
  totalPaid += minimum_monthly_payment
  print 'Total paid: ' + str(round(totalPaid, 2))

