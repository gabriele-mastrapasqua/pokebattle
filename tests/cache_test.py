import pytest
import time
from pokebattle.services.redisCache import RedisCache
from pokebattle.services.fakeCache import FakeCache

@pytest.fixture
def fake_cache():
    return FakeCache()

def test_fake_cache_set_get(fake_cache):
    fake_cache.set('test_key', 'test_value')
    result = fake_cache.get('test_key')
    assert result == 'test_value'

def test_fake_cache_delete(fake_cache):
    fake_cache.set('test_key', 'test_value')
    fake_cache.delete('test_key')
    result = fake_cache.get('test_key')
    assert result is None

def test_fake_cache_ttl(fake_cache):
    fake_cache.set('test_key', 'test_value')
    time.sleep(3)
    result = fake_cache.get('test_key')
    assert result is not None

if __name__ == "__main__":
    pytest.main()