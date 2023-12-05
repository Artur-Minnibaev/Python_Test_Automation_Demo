import requests
from fake_useragent import UserAgent

ua = UserAgent()

session = requests.Session()

headers = {
    'Accept': "application/json",
    'User-Agent': ua.random
}

url1 = 'https://demoqa.com/Account/v1/Login'
url2 = 'https://demoqa.com/BookStore/v1/Books'

data = {
    "userName": "test_test11",
    "password": "Test123!"
}


def log_in():
    """The process of obtaining information about books"""
    session.post(url=url2, data=data, headers=headers, allow_redirects=True)
    page_of_books = session.get(url=url2, headers=headers)

    with open(f'file.json', 'w') as file:
        file.write(page_of_books.text)
    return page_of_books


if __name__ == '__main__':
    log_in()
    print("[INFO] The file is ready!")
