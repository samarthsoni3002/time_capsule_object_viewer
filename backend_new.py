import os
import requests
from io import BytesIO
from PIL import Image
from urllib.parse import quote
from bs4 import BeautifulSoup




def futuristic_images(im):

    hi = im
    query = f'futuristic {im} images '
    num_images = 10


    url = f'https://www.bing.com/images/search?q={quote(query)}&form=HDRSC2&first=1&tsc=ImageBasicHover'


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_urls = [img.get('src') for img in soup.find_all('img', class_='mimg')]


    if not os.path.exists(f'{hi}_images'):
        os.makedirs(f'{hi}_images')


    for i in range(num_images):
        try:
            url = image_urls[i]
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            file_path = os.path.join(f'{hi}_images', f'{hi}_{i+1}.jpg')
            img.save(file_path)
            print(f'{file_path} downloaded successfully.')
        except Exception as e:
            print(f'Error downloading {url}: {e}')



def old_images(im):

    hi = im
    query = f'old {im} images '
    num_images = 10


    url = f'https://www.bing.com/images/search?q={quote(query)}&form=HDRSC2&first=1&tsc=ImageBasicHover'


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_urls = [img.get('src') for img in soup.find_all('img', class_='mimg')]


    if not os.path.exists(f'{hi}_images'):
        os.makedirs(f'{hi}_images')


    for i in range(num_images):
        try:
            url = image_urls[i]
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            file_path = os.path.join(f'{hi}_images', f'{hi}_{i+1}.jpg')
            img.save(file_path)
            print(f'{file_path} downloaded successfully.')
        except Exception as e:
            print(f'Error downloading {url}: {e}')

