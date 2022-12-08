import os
import requests

import tool

# Set the maximum number of retries for requests
requests.adapters.DEFAULT_RETRIES = 5
# Define the path to the directory where the images will be saved
folder_name = 'e:\\pic\\美女目录'
subfolder_name = 'heijiajia'
path = os.path.join(folder_name, subfolder_name)

# Get a list of URLs to the pages on the website
page_urls = tool.getAllPages('https://www.girldir.com/photos/' + subfolder_name + '_list/?page=', 1, 2)

# Iterate over the page URLs
for page_url in page_urls:
    # Get the image URLs from the page
    image_urls = tool.getTarget(page_url, '/html/body/div[3]/div/div/div[2]//div/a/@href')
    # Check if the image_urls list is not empty
    if len(image_urls) > 0:
        for image_url in image_urls:
            # Get the full URL to the image
            image_url = 'https://www.girldir.com' + image_url
            # Get the image URLs from the page
            image_urls = tool.getTarget(image_url, '/html/body/div[3]/div[2]/div[1]/div[3]/a/picture/source/@srcset')
            # Check if the image_urls list is not empty
            if len(image_urls) > 0:
                for image_url in image_urls:
                    # Remove the last 36 characters from the image URL
                    image_url = image_url[:-36]
                    # Extract the file name from the image URL
                    image_name = image_url.split('/')[-1]
                    tool.download_image(image_url,path,image_name)
