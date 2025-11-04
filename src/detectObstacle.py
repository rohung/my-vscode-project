def detect_obstacle(distance, speed):
    if distance < 5 and speed > 20:
        return "Brake hard!"
    elif distance < 10:
        return "Swerve!"
    else:
        return "Cruise on!"


print(detect_obstacle(3, 25))
print(detect_obstacle(15, 10))
