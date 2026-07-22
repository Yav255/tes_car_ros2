import pytest
from unittest.mock import MagicMock
def check_safety(battery_level,range_sensor):
    if battery_level < 15 :
        return "LOW_BATTERY"
    dist = range_sensor.get_min_distance()

    if dist < 0.3:
        return "EMERGENCY STOP"
    return "CLEAR"


def test_battery_level():

    mock_sensor = MagicMock()

    battery_level = 25
    mock_sensor.get_min_distance.return_value = 0.5
    
    result = check_safety(battery_level , mock_sensor)

    assert result == "CLEAR" 

def test_emergency_stop():
    mock_sensor = MagicMock()

    mock_sensor.get_min_distance.return_value = 0.2

    battery_lvl  = 80

    result = check_safety(battery_lvl, mock_sensor)

    assert result == "EMERGENCY STOP"

@pytest.mark.parametrize("battery , distance , expected_output", [(30,0.5,"CLEAR" ),
(57 , 0.6 , "CLEAR")])
def test_path_clear_scenarios(battery , distance , expected_output):

    mock_sensor = MagicMock()

    mock_sensor.get_min_distance.return_value = distance

    result = check_safety(battery , mock_sensor)

    assert result == expected_output

    



