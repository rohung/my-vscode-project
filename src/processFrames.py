def process_frames(frames):
    good_frames = [f for f in frames if f >= 90]  # List comprehension
    if not good_frames:
        return "Too dark-retry!"
    return sum(good_frames) / len(good_frames)


print(process_frames([100, 80, 120]))
print(process_frames([70, 85]))
