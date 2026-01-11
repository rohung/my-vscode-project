from assess_threats import assess_threats
from decide_speed import decide_speed
from decide_steering import decide_steering

def autopilot_decision(sensor_data, vehicle_state):
    # Step inside: Get threats from sensors
    threats = assess_threats(sensor_data)
    # Decide speed change based on threats and speed
    accel = decide_speed(threats, vehicle_state['speed'])
    # Decide steering based on threats, bias, and speed
    steer = decide_steering(threats, vehicle_state['direction_bias'], vehicle_state['speed'])
    # Package and return the pair
    return (steer, accel)


sensor_data = [7.3, 12.0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
vehicle_state = {'speed': 50.0, 'direction_bias': -0.8}

result = autopilot_decision(sensor_data, vehicle_state)
print(result)