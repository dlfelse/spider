import linecache
import logging
import os
import you_get
import requests
from lxml import etree

proxies = {"http": "socks5://127.0.0.1:10808","https": "socks5://127.0.0.1:10808"}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}

def getProxies():
    return proxies

def getHeaders():
    return headers

def downVideo(url, path):
    # 使用 you_get.download() 方法来下载视频
    you_get.download(url, output_dir=path)

def download_image(image_url, save_path, image_name):
    try:
        # Send a GET request to the given URL to download the image
        response = requests.get(image_url, headers=headers, timeout=3)
        response.raise_for_status()

        # Create the save_path folder if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        # Save the image to the specified path and name
        with open(os.path.join(save_path, image_name), 'wb') as f:
            f.write(response.content)

    except requests.exceptions.RequestException as e:
        # Log the error message
        logging.debug(f'{image_url} is wrong: {e}')





# Define the function to get the target elements from a page
def getTarget(url, xpath):
    # Initialize an empty list to store the elements
    elements = []
    # Try to send a GET request to the given URL and extract the elements using the given XPath
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=6)
        # Parse the HTML content of the page
        html = etree.HTML(response.text)
        # Close the response object
        response.close()
        # Extract the elements using the given XPath
        elements = html.xpath(xpath)
    # Catch any exceptions that may occur and log them
    except Exception as e:
        print(f'Error while getting elements from {url}: {e}')
    # Return the list of elements
    return elements




# 定义下载视频的函数


# 页面 URL，开始页数，结束页数
def getAllPages(url, j, k):
    # 使用 range() 函数生成页数列表
    pages = range(j, k + 1)
    # 使用 map() 函数拼接基础 URL 和页数来生成完整的 URL
    links = map(lambda x: url + str(x), pages)
    # 返回生成的 URL 列表
    return list(links)


# Define the function to write the strings to a file
def writetotxt(filename, string):
    # Try to open the file in append mode and write the given string to it
    try:
        # Open the file in append mode
        with open(filename, 'a', encoding='utf-8') as file:
            # Write the string to the file, adding a newline character at the end
            file.write(string + '\n')
    # Catch any exceptions that may occur and log them
    except Exception as e:
        print(f'Error while writing to file {filename}: {e}')




# Define the function to get the strings from a file
def getStrFromText(filename):
    # Initialize an empty list to store the strings
    strings = []
    # Try to read the lines from the file and store them in the list
    try:
        # Read the lines from the file
        lines = linecache.getlines(filename)
        # Iterate over the lines and store them in the list
        for line in lines:
            # Append the line to the list, removing the newline character at the end
            strings.append(line.strip())
    # Catch any exceptions that may occur and log them
    except Exception as e:
        print(f'Error while reading file {filename}: {e}')
    # Return the list of strings
    return strings
