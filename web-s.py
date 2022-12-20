from bs4 import BeautifulSoup as bsoup
import requests as request
import time

def get_response(url):
    #get page content
    try:
        response = request.get(url, timeout=60)
        #make soup
        page_soup = bsoup(response.content, 'lxml')
        return page_soup

    except request.exceptions.ConnectTimeout:
        print('Server time out')
    except request.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            print('Page not found')
    except request.exceptions.ConnectionError:
        print('No internet connection')
        


if __name__ == '__main__':
    page_soup = get_response('https://en.wikipedia.org/wiki/Web_scraping')
    paragraph = page_soup.find('p').text

    with open('web-s.txt', 'a') as file:
        file.write(paragraph)