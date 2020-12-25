# Hibike scraping for theHibikebot

import requests
from bs4 import BeautifulSoup as bs
import os

# Wesite with images
url = 'https://www.google.com/search?q=japon&rlz=1C1CHBF_frFR869FR869&sxsrf=ALeKk00VviaZDJd5Mn8TXmgtHD0WfxoRRw:1604776684542&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjL9-aBk_HsAhUFJhoKHU4KCGEQ_AUoA3oECAQQBQ&biw=1396&bih=657'


# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for hibike image
if not os.path.exists('HibikePic'):
    os.makedirs('HibikePic')

# move to new directory
os.chdir('HibikePic')

#image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('Hibike-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                print("Done Hibike", x)
                x += 1

    except:
        pass
