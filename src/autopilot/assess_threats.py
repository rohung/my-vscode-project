# Get threats from sensors
def assess_threats(sensor_list):
    # Function receives a list of distances
    threat_list = []
    # Looping through sensor list from 0 to 8 index to determine threat level
    for distance in sensor_list:
        if distance == float('inf') or distance >= 20:
            threat_list.append("Safe")
        elif distance >= 10:
            threat_list.append("Warning")
        else:
            threat_list.append("Critical")
    
    return threat_list


sensor_data = [float('inf'), 15.2, 8.1, float('inf'), float('inf'), 7.3, 12.0, float('inf'), float('inf')]
result = assess_threats(sensor_data)
print(result)