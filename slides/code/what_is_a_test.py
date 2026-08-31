def test_sort():
    # arrange
    data = [2,3,1,4]
    # act
    sorted_data = sort(data)
    # assert
    assert sorted_data == [1,2,3,4]