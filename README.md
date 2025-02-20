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

2. Install required packages using any of these commands (if one doesn't work, try the next):
```bash
pip install requests
```
or
```bash
python -m pip install requests
```
or (for Python 3 specifically)
```bash
pip3 install requests
```

If you get a "pip not found" error:
- Make sure Python is installed correctly
- Ensure Python is added to your system's PATH environment variable
- You might need to install pip separately

3. Set up your Fixer.io API key:
   - Sign up at [Fixer.io](https://fixer.io/)
   - Replace the API key in the code with your own

## Common Installation Issues

If you see this error:
```
ModuleNotFoundError: No module named 'requests'
```
This means the requests library isn't installed. Use one of the pip install commands mentioned above.

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

## Project Structure

```
currency-exchange-converter/
│
├── currency_converter.py     # Main application file
├── conversion_history.txt    # Conversion history storage
├── requirements.txt         # Project dependencies
├── LICENSE                 # MIT License
└── README.md              # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- GUI interface
- Support for cryptocurrency conversions
- Historical exchange rate data
- Rate alerts and notifications
- Batch conversion support
- Export conversion history to CSV/Excel

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Fixer.io](https://fixer.io/) for providing exchange rate data
- All contributors and users of this project

## Author

[Your Name] - [Your Email]

## Support

For support, please:
1. Check the Common Installation Issues section above
2. Open an issue in the GitHub repository
3. Contact [your email]

## Version History

- 1.0.0
    - Initial Release
    - Basic currency conversion functionality
    - Conversion history tracking
