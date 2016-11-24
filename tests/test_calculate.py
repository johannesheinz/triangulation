import pytest
from triangulation import calculate as calc

def test_intersecting_lines():
    matrix = [[[2,1], [3,2]], [[1,0],[2,0]]]
    assert calc.check_intersection(matrix, None)    

def test_intersecting_lines_outside_range():
    matrix = [[[0,10], [1,9.9]], [[0,0.01],[1,0.02]]]
    assert not calc.check_intersection(matrix, None)    
    
def test_parallel_lines():
    matrix = [[[1,1], [2,2]], [[1,0],[2,1]]]
    assert not calc.check_intersection(matrix, None)    

def test_identical_lines():
    matrix = [[[1,1], [3,3]], [[0,0],[2,2]]]
    assert not calc.check_intersection(matrix, None)    

#def test_orientation():
#    matrix = [[1, 2], [3, 4]]
#    orientation = calc.check_orientation(matrix, None)
#    print('orientation', orientation)
#    assert false
