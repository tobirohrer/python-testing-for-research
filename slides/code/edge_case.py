
def test_sort():
  data = [1,-1,0]
  assert sort(data) == [-1,0,1]

@pytest.mark.parametrize("data, expected", 
                         [
                            ([3,1,2], [1,2,3]),
                            ([-1,2,0], [-1,0,2]),
                            ([-1,0,0], [-1,0,0]),
                            ([-1.5,1.5,0], [-1.5,0,1.5]),        
                         ])
def test_sort(data, expected):
    assert sort(data) == expected