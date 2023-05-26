from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
import requests
from bs4 import BeautifulSoup

from apps.shops.models import Product


class Command(BaseCommand):
    help = _('Parse data from external source')
    base_url = 'https://www.newbalance.com/'

    def add_arguments(self, parser):
        parser.add_argument('--date', type=str, help=_('Date in format: YYYY-mm-dd'))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(_('Parsing starting!')))
        self.parse(options['date'])
        self.stdout.write(self.style.SUCCESS(_('Parsing finished!')))

    def get_html(self, url):
        response = requests.get(url)
        return response.content

    def get_soup(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def parse(self, date):
        response = self.get_html(f"{self.base_url}/?lable=8&date={date}&order=time")
        soup = self.get_soup(response)
        shoes_block = soup.find('div', {'class': 'pgptiles col-6 col-lg-4 px-1 px-lg-2'})
        
        shoes_list = shoes_block.find_all('div', {'class': 'product-tile-inner'})
        for shoes in shoes_list:
            product = Product()
            product.name = shoes.find('a', {'class': 'link font-weight-bold pname text-underline no-underline-lg'}).get_text()

        description = ""
        for text in shoes.find_all('text'):
            description += f"{text.text}\n"
        
        product.description = description.strip()
        
        product.price = shoes.find('span', {'class': 'sales font-body-large'}).get_text()
        product.save()
        
        self.stdout.write(self.style.SUCCESS(str(product)))
