import pytest

from python_testing_research.battery import Battery


def test_charge():
    # Try Out Session 1
    # Test if charge operation works correctly

    # Arrange
    # ToDo: Create a battery

    # Act
    # ToDo: Charge the battery

    # Assert
    # ToDo: Check if charging "worked"
    pass

@pytest.mark.parametrize("input_a, expected", 
                         [
                            (-1, 1),
                            (0, 0),
                            # ...
                         ])
def test_charge_with_edge_cases(innput_a, expected):
    # Try Out Session 2
    # First, this is not a nice name for the test ;)
    # Test if charge operation works correctly by defining additional edge cases
    pass