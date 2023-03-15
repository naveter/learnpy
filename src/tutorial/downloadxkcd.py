import bs4
import os
import requests

# It called from threads.py script

url = 'http://xkcd.com'     # starting url
os.makedirs('../../resource/xkcd', exist_ok=True)   # store comics in ./xkcd


def xkcd(start_comic, end_comic):
    for i in range(start_comic, end_comic):
        global url
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('Could not find comic image.')
        else:
            comic_url = comic_elem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % comic_url)
            res = requests.get('http:' + comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd
            image_file = open(os.path.join('../../resource/xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

        # Get the Prev button's url.
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prev_link.get('href')



