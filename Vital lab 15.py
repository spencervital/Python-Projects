
import sys
import threading
from bs4 import BeautifulSoup
import time

# Check if required modules are installed
try:
    import webbrowser
    import sys
    import requests
except ImportError:
    print("Required modules are not installed.")
    sys.exit(1)

# Download and install the BS4 module if not already installed
try:
    import bs4
except ImportError:
    print("Downloading and installing BS4...")
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
        print("BS4 successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install BS4.")
        sys.exit(1)

# Function to download images from a website
def download_images(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            image_url = image.get('src')
            if image_url.startswith('http'):
                image_data = requests.get(image_url).content
                with open(f'image_{time.time()}.jpg', 'wb') as f:
                    f.write(image_data)
        print("Images downloaded successfully.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while downloading images:", str(e))

# Function to parse website using BS4
def parse_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title')
        images = soup.find_all('img')
        timestamps = soup.find_all('time')
        links = soup.find_all('a')
        videos = soup.find_all('video')

        print("Title:", title.text if title else "Not found")
        print("Images:", len(images))
        print("Timestamps:", len(timestamps))
        print("Links:", len(links))
        print("Videos:", len(videos))

    except requests.exceptions.RequestException as e:
        print("Error occurred while parsing website:", str(e))

# Main program
if __name__ == '__main__':
    # Get the URLs for the websites
    url1 = input("Enter URL for website 1: ")
    url2 = input("Enter URL for website 2: ")

    # Schedule launching of threads
    thread1 = threading.Timer(180, download_images, args=(url1,))
    thread1.start()

    thread2 = threading.Timer(300, parse_website, args=(url2,))
    thread2.start()
