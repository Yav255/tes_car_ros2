
def check_status(sensor_voltage):
    if sensor_voltage <1.0: 
        return "TRIGGERED"
    else:
        return "FAILED"

def test_stop_triggers_on_low_voltage():
    actual_status = check_status(2.0)

    assert actual_status == "FAILED"

def check_wheel_speed(wheel_speeds):

    if 0.0 in wheel_speeds:
        return "SLIPPED"
    else:
        return "NORMAL"

def test_stucked_wheels():

    speeds = [1.0, 2.0, 2.0, 0.0]
    result = check_wheel_speed(speeds)

    assert result == "SLIPPED"

def test_normal_driving_no_slip():
    
    speeds = [1.0, 2.0, 2.0, 1.0]
    result = check_wheel_speed(speeds)

    assert result == "NORMAL"
