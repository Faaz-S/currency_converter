# currency_converter
The currency converter is a Python program that allows users to convert currencies between different countries. It uses real-time exchange rates to convert the input amount from one currency to another.
Features : 
    Real-time exchange rates fetched using an API
    User-friendly interface with input validation
    Conversion between multiple currencies supported
    Code structured with functions and modules
Technologies used :
    Python
    Requests module (for fetching exchange rates)
    Tkinter module (for GUI)
How to use :
    Clone the repository from GitHub to your local machine
    Install the required modules using pip: pip install -r requirements.txt
    Run the currency_converter.py file using Python: python currency_converter.py
    Enter the input currency, output currency, and amount to convert in the respective fields
    Click on the Convert button to see the converted amount
Code structure :
    currency_converter.py: Main program file that runs the GUI and calls the required functions
    currency_converter_functions.py: Contains functions for fetching exchange rates, converting currency, and input validation
    requirements.txt: Contains a list of required modules with their versions
Future improvements :
    Add support for more currencies
    Improve error handling and input validation
    Implement a caching mechanism for frequently used exchange rates
    
## To get an access key for the exchangeratesapi.io service, you can follow these steps:

    Go to the exchangeratesapi.io website at https://exchangeratesapi.io/
    Click on the "Get Free API Access" button in the top right corner of the page.
    Fill out the form with your email address and choose a password.
    After submitting the form, you should receive an email with a link to confirm your account.
    Follow the link to confirm your account, and you should be redirected to the API dashboard where you can find your access key.
    Once you have obtained your access key, you can replace the API_KEY constant in the convert_currency function with your own key to use the service.
