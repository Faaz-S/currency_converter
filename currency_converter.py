import requests
from currency_converter_functions import validate_input

API_URL = "https://api.exchangeratesapi.io/latest"
API_KEY = "yfifeTfSlGsUZqENNpRmcrzsLnPHD8qk"


def convert_currency(input_currency, output_currency, amount):
    """
    Converts an amount from one currency to another.
    """
    params = {
        "base": input_currency,
        "symbols": output_currency
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(API_URL, params=params, headers=headers)
    data = response.json()
    if "error" in data:
        print(f"Error: {data['error']}")
        return
    rate = data["rates"].get(output_currency)
    if not rate:
        print("Invalid currency!")
        return
    converted_amount = amount * rate
    print(f"{amount} {input_currency} = {converted_amount} {output_currency}")

if __name__ == "__main__":
    input_currency = input("Enter input currency: ")
    output_currency = input("Enter output currency: ")
    amount = input("Enter amount: ")

    if validate_input(input_currency, output_currency, amount):
        amount = float(amount)
        convert_currency(input_currency.upper(), output_currency.upper(), amount)
