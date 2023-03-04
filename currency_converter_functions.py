def validate_input(input_currency, output_currency, amount):
    """
    Validates the user input for currency conversion.
    """
    if not input_currency:
        print("Please enter an input currency.")
        return False
    if not output_currency:
        print("Please enter an output currency.")
        return False
    if not amount:
        print("Please enter an amount.")
        return False
    try:
        float(amount)
    except ValueError:
        print("Please enter a valid amount.")
        return False
    return True






