# function to calculate options-related metrics
def options_calc():
    # Prompt user for input values related to options trading
    bc = input("Please enter the strike price of your long call:\n")
    sc = input("Please enter the strike price of your short call:\n")
    bc_price = input("Please enter the value of the long call:\n")
    sc_price = input("Please enter the value of the short call:\n")

    try:
        # Attempt to convert user inputs to floating-point numbers
        bc = float(bc)
        sc = float(sc)
        bc_price = float(bc_price)
        sc_price = float(sc_price)

        # Check if the inputs are indeed floating-point numbers
        if isinstance(bc, float) and isinstance(sc, float) and isinstance(bc_price, float) and isinstance(sc_price, float):
            # Calculate the intrinsic value of the options position
            m_sc = sc - bc
            print(f"The intrinsic value of your position is ${m_sc}.\nThis is the amount you would get if you were to get assigned early.")
            print("-----------")

            # Calculate the value of the long call minus the Premium received
            xp = bc_price - sc_price
            print(f"${xp} is the current value of your long call minus the Premium received.")
            print("---------------")

            # Calculate the break-even point
            break_even = bc_price - m_sc
            print(f"Break-even point: ${break_even} This is how much premium you would need to cover to break even if you get assigned early.")
            print(f"Collect Premiums regularly to cover this.")
            print("------------")

            # Calculate potential monthly premiums from short calls
            sc_regular = sc_price * 4
            print(f"If you can collect ${sc_price} 4 times a month you would net ${sc_regular} in premium collected a month.")
            print("------------------------")

            # Calculate the potential profit from premiums
            pt_sc = sc_regular - break_even
            if pt_sc > 0:
                print(f"By offsetting the break-even price you need to cover, by providing a profit of ${pt_sc} in premium a month.")
            else:
                print("you will not break even or make a profit this month.")
        else:
            # If inputs are not floating-point numbers, prompt for valid inputs
            print("Please enter valid integers for prices")
    except ValueError:
        # Handle the case where user inputs are not valid numbers
        print("Please enter valid numbers")


# Call the function to execute the options calculation
options_calc()
