from ex15_stack import *

def test_push():
    books = Stack()
    books.push('physics book')
    books.push('cooking book')
    books.push('banana-looking book')
    assert books.pop() == 'banana-looking book'
    assert books.count() == 2
    books.pop()
    assert books.count() == 1
    books.push('super bananana')
    assert books.count() == 2
    assert books.topp() == 'super bananana'

    colors = Stack()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
def test_pop():
    books = Stack()
    for i in range(1, 5):
        books.push(f'book number {i}')
    for i in range(1, 5):
        j = 5-i
        assert books.topp() == f'book number {j}'
        books.pop()

    assert books.topp() == None

    colors = Stack()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None
def test_top():
    book = Stack()
    book.push('banana')
    assert book.topp() == 'banana'
    book.push('turtle')
    book.push('super banana')
    assert book.topp() == 'super banana'
    book.pop()
    assert book.topp() == 'turtle'
    colors = Stack()
    colors.push("Cadmium Red Light")
    assert colors.topp() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.topp() == "Hansa Yellow"
    colors.push("Pthalo Green")
    assert colors.topp() == "Pthalo Green"

def test_count():
    books = Stack()
    books.push('tolkien book')
    books.push('banana book')
    assert books.count() == 2
    books.pop()
    assert books.count() == 1
    books.push('super bananananana')
    assert books.count() == 2
    books.pop()
    books.pop()
    assert books.count() == 0


test_push()
test_pop()
test_top()
test_count()
