import pytest
import time
from main import param_for_test


def test_wait_timer():
    """
    Пауза
    """
    time.sleep(15)
    assert 1 == 1

def test_work():
    """
    Пауза
    """
    assert param_for_test == 100
