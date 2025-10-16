import pytest

from product_class import Product
from core import get_avg_rating


class TestAnalysis:
    @pytest.fixture
    def sample_products(self):
        return [
            Product('Phone1', 'Apple', 1000, 4.5),
            Product('Phone2', 'Apple', 1200, 4.7),
            Product('Phone3', 'Samsung', 800, 4.3),
            Product('Phone4', 'Samsung', 900, 4.4),
            Product('Phone5', 'Xiaomi', 500, 4.2)
        ]

    def test_avg_ratings_calculation(self, sample_products):
        result = get_avg_rating(sample_products)

        assert 'Apple' in result
        assert 'Samsung' in result
        assert 'Xiaomi' in result

        # Apple: (4.5 + 4.7) / 2 = 4.6
        assert result['Apple'] == pytest.approx(4.6, 0.01)

        # Samsung: (4.3 + 4.4) / 2 = 4.35
        assert result['Samsung'] == pytest.approx(4.35, 0.01)

    def test_empty_products(self):
        """Тест пустого списка продуктов"""
        result = get_avg_rating([])
        assert result == {}