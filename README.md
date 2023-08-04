# JSCodeInspector

JSCodeInspector is a Python tool designed to extract important information from JavaScript files. It provides a convenient way to analyze JavaScript code and identify potential function names, variable names, usernames, passwords, version information, URLs, and API keys.

## Features

- Extract function names from JavaScript code.
- Identify variable names used in the code.
- Find potential usernames and passwords.
- Detect version information used in the code.
- Extract URLs and API keys, if present.


![Screenshot_2023-08-04_17_19_43](https://github.com/Aniruddhpathak404/JSCodeInspector/assets/101852962/8409d479-8958-493d-a37c-642981b9b6f8)
![Screenshot_2023-08-04_17_20_14](https://github.com/Aniruddhpathak404/JSCodeInspector/assets/101852962/dc1862b9-50fb-4a98-b01f-ddd31996afc3)


## Requirements

To use the JSCodeInspector tool, you need to have the following libraries installed:

- jsbeautifier
- esprima
- requests

You can install the required libraries using the following command:

```bash
pip install jsbeautifier esprima requests

Usage

    Clone the repository to your local machine:



git clone https://github.com/yourusername/JSCodeInspector.git
cd JSCodeInspector

    Run the script JSCodeInspector.py:



python JSCodeInspector.py

    The tool will prompt you to enter the URL of the JavaScript file you want to analyze.

    After providing the URL, the script will fetch the JavaScript code, inspect it, and display the extracted information, including function names, variable names, usernames, passwords, version information, URLs, and API keys.



Legal Disclaimer

Please note that using this tool on any JavaScript file without proper authorization may be illegal and unethical. Always ensure you have explicit permission from the file owner to analyze the JavaScript code. The tool is provided for educational and ethical purposes only.
Contributions

Contributions to the JSCodeInspector tool are welcome! If you find any bugs or want to add new features, feel free to create a pull request. For major changes, please open an issue first to discuss the proposed changes.


