"""
Enhanced Currency Converter
This program converts between different currencies using real-time exchange rates from fixer.io API.
Features include currency conversion, conversion history, and a list of available currencies.
"""

import requests
import json
import sys
from typing import Tuple, Union, Dict
from datetime import datetime
from pathlib import Path
from decimal import Decimal

# List of available currencies with their descriptions
CURRENCIES = [
    "AED : Emirati Dirham,United Arab Emirates Dirham",
    "AFN : Afghan Afghani,Afghanistan Afghani",
    "ALL : Albanian Lek,Albania Lek",
    "AMD : Armenian Dram,Armenia Dram",
    "ANG : Dutch Guilder,Netherlands Antilles Guilder,Bonaire,Cura&#231;ao,Saba,Sint Eustatius,Sint Maarten",
    "AOA : Angolan Kwanza,Angola Kwanza",
    "ARS : Argentine Peso,Argentina Peso,Islas Malvinas",
    "AUD : Australian Dollar,Australia Dollar,Christmas Island,Cocos (Keeling) Islands,Norfolk Island,Ashmore and Cartier Islands,Australian Antarctic Territory,Coral Sea Islands,Heard Island,McDonald Islands,Kiribati,Nauru",
    "AWG : Aruban or Dutch Guilder,Aruba Guilder",
    "AZN : Azerbaijan Manat,Azerbaijan Manat",
    "BAM : Bosnian Convertible Mark,Bosnia and Herzegovina Convertible Mark",
    "BBD : Barbadian or Bajan Dollar,Barbados Dollar",
    "BDT : Bangladeshi Taka,Bangladesh Taka",
    "BGN : Bulgarian Lev,Bulgaria Lev",
    "BHD : Bahraini Dinar,Bahrain Dinar",
    "BIF : Burundian Franc,Burundi Franc",
    "BMD : Bermudian Dollar,Bermuda Dollar",
    "BND : Bruneian Dollar,Brunei Darussalam Dollar",
    "BOB : Bolivian Bol&#237;viano,Bolivia Bol&#237;viano",
    "BRL : Brazilian Real,Brazil Real",
    "BSD : Bahamian Dollar,Bahamas Dollar",
    "BTC : Bitcoin,BTC, XBT",
    "BTN : Bhutanese Ngultrum,Bhutan Ngultrum",
    "BWP : Botswana Pula,Botswana Pula",
    "BYN : Belarusian Ruble,Belarus Ruble",
    "BYR : Belarusian Ruble,Belarus Ruble",
    "BZD : Belizean Dollar,Belize Dollar",
    "CAD : Canadian Dollar,Canada Dollar",
    "CDF : Congolese Franc,Congo/Kinshasa Franc",
    "CHF : Swiss Franc,Switzerland Franc,Liechtenstein,Campione d&#039;Italia,B&#252;singen am Hochrhein",
    "CLF : Chilean Unit of Account",
    "CLP : Chilean Peso,Chile Peso",
    "CNY : Chinese Yuan Renminbi,China Yuan Renminbi",
    "COP : Colombian Peso,Colombia Peso",
    "CRC : Costa Rican Colon,Costa Rica Colon",
    "CUC : Cuban Convertible Peso,Cuba Convertible Peso",
    "CUP : Cuban Peso,Cuba Peso",
    "CVE : Cape Verdean Escudo,Cape Verde Escudo",
    "CZK : Czech Koruna,Czech Republic Koruna",
    "DJF : Djiboutian Franc,Djibouti Franc",
    "DKK : Danish Krone,Denmark Krone,Faroe Islands,Greenland",
    "DOP : Dominican Peso,Dominican Republic Peso",
    "DZD : Algerian Dinar,Algeria Dinar",
    "EGP : Egyptian Pound,Egypt Pound,Gaza Strip",
    "ERN : Eritrean Nakfa,Eritrea Nakfa",
    "ETB : Ethiopian Birr,Ethiopia Birr,Eritrea",
    "EUR : Euro,Euro Member Countries",
    "FJD : Fijian Dollar,Fiji Dollar",
    "FKP : Falkland Island Pound,Falkland Islands (Malvinas) Pound",
    "GBP : British Pound,United Kingdom Pound",
    "GEL : Georgian Lari,Georgia Lari",
    "GGP : Guernsey Pound,Guernsey Pound",
    "GHS : Ghanaian Cedi,Ghana Cedi",
    "GIP : Gibraltar Pound,Gibraltar Pound",
    "GMD : Gambian Dalasi,Gambia Dalasi",
    "GNF : Guinean Franc,Guinea Franc",
    "GTQ : Guatemalan Quetzal,Guatemala Quetzal",
    "GYD : Guyanese Dollar,Guyana Dollar",
    "HKD : Hong Kong Dollar,Hong Kong Dollar",
    "HNL : Honduran Lempira,Honduras Lempira",
    "HRK : Croatian Kuna,Croatia Kuna",
    "HTG : Haitian Gourde,Haiti Gourde",
    "HUF : Hungarian Forint,Hungary Forint",
    "IDR : Indonesian Rupiah,Indonesia Rupiah",
    "ILS : Israeli Shekel,Israel Shekel",
    "INR : Indian Rupee,India Rupee",
    "USD : US Dollar,United States Dollar",
]

