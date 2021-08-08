import pytest
import test as ts

array = [5,3,4,2,1]
diccionario = [{"nombre":"Fernando","edad":23},{"nombre":"Ruben","edad":15},{"nombre":"Fernando","edad":43}]

def test():
    assert ar.ordenacion(array) == [1,2,3,4,5]

def test_conteo_may():
    assert ar.conteo_may(diccionario) == 2
