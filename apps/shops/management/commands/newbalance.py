from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
import requests
from bs4 import BeautifulSoup

from apps.shops.models import Product


class Command(BaseCommand):
    help = _('Parse data from external source')
    base_url = 'https://www.example.com/men/shoes/all-shoes/'  # Замените на URL нужного магазина

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(_('Parsing starting!')))
        self.parse()
        self.stdout.write(self.style.SUCCESS(_('Parsing finished!')))

    def get_html(self, url):
        response = requests.get(url)
        return response.content

    def get_soup(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def parse(self):
        response = self.get_html(self.base_url)
        soup = self.get_soup(response)
        shoes_block = soup.find('div', {'class': 'shoes-block'})  # Замените на соответствующий селектор для блока с обувью

        if shoes_block:
            shoes_list = shoes_block.find_all('div', {'class': 'shoe-item'})  # Замените на соответствующий селектор для каждого товара
            for shoes in shoes_list:
                # Извлечение данных о товаре
                image_url = shoes.find('img', {'class': 'shoe-image'}).get('src')
                name = shoes.find('h3', {'class': 'shoe-name'}).get_text()
                price = shoes.find('span', {'class': 'shoe-price'}).get_text()
                description = shoes.find('p', {'class': 'shoe-description'}).get_text()

                # Создание и сохранение экземпляра Product
                product = Product()
                product.name = name
                product.price = price
                product.description = description

                # Сохранение фото обуви в модели Product
                image_content = self.get_html(image_url)
                product.image.save(f'{name}.jpg', image_content, save=True)

                product.save()
                self.stdout.write(self.style.SUCCESS(f'Saved product: {product}'))
        else:
            self.stdout.write(self.style.WARNING('No shoes found.'))


