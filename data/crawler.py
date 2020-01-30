import requests
from lxml import html

url = r'https://bnonews.com/index.php/2020/01/the-latest-coronavirus-cases/'
page=requests.Session().get(url)
tree=html.fromstring(page.text)
result=tree.xpath('//table[@class="wp-block-table alignenter is-style-stripes"]//tbody//tr//td//strong/text()')

print(result)