MENU = {
    "e": {
        "ingredients":
            {
                "water": 50,
                "coffee": 18
            },
        "cost": 1.5,
    },
    "l": {
        "ingredients":
            {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
        "cost": 2.5,
    },
    "c": {
        "ingredients":
            {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

income = 0
# TODO: Check for Available Resources
def resources_check(choice):
    for items in MENU[choice]["ingredients"]:
        if resources[items] < MENU[choice]["ingredients"][items]:
            print(f"insufuciaent {items} ")
            return False


# TODO: Money Counting
def payment(choice):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input('How many "Quarters" do you have : ')) * 0.25
    dimes = int(input('How many "Dimes" do you have : ')) * 0.10
    nickles = int(input('How many "Nickles" do you have : ')) * 0.05
    pennies = int(input('How many "Pennies" do you have : ')) * 0.01
    total = (quarters + dimes + nickles + pennies)
    if total >= MENU[choice]["cost"]:
        print(f'Here is $ {round(total - MENU[choice]["cost"], 3)} in change')
        return total
    elif input(f"You have only ${total}, Insufficient funds for option - {choice.upper()} ,  Try again Y/N").lower() == 'y':
        payment(choice)
    else:
        coffee_machine(income)
    return total

#TODO: Coffee Machine Codes

def coffee_machine(income):
    choice = input("Please place your order - (E)spresso / (L)atte / (C)appuccino : ").lower()
# TODO: Print the total Income
    if choice =='income':
        print(f"Total income is : {income}")
# TODO: Print the Report
    elif choice == 'report':
        print("\nAvailable Ingredients:")
        for items in resources:
            print(f"{items} : {resources[items]}")
# TODO: Power off the machine
    elif choice == 'off':
        exit("\n!!! Machine Powered off for maintenance !!!")
        return 440

    elif choice == 'e' or choice == 'l' or choice == 'c':
        income += MENU[choice]["cost"]
        if resources_check(choice) == False:
            print('Please choose another Item')
        else:
            payment(choice)
            print("Here is yout Drink ☕️ ")
            for items in MENU[choice]["ingredients"]:
                resources[items] -= MENU[choice]["ingredients"][items]
    else:
        print("Please choose correct item !!!")


    coffee_machine(income)

coffee_machine(income)
