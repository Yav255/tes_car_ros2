import pytest 
from unittest.mock import MagicMock

def evaluate_dis_sensor(sensor_node):
    distance = sensor_node.get_distance()
    if distance < 0.5 :
        return "COLLISION_WARNING"
    return "CLEAR"


def test_sensor_collision_warnin():
    mock_sensor = MagicMock()

    mock_sensor.get_distance.return_value =0.3

    result = evaluate_dis_sensor(mock_sensor)

    assert result == "COLLISION_WARNING"
