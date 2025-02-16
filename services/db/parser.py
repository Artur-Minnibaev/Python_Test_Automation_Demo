import requests
from fake_useragent import UserAgent

ua = UserAgent()
session = requests.Session()

headers = {
    'Accept': "application/json",
    'User-Agent': ua.random
}

url_books = 'https://demoqa.com/BookStore/v1/Books'


def log_in():
    """Getting a list of books in API json format and insert to the file.json"""
    response = session.get(url_books, headers=headers)

    if response.status_code == 200:
        with open("file.json", "w") as file:
            file.write(response.text)
        print("[PASS] JSON file crated!")
        return response
    else:
        print(f"[FAIL] Exception API: {response.status_code}, {response.text}")
        return None


if __name__ == '__main__':
    log_in()
