from ex23 import *
def test_TSTree_get_set():
    urls = TSTree()
    urls.set('/apple/', 'Apple')
    urls.set('/grape/', 'Grape')
    urls.set('/kiwi/', 'Kiwi')
    urls.set('/kumquat/', 'Kumquat')
    urls.set('/pineapple/', 'Pineapple')
    urls.set('/sick/', 'Sick')
    urls.set('/sina/', 'Sina')

    assert urls.get('/sick/') == 'Sick' 
    assert urls.get('/apple/') == 'Apple'
    assert urls.get('/kumquat/') == 'Kumquat'
    assert urls.get('/grape/') == 'Grape'
    assert urls.get('/pineapple') == None
    assert urls.get('/pineapple/') == 'Pineapple'
    assert urls.get('/') == None
    assert urls.get('/kiwi///') == None
    assert urls.get('/kiwi/') == 'Kiwi'
    return urls
    
def test_TSTree_find_all():
    urls = test_TSTree_get_set()
    results = [n.value for n in urls.find_all('/k')]
    assert results == ['Kiwi', 'Kumquat']

def test_TSTree_find_shortest():
    urls = test_TSTree_get_set()
    urls.set('/kiwiki/', 'Kiwiki')
    urls.set('/kiwikiwi/', 'Kiwikiwi')
    assert urls.find_shortest('/k').value == 'Kiwi'
    urls.set('/kiw/', 'Kiw')
    assert urls.find_shortest('/k').value == 'Kiw'
    assert urls.find_shortest('/').value == 'Kiw'
    assert urls.find_shortest('/a').value == 'Apple'
    assert urls.find_shortest('/kiwik').value == 'Kiwiki'
    return urls

def test_TSTree_find_longest():
    urls = test_TSTree_find_shortest()
    assert urls.find_longest('/ki').value == 'Kiwikiwi'
    assert urls.find_longest('/').value == 'Pineapple'

def test_TSTree_find_part():
    urls = test_TSTree_get_set()
    assert urls.find_part('/kabababa').value == 'Kiwi'
    assert urls.find_part('/application/').value == 'Apple'
    assert urls.find_part('/paple').value == 'Pineapple'
    assert urls.find_part("/apple/120/1000/").value == "Apple"
    assert urls.find_part("/kiwi/user/zedshaw/has/stuff").value == "Kiwi"
    assert urls.find_part("XTREEME") == None

test_TSTree_find_shortest()
test_TSTree_find_longest()
