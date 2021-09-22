## This script output the latest file version located on a website
## This script will fetch all files in the following format "bigdata-<number>.<number>.<number>.tar"
# 1. list all the files on a website
# 2. Using regex extract the version
# 3. Print the latest version

from bs4 import BeautifulSoup
import requests
import re

url = 'http://1.1.1.1/project/release-1/' # The url that holds the files
file_ext = 'tar' # Define the file extantion that should be process
filname_match_regex_start = 'bigdata-' #
filname_match_regex_end = '.tar'

def max_file_list(file_list):
    version_number = 0
    file_to_download = 'd'
    for file in file_list:
        extract_version_number = re.search(filname_match_regex_start + '(.+?)' + filname_match_regex_end, file)
        # print(extract_version_number.group(1))
        extract_version_number_int = int(extract_version_number.group(1).replace('.', ''))
        higher_version = max(version_number, extract_version_number_int)
        if higher_version > version_number:
            version_number = higher_version
            file_to_download = file
    return file_to_download


## Get file List from URL ##
page = requests.get(url).text
#print (page)
soup = BeautifulSoup(page, 'html.parser')
#print (soup)
file_list = [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(file_ext)]
#print(file_list)

max_file_list(file_list)
