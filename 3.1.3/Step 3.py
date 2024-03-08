sandwich_type = ""
subtotal = 0.0

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwich_type = input("Sandwich Choice: ")

# Calculating Sandwich Price
if sandwich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif sandwich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25


beverage_choice = ""
subtotal = 0.0

beverage_size = ""

beverage_choice = input ("Would you like a beverage?")
if beverage_choice == "yes":
    print(" pick one small 1.00, medium 1.75, large 2.25")

    beverage_size = input("beverage size")
    if beverage_size == "small":
        print("you chose small, which will be 1.00")
        subtotal += 1.00
    elif beverage_size == "medium":
        print("you chose medium, which will be 1.75")
        subtotal += 1.75
    else:
        print ("you chose large which will be 2.25")
        subtotal += 2.25

fries_choice = ""
subtotal = 0.0

fries_size = ""

fries_choice = input ("would you like some fries?")
if fries_choice == "yes":
    print(" pick one small 1.00, medium 1.50, large 2.00")

    fries_size = input("fries size")
    if fries_size == "small":
        print("would you like to mega size")
