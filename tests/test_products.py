import pytest

from core import create_product_list

class TestProduct:
    @pytest.fixture
    def sample_data(self):
        """Тестовые данные CSV"""
        return [
            {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
            {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
            {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
            {'name': 'iphone 14', 'brand': 'apple', 'price': '799', 'rating': '4.7'},
            {'name': 'galaxy a54', 'brand': 'samsung', 'price': '349', 'rating': '4.2'},
            {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'},
            {'name': 'iphone se', 'brand': 'apple', 'price': '429', 'rating': '4.1'},
            {'name': 'galaxy z flip 5', 'brand': 'samsung', 'price': '999', 'rating': '4.6'},
            {'name': 'redmi 10c', 'brand': 'xiaomi', 'price': '149', 'rating': '4.1'},
            {'name': 'iphone 13 mini', 'brand': 'apple', 'price': '599', 'rating': '4.5'}
        ]

    def test_create_products(self, sample_data):
        """Тест создания продуктов из данных"""
        products = create_product_list(sample_data)

        assert len(products) == 10
        assert products[0].name == 'iphone 15 pro'
        assert products[7].brand == 'samsung'
        assert products[9].rating == 4.5

    def test_empty_data(self):
        """Тест пустых данных"""
        products = create_product_list([])
        assert products == []