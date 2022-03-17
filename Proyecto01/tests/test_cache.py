"""
Corre las pruebas unitarias necesarias para comprobar la correcta implementacion de 'cache.py'
@author MarioLetepichia
"""
import unittest
import sys
sys.path.append('src')
import cache

class TestCache(unittest.TestCase):
    def test_addValue(self):
        cache_a = cache.Cache()
        try:
            cache_a.addValue("HND",{'Country': 'Japan', 'City': 'Tokyo', 'Elevation': 35})
        except Exception: 
            raise  AssertionError
        else: 
            self.assertTrue(cache_a.getLength() == 1)
        try:
            cache_a.addValue("abcde", {'Country': 'Japan', 'City': 'Tokyo', 'Elevation': 35})
        except ValueError:
            pass
        else:
            self.assertFalse(cache_a.getLength() == 2)
        try:
            cache_a.addValue("HND", "cow")
        except TypeError:
            pass
        else:
            self.assertFalse(cache_a.getLength() == 2)
        try: 
            cache_a.addValue("KIM", {'Country': 'South Africa', 'City': 'Kimberley', 'Elevation':3950})
        except Exception:
            raise AssertionError
        else:
            self.assertTrue(cache_a.getLength() == 2)

    def test_updateCache(self):
        cache_b = cache.Cache()
        try:
            cache_b.updateCache("Cat")
        except TypeError:
            pass
        else:
            raise AssertionError
        try:
            cache_b.updateCache(Example.cache1.copy())
        except Exception:
            raise AssertionError
        self.assertTrue(cache_b.getLength() == 5)

    def test_clearCache(self):
        cache_c = cache.Cache()
        cache_c.updateCache(Example.cache1.copy())
        cache_c.clearCache()
        self.assertTrue(cache_c.getLength() == 0)

class Example:
    cache1 = {
        'HND': {'Country': 'Japan', 'City': 'Tokyo', 'Elevation': 35},
        'YLT': {'Country': 'Canada', 'City': 'Alert', 'Elevation': 100},
        'PUQ': {'Country': 'Chile', 'City': 'Punta Arenas', 'Elevation': 139},
        'KIM': {'Country': 'South Africa', 'City': 'Kimberley', 'Elevation':3950},
        'MAN': {'Country': 'United Kingdom', 'City': 'Manchester', 'Elevation': 257}
    }

if __name__ == '__main__':
    unittest.main()
    