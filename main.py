from bs4 import BeautifulSoup
import requests

html_file = requests.get('https://stackoverflow.com/questions/15115328/python-requests-no-connection-adapters').text
print(html_file)
