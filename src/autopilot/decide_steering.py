import math  # Only for potential future extensions; not strictly needed here

def decide_steering(threat_list, direction_bias, speed):
    """
    Find the widest safe gap (>=3 consecutive 'Safe') and steer toward its center.
    Returns steering_angle (float, rounded to 1 decimal, clamped -30 to +30).
    """
    best_width = 0
    best_center = 4.0  # Default: straight ahead
    best_score = float('-inf')  # For tie-breaking with bias
    
    i = 0
    while i < len(threat_list):
        if threat_list[i] == 'Safe':
            # Find the end of this safe streak
            start = i
            while i < len(threat_list) and threat_list[i] == 'Safe':
                i += 1
            end = i - 1  # end is inclusive
            width = end - start + 1
            
            if width >= 3:
                center = (start + end) / 2.0
                
                # Bias score: how well this center matches the driver's preference
                # We want to maximize this score for right bias, minimize for left
                # Simple formula: score = center * direction_bias
                # (positive bias likes high center, negative likes low)
                bias_score = center * direction_bias
                
                # Primary: wider is always better
                # Secondary: if same width, higher bias_score wins
                if (width > best_width) or (width == best_width and bias_score > best_score):
                    best_width = width
                    best_center = center
                    best_score = bias_score
        else:
            i += 1
    
    # If no good gap found, default to straight
    if best_width < 3:
        return 0.0
    
    # Calculate raw angle
    speed_dampener = 1 - (speed / 100.0)
    speed_dampener = max(0.0, speed_dampener)  # Don't go negative at very high speeds
    raw_angle = (best_center - 4.0) * 5.0 * speed_dampener
    
    # Clamp to -30 to +30
    clamped_angle = max(-30.0, min(30.0, raw_angle))
    
    # Round to 1 decimal place
    return round(clamped_angle, 1)