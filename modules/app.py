from ecommerce.sales import Sales # import a modules from a directory acts as a package

sales = Sales(1000)
sales.show_profit()

import requests # importing a third party module to make HTTP requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("Response from API:", response.json()) # printing the response from the API in JSON format

# PyPI is the default package manager for Python and allows users to easily install and manage third-party libraries and packages. 
# PyPI hosts thousands of packages that can be installed using the pip command, which is included with Python installations.