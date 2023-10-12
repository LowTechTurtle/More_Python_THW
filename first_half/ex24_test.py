from ex24 import *
from ex23_solve import *
from ex20_solve import *
from ex17_reimplement import *

def test_URLs(UDS):
    #UDS will be TSTRouter, BSTRouter,...
    urls = UDS()
    urls.add('/banana/', 'Banana')
    urls.add('/banana/turtle/superbanana/', 'Super Banana')
    urls.add('/paple/whatispaple/itsapplereverse', 'Apple')

    assert urls.get('/banana') == None
    assert urls.get_best('/banana/ramana/turlte') == ('/banana/', 'Banana')
    assert urls.get_best('/banana/turtle/whatisturtle') == ('/banana/', 'Banana')
    assert urls.get_best('/') == None
    assert urls.get_best('/banana/') == ('/banana/', 'Banana')
    urls.add('/paple/paple/ok/', 'Gud Paple')
    urls.add('/banana/averageturtle/', 'Avr Turtle')
    urls.add('/banana/paple/incrediblylongturtle/superlongthatimabouttovomit/longturtle', 'Long Turtle')
    assert urls.get_longest('/')[1] == 'Long Turtle'
    assert urls.get_shortest('/')[1] == 'Banana'
    assert urls.get_longest('/pap')[1] == 'Apple'
    assert urls.get_shortest('/papl')[1] == 'Gud Paple'
    assert urls.get('/superbananarama/') == None
    assert urls.get_best('/bananana/turtle/superturtle/superbanananana') == None
    assert urls.get_shortest('/bananan/turtle/wtf/asdasdasd/lkjsdgkasjgd') == None
    assert urls.get_longest('/supafuckingturtle/amazingturtle/theonetruelord') == None
    for i in range(0, 500):
        urls.add(f'/banana/banananumber{i}/', f'Banana Number {i}')
    for i in range(0, 500):
        urls.get(f'/banana/banananumber{i}/')
def test_URL_TST():
    test_URLs(TSTRouter)
def test_URL_BST():
    test_URLs(BSTRouter)
def test_URL_D():
    test_URLs(DRouter)
for i in range(0, 100):
    test_URL_TST()
    test_URL_BST()
    test_URL_D()
