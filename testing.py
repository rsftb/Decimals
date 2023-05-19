import os
os.system("cls||clear") #..

from Decimals import Decimals


a = Decimals("234,2325375547563457824895627834623786473264789236478236478623784623789468836572")
b = Decimals("1,235343287467864235423546174789123891293")
c = a + b
print(c)

Decimals.set_separator('.')
c = a + b
print(c)


# For comparison
import decimal
decimal.getcontext().prec = 1000

a = decimal.Decimal("234.2325375547563457824895627834623786473264789236478236478623784623789468836572")
b = decimal.Decimal("1.235343287467864235423546174789123891293")
c = a + b
print(c)
