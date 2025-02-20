# Currency Exchange Converter

A powerful and accurate currency conversion tool that provides real-time exchange rates using the Fixer.io API. This Python-based application offers precise currency conversions with a clean command-line interface.

## Features

- Real-time exchange rates from Fixer.io API
- Support for 170+ global currencies
- Precise decimal-based calculations
- Conversion history tracking with timestamps
- User-friendly command-line interface
- Comprehensive error handling
- Detailed currency information and descriptions

## Requirements

- Python 3.7+
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/currency-exchange-converter.git
cd currency-exchange-converter
```

2. Install required packages:
```bash
pip install requests
```

3. Set up your Fixer.io API key:
   - Sign up at [Fixer.io](https://fixer.io/)
   - Replace the API key in the code with your own

## Usage

Run the program:
```bash
python currency_converter.py
```

### Commands:
- Convert currency: Enter amount and currency codes (e.g., `100 USD EUR`)
- Show available currencies: Type `SHOW`
- View conversion history: Type `DISPLAY`
- Quit the program: Type `Q`

Example:
```
Currency Converter
--------------------------------------------------
Enter amount from_currency to_currency (e.g., 100 USD EUR)
Commands: SHOW (list currencies), DISPLAY (show history), Q (quit)
> 100 USD EUR

Result: 100.00 USD = 91.85 EUR
Rate: 1 USD = 0.9185 EUR
```

## Features in Detail

1. **Real-time Exchange Rates**: 
   - Fetches current rates from Fixer.io API
   - Automatic rate updates with each conversion

2. **Accurate Calculations**: 
   - Uses Python's Decimal type for precise financial calculations
   - Avoids floating-point errors

3. **Conversion History**: 
   - Tracks all conversions with timestamps
   - Maintains a local history file

4. **Error Handling**: 
   - Comprehensive validation of user inputs
   - Network error handling
   - API error management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch 
3. Commit your changes
4. Push to the branch 
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Fixer.io](https://fixer.io/) for providing exchange rate data
- All contributors and users of this project

## Author

[Abhinav] - [raj316638@ggmail.com]

## Support

For support, please open an issue in the GitHub repository or contact [raj316638@gmail.com].
