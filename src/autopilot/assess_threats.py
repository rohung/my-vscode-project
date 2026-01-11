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


