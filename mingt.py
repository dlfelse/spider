import linecache
import logging
import os
from lxml import etree
import requests
from multiprocessing.dummy import Pool as ThreadPool
import base.tool

# Set the number of retries for requests
requests.adapters.DEFAULT_RETRIES = 5

# Set the User-Agent header for requests
headers = {
    'Connection': 'close',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
}

# Function to scrape the page links for a given category page
def get_page_links(link):
    try:
        # Send a GET request to the given link and parse the response
        response = requests.get(link, headers=headers, timeout=10)
        html = etree.HTML(response.text)

        # Extract the URLs of the pages from the response
        page_links = html.xpath('/html/body/div[1]/div/section/div//article/header/h1/a/@href')

        # Return the page links
        return page_links
    except:
        logging.debug(f'PageError: {link}')
        return []

# Function to scrape the image links for a given page
def get_image_links(link):
    try:
        # Send a GET request to the given link and parse the response
        response = requests.get(link, headers=headers, timeout=10)
        html = etree.HTML(response.text)

        # Extract the URLs of the images from the response
        image_links = html.xpath('/html/body/div[1]/div/div[1]/div/article/div/p//a/@href')

        # Return the image links
        return image_links
    except:
        logging.debug(f'UrlError: {link}')
        return []

# Function to download and save an image from a given link
def download_photo(link):
    try:
        # Send a GET request to the given link to download the image
        response = requests.get(link, headers=headers, timeout=3)
        response.raise_for_status()

        # Derive the filename from the URL
        filename = link[51:-13] + '.jpg'

        # Save the file to the specified directory
        with open(os.path.join('e:\pic\sy\ ', filename), 'wb') as f:
            f.write(response.content)

    except requests.exceptions.RequestException as e:
        # Log the error message
        logging.debug(f'{link} is wrong: {e}')


# Function to scrape the images for a given celebrity
def scrape_celebrity(celebrity_name):
    # Get the URLs of the pages in the given celebrity's category
    page_links = []
    for i in range(1, 7):
        link = f'http://www.mingtuiw.com/archives/tag/{celebrity_name}/page/{i}'
        page_links.extend(get_page_links(link))
        # Get the URLs of the images on each page
        image_links = []
        for page_link in page_links:
            link = f'http://www.mingtuiw.com{page_link}'
            image_links.extend(get_image_links(link))

        # Save the image links to a file
        with open(f'{celebrity_name}.txt', 'w', encoding='utf-8') as f:
            for image_link in image_links:
                f.write(f'http://www.mingtuiw.com{image_link}\n')

scrape_celebrity('宋轶')
# import linecache
#
# alinks = linecache.getlines('宋轶.txt')
# for al in alinks:
#     response = requests.get(al[:-1], headers=headers, timeout=10)
#     html = etree.HTML(response.text)
#
#     # Extract the URLs of the pages from the response
#     page_links = html.xpath('/html/body/div[1]/div/div/div/article/header/footer/a[1]/@href')
#     # Check if the page_links list is not empty
#     if len(page_links) > 0:
#         # Get the first page link
#         image_url = 'https://www.mingtuiw.com/' + page_links[0]
#         # Extract the filename from the URL using string slicing
#         filename = image_url[image_url.rfind('/') + 1:]
#         # Use the os.path.basename() function to extract the filename without the extension
#         image_name = os.path.basename(filename).split('.')[0]
#
#     # base.tool.downPhoto(image_url,'e:\pic\songyi\ ',image_name)
#     base.tool.download_image(image_url,'e:\pic\songyi',filename)