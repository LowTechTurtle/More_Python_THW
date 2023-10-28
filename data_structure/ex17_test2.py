from ex17 import Dictionary
from nose.tools import *
def test_states_and_cities():
    states = Dictionary()
    states.set('Oregon', 'OR')
    states.set('Florida', 'FL')
    states.set('California', 'CA')
    states.set('New York', 'NY')
    states.set('Michigan', 'MI')

    cities = Dictionary()
    cities.set('CA', 'San Francisco')
    cities.set('MI', 'Detroit')
    cities.set('FL', 'Jacksonville')
    cities.set('NY', 'New York')
    cities.set('OR', 'Portland')
    assert_equal(cities.get('NY'), 'New York')
    assert_equal(cities.get('OR'), 'Portland')
    assert_equal(states.get('Michigan'), 'MI')
    assert_equal(states.get('Florida'), 'FL')
    assert_equal(cities.get(states.get('Michigan')), 'Detroit')
    assert_equal(states.get('Texas'), None)
    assert_equal(cities.get('TX'), None)
    cities.delete('OR')
    assert_equal(cities.get('OR'), None)

test_states_and_cities()
