from bs4 import BeautifulSoup
import requests
import re

def extract_number(f):
    s = re.findall('\d$',f)
    return (int(s[0]) if s else -1,f)


url = 'http://file-repo/'
file_ext = 'gz'

## Get file List from URL ##
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
file_list = [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(file_ext)]
#print(file_list)

file_to_download = max(file_list,key=extract_number)

print(file_to_download)
