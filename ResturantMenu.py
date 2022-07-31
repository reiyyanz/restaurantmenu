#restaurant menu

#Lists for data validatation, to make sure user input can vary
yeslist = ['Yes', 'Y', 'y', 'yes', 'YES']
nolist = ['No', 'N', 'no', 'n', 'NO']
sandwichlist = ['Chicken', 'Beef', 'Tofu']
sizelist = ['Small', 'Medium', 'Large']
size = str('')

#questions to ask for sandwiches, fries, and drinks
sandwich = str(input("What type of sandwich do you want? (Chicken $5.25, Beef $6.25, Tofu $5.75): "))
while sandwich not in sandwichlist:
  sandwich = str(input("What type of sandwich do you want? (Chicken $5.25, Beef $6.25, Tofu $5.75): "))
if sandwich == 'Chicken':
  price = 5.25
  print("Your " + sandwich + " sandwich will cost $" + str(price) )
if sandwich == 'Beef':
  price = 6.25
  print("Your " + sandwich + " sandwich will cost $" + str(price) )
if sandwich == 'Tofu':
  price = 5.75
  print("Your " + sandwich + " sandwich will cost $" + str(price) )

drink = str(input("Would you like a drink? (Yes or No): "))
if drink in yeslist:
  size = str(input("What size would you like? (Small $1.00, Medium $1.75, Large $2.25): "))
  while not size in sizelist:
      size = str(input("What size would you like? (Small $1.00, Medium $1.75, Large $2.25): "))
  if size == 'Small':
    price = price + 1.00
    print("You chose a Small drink.")
  elif size == 'Medium':
    price = price + 1.75
    print("You chose a Medium drink.")
  elif size == 'Large':
    price = price + 2.25
    print("You chose a Large drink.")
if drink in nolist:
  print("You have choose no drink with your order.")
  size = str("No")

fries = str(input("Would you like fries with your order? (Yes or No): "))
if fries in yeslist:
  friesize = str(input("What size fries would like? (Small $1.00, Medium $1.50, Large $2.00): "))
  while not friesize in sizelist:
    friesize = str(input("What size fries would like? (Small $1.00, Medium $1.50, Large $2.00): "))
  if friesize == 'Small':
    friesQ1 = str(input("Would you like to Mega size your fries to Large? (Yes or No): "))
    if friesQ1 in nolist:
      print("You have selected Small fries" )
      price = price + 1.00
    if friesQ1 in yeslist:
      print("You have Mega sized your fries to Large")
      price = price + 2.00
    while not friesize in sizelist:
      friesize = str(input("What size fries would like? (Small $1.00, Medium $1.50, Large $2.00): "))
  if friesize == 'Medium':
    print("You have selected Medium fries")
    price = price + 1.50
  if friesize == 'Large':
    print("You have selected Large fries")
    price = price + 2.00
if fries in nolist:
  print("You have selected no fries with your order.")
  friesize = ("No")

#user gets to decide if they want ketchup, if they want multiple it will charge them $.25 for each
ketchup = str(input("Would you like ketchup with your order? (Yes or No): "))
if ketchup in yeslist:
  ketchupQ1 = str(input("How many ketchup packets would you like? ($.25 per packet), (Enter Quantity): "))
while not ketchupQ1.isnumeric():
  ketchupQ1 = str(input("How many ketchup packets would you like? ($.25 per packet), (Enter Quantity): "))

ketchuprice = int(ketchupQ1) * .25 
price = ketchuprice + price 

if ketchup in nolist:
  print("You have selected no ketchup packets with your order.")

#if the customer buys a drink and fries, they get a automatically applied $1 discount
if drink in yeslist and fries in yeslist:
  print( "\u001b[31m Hooray!, you qualified for a $1 Discount on this meal! (Auto Applied) \u001b[31m")
  price = price - 1.00

#States the final stats of the order and cost
print("You Ordered:") 
print("- " + sandwich + " sandwich") 
print("- " + size + " drink ") 
print("- " + friesize + " fries")
print("- " + str(ketchupQ1) + " ketchup packets" )

print("\u001b[32m Your total comes out $" + str(price))