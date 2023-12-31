from ex24_solve import *



def add_test(urls):
    urls.add("/kiwi/", "Kiwi")
    urls.add("/apple/", "Apple")
    return urls

def exact_match_test(urls):
    assert urls.exact_match("/kiwi/") == "Kiwi"
    assert urls.exact_match("/apple/") == "Apple"
    assert urls.exact_match("/stuff/") == None
    for i in range(0, 500):
        urls.add(f'/banana/banananumber{i}/', f'Banana Number {i}')
    for i in range(0, 500):
        urls.exact_match(f'/banana/banananumber{i}/')

def best_match_test(urls):
    assert urls.best_match("/kiwi/user/1234/").value == "Kiwi"
    assert urls.best_match("/apple/user/2344/").value == "Apple"
    assert urls.best_match("NOTHING") == None

def match_all_test(urls):
    urls.add("/kiwikiwi/", "KiwiKiwi")
    all_matches = [n.value for n in urls.match_all("/kiwi")]
    assert all_matches == ["Kiwi", "KiwiKiwi"]

def match_shortest_test(urls):
    urls.add("/kiwikiwi/", "KiwiKiwi")
    assert urls.match_shortest("/k").value == "Kiwi"
    assert urls.match_shortest("/a").value == "Apple"

def match_longest_test(urls):
    urls.add("/kiwikiwi/", "KiwiKiwi")
    assert urls.match_longest("/k").value == "KiwiKiwi"
    assert urls.match_longest("/a").value == "Apple"

def all_tests(urls):
    add_test(urls)
    exact_match_test(urls)
    best_match_test(urls)
    match_all_test(urls)
    match_shortest_test(urls)
    match_longest_test(urls)

def test_TSTRouter():
    urls = TSTRouter()
    all_tests(urls)

def test_DictRouter():
    urls = DictRouter()
    all_tests(urls)

def test_BSTreeRouter():
    urls = BSTreeRouter()
    all_tests(urls)
for i in range(0, 100):
    test_TSTRouter()
    test_DictRouter()
    test_BSTreeRouter()

