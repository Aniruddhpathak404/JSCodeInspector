import re
import jsbeautifier
import esprima
import requests
import sys
import random
import time

class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'  # Red color escape sequence
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'



color_random = [colors.CBLUE, colors.CVIOLET, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,
                colors.CRED, colors.CBEIGE]
random.shuffle(color_random)

def entryy():
    x = color_random[0] + """
           
    
✅✅✅✅✅✅✅✅✅✅✅✅
✅✅✅✅✅✅✅✅✅✅✅✅
✅✅⬛⬛⬛✅✅⬛⬛⬛✅✅
✅✅⬛⬛⬛✅✅⬛⬛⬛✅✅
✅✅✅✅✅⬛⬛✅✅✅✅✅
✅✅✅⬛⬛⬛⬛⬛⬛✅✅✅
✅✅✅⬛⬛⬛⬛⬛⬛✅✅✅
✅✅✅⬛⬛✅✅⬛⬛✅✅✅
✅✅✅✅✅✅✅✅✅✅✅✅


\n"""
    for c in x:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.005)

entryy()

def fetch_js_code(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching JavaScript code from URL: {e}")
        return None

def extract_info(js_code):
    # Beautify the JavaScript code to make it more readable
    beautified_code = jsbeautifier.beautify(js_code)

    # Parse the JavaScript code into an Abstract Syntax Tree (AST)
    ast = esprima.parseScript(beautified_code)

    # Extract function names using regular expression
    function_names = re.findall(r'\bfunction\s+(\w+)\s*\(', beautified_code)

    # Extract variable names using regular expression
    variable_names = re.findall(r'\bvar\s+(\w+)(?:\s*=\s*[^;]+)?;', beautified_code)

    # Extract potential usernames
    usernames = re.findall(r'\b(?:user(?:name)?|login)\s*[:=]\s*[\'"]?([^\'";]+)', beautified_code)

    # Extract potential passwords
    passwords = re.findall(r'\b(?:pass(?:word)?|key)\s*[:=]\s*[\'"]?([^\'";]+)', beautified_code)

    # Extract version information
    versions = re.findall(r'\bversion\s*[:=]\s*[\'"]?([^\'";]+)', beautified_code)

    # Extract URLs
    urls = []
    api_keys = []
    for node in ast.body:
        if node.type == 'ExpressionStatement':
            if node.expression.type == 'AssignmentExpression':
                right_expr = node.expression.right
                if right_expr.type == 'Literal' and isinstance(right_expr.value, str):
                    value = right_expr.value
                    if 'http://' in value or 'https://' in value:
                        urls.append(value)
                    elif 'api_key' in node.expression.left.name.lower() or 'apikey' in node.expression.left.name.lower():
                        api_keys.append(value)

    return function_names, variable_names, usernames, passwords, versions, urls, api_keys

def main():
    url = input("Enter the URL of the JavaScript file: ")
    js_code = fetch_js_code(url)

    if js_code:
        function_names, variable_names, usernames, passwords, versions, urls, api_keys = extract_info(js_code)

        print("Extracted Function Names:")
        print(function_names)
        print("\nExtracted Variable Names:")
        print(variable_names)
        print("\nExtracted Usernames:")
        print(usernames)
        print("\nExtracted Passwords:")
        print(passwords)
        print("\nExtracted Versions:")
        print(versions)
        print("\nExtracted URLs:")
        print(urls)
        print("\nExtracted API Keys:")
        print(api_keys)

if __name__ == "__main__":
    main()
