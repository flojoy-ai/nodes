import pytest
from unittest.mock import Mock, patch
from flojoy import OrderedPair
from POLOLU_TIC import POLOLU_TIC

# Define a mock ticUSB class and its methods
class MockTicUSB:
    def __init__(self):
        self.time_since_last_step = 100  # milliseconds

    def energize(self):
        pass

    def halt_and_set_position(self):
        pass

    def set_current_limit(self):
        pass

    def set_decay_mode(self):
        pass

    def set_max_acceleration(self):
        pass

    def set_max_deceleration(self):
        pass

    def set_max_speed(self):
        pass

    def set_starting_speed(self):
        pass

    def set_step_mode(self):
        pass

    def set_target_position(self):
        pass

mock_tic = MockTicUSB()

# Patch ticUSB import; return the mock instance
@patch('POLULU_TIC.ticUSB', return_value=mock_tic)
def test_pololu_tic(mock_ticUSB):
    initial_position = 0
    target_position = 1000

    result = POLOLU_TIC(initial_position, target_position)

    assert result.x == initial_position
    assert result.y == mock_tic.time_since_last_step / 1000

if __name__ == '__main__':
    pytest.main()
