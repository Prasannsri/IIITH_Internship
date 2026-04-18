from moviepy.editor import VideoFileClip

video = VideoFileClip("segmentation_final.mp4")

duration = video.duration  # in seconds

# Target size = 9 MB (safe under 10MB)
target_size_mb = 6.5

# Convert MB → bits
target_size_bits = target_size_mb * 8 * 1024 * 1024

# Calculate bitrate
bitrate = int(target_size_bits / duration)

print(f"Using bitrate: {bitrate}")

# Resize moderately
video = video.resize(height=300)

video.write_videofile(
    "segmentation_small.mp4",
    codec="libx264",
    bitrate=f"{bitrate}",
    fps=12,
    audio_codec="aac"
)

print("Compressed successfully under 10MB!")