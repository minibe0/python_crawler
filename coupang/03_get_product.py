from libs.stringGetter import getPageString
from bs4 import BeautifulSoup
from libs.coupang.productsParser import getProducts

url = "https://www.coupang.com/np/categories/186764?page=2"
pageString = getPageString(url)
products = getProducts(pageString)
