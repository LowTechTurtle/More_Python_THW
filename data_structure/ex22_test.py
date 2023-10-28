from ex22 import *
def test_SA():
    word = SuffixArray('abracadabra')
    assert word.find_all('abra') == ['abra', 'abracadabra']
    assert word.find_longest('abra') == 'abracadabra'
    assert word.find_shortest('abra') == 'abra'
    assert word.find_all('a') == ['a', 'abra', 'abracadabra', 'acadabra', 'adabra']
    assert word.find_all('br') == ['bra', 'bracadabra']
    assert word.find_longest('br') == 'bracadabra'
    assert word.find_shortest('br') == 'bra'
for i in range(0, 500):
    test_SA()
