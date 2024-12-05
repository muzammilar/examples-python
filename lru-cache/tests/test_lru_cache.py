# tests/test_math_util.py
from unittest.mock import patch
import pytest
from app import LRUCache

# Test the add function
def test_no_capacity():
    cache = LRUCache(0)
    with pytest.raises(ValueError):
        cache.write(1,"test")

@patch('app.LRUCache._remove_oldest')
@patch('app.StorageObject.timestamp')
def test_basic_cache(rmv, ts):

    ts =4600
    cache = LRUCache(2)
    cache.write(1,"test1")
    rmv.assert_called_once()
    cache.write(2,"test2")
    assert cache.get(1) == "test1"
    assert cache.get(2) == "test2"


def test_cache_overflow():
    cache = LRUCache(2)

    cache.write(1,"test1")
    cache.write(2,"test2")
    cache.write(3,"test3")
    assert cache.get(1) == None
    assert cache.get(2) == "test2"
    assert cache.get(3) == "test3"

def test_get_nonexistent():
    cache = LRUCache(2)
    assert cache.get(1) == None
    cache.write(1,"test1")
    assert cache.get(1) == "test1"

def test_timestamp_iupdate():
    pass
