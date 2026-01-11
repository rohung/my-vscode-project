# Using threat list to decide speed
def decide_speed(threat_list, speed):
    # Front critical (emergency)
    front_slice = threat_list[3:6]
    if 'Critical' in front_slice:
        return -5.0
    
    # Warnings anywhere
    warning_count = threat_list.count('Warning') 
    if warning_count >= 2:
        return -2.0
    
    # Totally clear + high speed
    total_threats = threat_list.count('Warning') + threat_list.count('Critical')
    if speed > 80 and total_threats == 0:
        return -1.0
    
    # Default
    return 0.5