import requests
import os
from bs4 import BeautifulSoup
from zapis import write_to_file 


# Specify the URL of the website you want to scrape
url = 'https://stackoverflow.com/questions/24290358/remove-a-folder-from-git-tracking'

# Send a GET request to the URL
response = requests.get(url, verify=False)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information based on HTML tags and classes
    # For example, let's extract all the links on the page
    links = soup.find_all('a')

    # Print the extracted links
    for link in links:
        write_to_file(os.path.join(os.path.dirname(__file__), 'data','linki.txt'),str(link.get('href')),'a')
        #print(link.get('href'))
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")