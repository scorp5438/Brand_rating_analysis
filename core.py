import csv
from collections import defaultdict
from pathlib import Path

from product_class import Product


def get_full_path(file_names, path):
    return [Path().joinpath(path, file_name) for file_name in file_names]


def read_file(args):
    data_in_file = []
    for file in args:
        try:
            with open(file, 'r', newline='') as f:
                data = csv.DictReader(f, delimiter=';')
                data_in_file.extend([prod for prod in data])
        except FileNotFoundError:
            print(f'Файл {file} не найден')
    return data_in_file


def create_product_list(products) -> list[Product]:
    product_list = []
    for line in products:
        product = Product(
            name=line.get('name'),
            brand=line.get('brand'),
            price=float(line.get('price')),
            rating=float(line.get('rating'))
        )
        product_list.append(product)
    return product_list


def get_avg_rating(product_list):
    row_data = defaultdict(list)
    for prod in product_list:
        row_data[prod.brand].append(prod.rating)
    avg_rating = {
        brand: round(sum(value) / len(value), 2) for brand, value in row_data.items()
    }

    return dict(sorted(avg_rating.items(), key=lambda x: x[1], reverse=True))
