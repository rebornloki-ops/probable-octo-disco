import cv2
from collections import defaultdict

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}")
        return

    # Video metadata
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = 0
    frames_per_second = defaultdict(int)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Determine common quality label
    resolution_label = f"{width}x{height}"
    if width >= 3840 or height >= 2160:
        resolution_label += " (4K)"
    elif width >= 2560 or height >= 1440:
        resolution_label += " (2K/QHD)"
    elif width >= 1920 or height >= 1080:
        resolution_label += " (1080p/Full HD)"
    elif width >= 1280 or height >= 720:
        resolution_label += " (720p/HD)"
    else:
        resolution_label += " (SD or lower)"

    # Count frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        current_time_sec = int(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
        frames_per_second[current_time_sec] += 1
        total_frames += 1

    cap.release()

    # Results
    print(f"Video path: {video_path}")
    print(f"Resolution: {resolution_label}")
    print(f"Total frames: {total_frames}")
    print(f"Video FPS (reported): {fps:.2f}")
    print("\nFrames per second:")

    for second in sorted(frames_per_second.keys()):
        print(f"Second {second}: {frames_per_second[second]} frames")


# Example usage
video_file = "/mnt/chromeos/MyFiles/Downloads/VID-20260215-WA0001.mp4"  # Update to your actual path
analyze_video(video_file)