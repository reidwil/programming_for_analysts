import os
import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

logger = logging.getLogger(__name__)

# Specify the target URL here
url = 'http://thehorrorsofitall.blogspot.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find the middle container
middle_container = soup.find('div', class_='blog-posts hfeed')

img_tags = middle_container.find_all('img')
# Specify the download path
download_path = 'images/'

if not os.path.exists(download_path):
    os.makedirs(download_path)

for img in img_tags:
    img_url = img.get('src')

    # Check if the img_url is not None and is a JPEG image
    if img_url is not None and '/img/a/' in img_url:
        print(f"downloading {img_url}")
        # Complete the img_url if it's not complete
        img_url = urljoin(url, img_url)
            
        response = requests.get(img_url, stream=True)
        
        # Open a binary file and write to it
        with open(os.path.join(download_path, f"{img_url.split('=')[-1]}.jpg"), 'wb') as file:
            logger.info(f"writing to: {download_path}\image: {img_url}")
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)