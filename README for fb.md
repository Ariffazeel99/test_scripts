
# Facebook Login Test Script

This repository contains a simple test script to automate the login process on Facebook using Selenium and Python.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.x**: The script is written in Python.
- **Selenium**: A browser automation tool. Install it via pip:
  ```bash
  pip install selenium
  ```
- **WebDriver**: You need the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome). Make sure the WebDriver executable is in your system's PATH.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/facebook-login-test.git
   ```
2. Navigate to the project directory:
   ```bash
   cd facebook-login-test
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the appropriate WebDriver for your browser:
   - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
   - [GeckoDriver for Firefox](https://github.com/mozilla/geckodriver/releases)
   - [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
   
   Ensure the WebDriver is in your system's PATH.

## Usage

1. Open the script file `facebook_login_test.py`.

2. Replace the placeholder email and password in the script with your credentials:
   ```python
   email_field.send_keys("your_email@example.com")
   password_field.send_keys("your_password")
   ```

3. Run the script:
   ```bash
   python facebook_login_test.py
   ```

4. The script will launch a browser window, navigate to Facebook, enter the login credentials, and attempt to log in.

5. The output will indicate whether the login was successful or failed.

## Important Notes

- **Credentials Security**: For security reasons, do not hardcode your credentials in the script. Consider using environment variables or secure storage solutions for handling sensitive information.
- **Compliance**: Automating interactions with Facebook may violate their Terms of Service. Use this script responsibly and only for educational purposes.
- **Dynamic Elements**: Facebook's UI may change over time, so the script may require updates to the element locators.

## Contributing

If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
