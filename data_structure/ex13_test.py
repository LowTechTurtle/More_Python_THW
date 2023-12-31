from ex13 import *

def test_push():
    colors = SingleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.push("Ultramarine Violet")
    assert colors.count() == 3

def test_pop():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

def test_unshift():
    colors = SingleLinkedList()
    colors.push('Viridian')
    colors.push('Sap Green')
    colors.push('Van Dyke')
    assert colors.unshift() == 'Viridian'
    assert colors.unshift() == 'Sap Green'
    assert colors.unshift() == 'Van Dyke'
    assert colors.unshift() == None

def test_remove():
    colors = SingleLinkedList()
    colors.push('Cobalt')
    colors.push('Zinc White')
    colors.push('Nickle Yellow')
    colors.push('Perinone')
    assert colors.remove('Cobalt') == 0
    assert colors.remove('Perinone') == 2
    assert colors.remove('Nickle Yellow') == 1
    assert colors.remove('Zinc White') == 0

def test_first():
    colors = SingleLinkedList()
    colors.push('Red')
    assert colors.first() == 'Red'
    colors.push('Hansa Yellow')
    assert colors.first() == 'Red'
    colors.shift('Green')
    assert colors.first() == 'Green'

def test_last():
    colors = SingleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Hansa Yellow"

def test_get():
    colors = SingleLinkedList()
    colors.push("Ver")
    assert colors.get(0) == "Ver"
    colors.push("Sap Green")
    assert colors.get(0) == "Ver"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get(0) == "Ver"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Ver"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Ver"
    colors.pop()
    assert colors.get(0) == None
def test_shift():
    colors = SingleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1
    colors.shift("Carbazole Violet")
    assert colors.count() == 2
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 1
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 0
test_push()
test_pop()
test_remove()
test_first()
test_last()
test_unshift()
test_shift()
test_get()













