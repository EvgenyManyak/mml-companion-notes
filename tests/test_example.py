"""
Пример тестового файла.
Запустите тесты командой: pytest tests/
"""

import numpy as np


def test_numpy_import():
    """Проверка, что NumPy доступен."""
    assert np is not None


def test_basic_array():
    """Пример базового теста."""
    a = np.array([1, 2, 3])
    assert a.sum() == 6
