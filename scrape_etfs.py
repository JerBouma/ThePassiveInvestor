import requests
import lxml
from lxml import html
import pandas as pd

def symbol_collector(url="https://finance.yahoo.com/etfs"):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    table = tree.xpath('//table')
    symbol = pd.read_html(lxml.etree.tostring(table[0], method='html'))[0]['Symbol'].to_list()

    return symbol
