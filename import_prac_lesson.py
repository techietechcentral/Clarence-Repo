# Calculate a groups shopping bills.
# How much would it cost for 5 people if each person needs:
#Assign the value to total
#Provide your answer as a printed variable called total.
#These prices do not include VAT. Calculate the VAT on the total, assuming that VAT is 20%.
#Then round it appropriately to two decimal places.

A = "A pack of tomatoes"
B = "3 washing sponges"
C = "A litre of juice"
D = "20m of foil"
E = "180g sugar"

import decimal
A = decimal.Decimal("0.67")
B = decimal.Decimal("2.70")
C = decimal.Decimal("1.75")
D = decimal.Decimal("3.00")
E = decimal.Decimal("1.15")

print("5 packs of tomatoes each costs = £", 5 * A)
F = 5 * A
print("5 packs of 3 washing sponges each costs = £", 5 * B)
G = 5 * B
print("5 packs of A litre of juice each costs = £", 5 * C)
H = 5 * C
print("5 packs of 20m of foil each costs = £", 5 * D)
I = 5 * D
print("5 packs of 180g sugar each costs = £", 5 * E)
J = 5 * E
total = A + B + C + D + E
print("Total (without VAT) = £",total)
print("Total (with 20% VAT)= £",decimal.Decimal("0.2") * (total) + total)
total_incl_vat = round(decimal.Decimal("0.2") * (total) + (total),2)
print("Round-up Total + 20% VAT)= £",(total_incl_vat))

def x():
    print("+--------------+-----------------+------------------+-----------------+")
    print("|   Quantity   |       Item      |    Unit cost     |    Total cost   |")
    print("+--------------+-----------------+------------------+-----------------+")
    print("|     5        |pack of Tomaotes |     0.67         |     ", F,"      |")
    print("+--------------+-----------------+------------------+-----------------+")
    print("|     5        |3x washing sponge|     2.70         |     ", G,"     |")
    print("+--------------+-----------------+------------------+-----------------+")
    print("|     5        |a litre of juice |     1.75         |     ", H,"      |")
    print("+--------------+-----------------+------------------+-----------------+")
    print("|     5        |20m foil         |     3.00         |     ", I,"     |")
    print("+--------------+-----------------+------------------+-----------------+")
    print("|     5        |180g of sugar    |     1.10         |     ", J,"      |")
    print("+--------------+-----------------+------------------+-----------------+")
    print("|              |            Grand Total(excl VAT)   |     ", total,"      |")
    print("+--------------+-----------------+------------------+-----------------+")
    print("|              |            Grand Total( + VAT)     |     ", total,"      |")
    print("+--------------+-----------------+------------------+-----------------+")

x()

print("-----------------------------------------------------------------------------")
""" The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of 
the try- and except blocks. """

try: 
    import decagon
    decagon()
    x = decagon()
    print(x)
except ModuleNotFoundError:
    print("Oops...it seems something went wrong.\nEnsure the module you are trying to import exists.")
else: 
    print ("Error")
