import requests
from bs4 import BeautifulSoup


def check_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Good"
        else:
            return "Broken"
    except requests.exceptions.RequestException:
        return "Broken"


def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    return [link.get("href") for link in links]


def main():
    url = input("Enter the URL of a web page: ")
    links = get_links(url)
    for link in links:
        status = check_link(link)
        print(f"Link: {link} - {status}")


if __name__ == "__main__":
    main()
