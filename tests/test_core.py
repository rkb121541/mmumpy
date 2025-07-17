import mmumpy as mm

def test_transpose():
    assert mm.transpose([[1,2,3],[4,5,6]]) == [['1','4'],['2','5'],['3','6']]