class CurrencyConverter:
    def __init__(self):
        """Initialize the Currency Converter with API settings and data structures."""
        self.api_key = "33ec7c73f8a4eb6b9b5b5f95118b2275"  # Consider moving to environment variable
        self.api_url = "http://data.fixer.io/api/latest"
        self.history_file = Path("conversion_history.txt")
        self.rates = self._get_exchange_rates()
        self.currencies = self._parse_currencies()

    def _get_exchange_rates(self) -> Dict[str, float]:
        """Fetch current exchange rates from the API."""
        try:
            response = requests.get(
                self.api_url,
                params={"access_key": self.api_key},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            if not data.get("success"):
                raise ValueError(f"API Error: {data.get('error', {}).get('info', 'Unknown error')}")
            
            return data["rates"]
        except requests.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            sys.exit(1)

    def _parse_currencies(self) -> Dict[str, str]:
        """Parse the currency list into a more usable format."""
        currency_dict = {}
        for currency in CURRENCIES:
            code, description = currency.split(" : ", 1)
            currency_dict[code] = description
        return currency_dict

    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> Decimal:
        """Convert an amount between currencies."""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError(f"Invalid currency code: {from_currency} or {to_currency}")

        converted = Decimal(str(amount)) * Decimal(str(self.rates[to_currency])) / Decimal(str(self.rates[from_currency]))
        return round(converted, 2)

    def save_conversion(self, amount: float, from_currency: str, to_currency: str, result: Decimal):
        """Save conversion details to history file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"{timestamp}: {amount:.2f} {from_currency} = {result:.2f} {to_currency}\n"
        
        with open(self.history_file, "a", encoding="utf-8") as f:
            f.write(record)

    def display_history(self):
        """Display conversion history."""
        if not self.history_file.exists():
            print("\nNo conversion history available.")
            return

        print("\nConversion History:")
        print("-" * 50)
        with open(self.history_file, "r", encoding="utf-8") as f:
            print(f.read())

    def show_currencies(self):
        """Display available currencies."""
        print("\nAvailable Currencies:")
        print("-" * 50)
        for code, description in sorted(self.currencies.items()):
            print(f"{code}: {description}")

    def process_input(self):
        """Process user input and handle currency conversion."""
        while True:
            try:
                query = input("\nEnter amount from_currency to_currency (e.g., 100 USD EUR)\n"
                            "Commands: SHOW (list currencies), DISPLAY (show history), Q (quit)\n> ")

                if query.upper() == "Q":
                    print("Goodbye!")
                    break
                elif query.upper() == "SHOW":
                    self.show_currencies()
                    continue
                elif query.upper() == "DISPLAY":
                    self.display_history()
                    continue

                # Parse conversion request
                try:
                    amount_str, from_curr, to_curr = query.split()
                    amount = float(amount_str)
                    if amount <= 0:
                        raise ValueError("Amount must be positive")

                    result = self.convert_currency(amount, from_curr, to_curr)
                    self.save_conversion(amount, from_curr, to_curr, result)

                    print(f"\nResult: {amount:.2f} {from_curr.upper()} = {result:.2f} {to_curr.upper()}")
                    print(f"Rate: 1 {from_curr.upper()} = {(result/amount):.4f} {to_curr.upper()}")

                except ValueError as e:
                    print(f"\nError: {str(e)}")
                except Exception as e:
                    print(f"\nUnexpected error: {str(e)}")

            except KeyboardInterrupt:
                print("\nExiting...")
                break

def main():
    """Main entry point of the program."""
    print("\nCurrency Converter")
    print("-" * 50)
    print("Real-time currency conversion using current exchange rates")
    
    converter = CurrencyConverter()
    converter.process_input()

if __name__ == "__main__":
    main()
