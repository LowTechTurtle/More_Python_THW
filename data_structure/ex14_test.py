from ex14 import *

def test_push():
    colors = DLL()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.push("Ultramarine Violet")
    assert colors.count() == 3
    colors.invariants()

def test_pop():
    colors = DLL()
    colors.invariants()
    colors.push("Magenta")
    colors.push("Alizarin")
    colors.invariants()
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    colors.invariants()
    assert colors.pop() == None
    colors.invariants()

def test_unshift():
    colors = DLL()
    colors.push('Viridian')
    colors.push('Sap Green')
    colors.invariants()
    colors.push('Van Dyke')
    colors.invariants()
    assert colors.unshift() == 'Viridian'
    assert colors.unshift() == 'Sap Green'
    colors.invariants()
    assert colors.unshift() == 'Van Dyke'
    assert colors.unshift() == None
    colors.invariants()

def test_remove():
    colors = DLL()
    colors.push('Cobalt')
    colors.invariants()
    colors.push('Zinc White')
    colors.push('Nickle Yellow')
    colors.push('Perinone')
    colors.invariants()
    assert colors.remove('Cobalt') == 0
    assert colors.remove('Perinone') == 2
    assert colors.remove('Nickle Yellow') == 1
    colors.invariants()
    assert colors.remove('Zinc White') == 0

def test_first():
    colors = DLL()
    colors.push('Red')
    assert colors.first() == 'Red'
    colors.push('Hansa Yellow')
    colors.invariants()
    assert colors.first() == 'Red'
    colors.shift('Green')
    assert colors.first() == 'Green'
    colors.invariants()

def test_last():
    colors = DLL()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.invariants()
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    colors.invariants()
    assert colors.last() == "Hansa Yellow"

def test_get():
    colors = DLL()
    colors.push("Ver")
    assert colors.get(0) == "Ver"
    colors.invariants()
    colors.push("Sap Green")
    assert colors.get(0) == "Ver"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    colors.invariants()
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
    colors.invariants()
def test_shift():
    colors = DLL()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1
    colors.invariants()
    colors.shift("Carbazole Violet")
    assert colors.count() == 2
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 1
    colors.invariants()
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 0
    colors.invariants()
test_push()
test_pop()
test_remove()
test_first()
test_last()
test_unshift()
test_shift()
test_get()













