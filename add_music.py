from moviepy.editor import VideoFileClip, AudioFileClip

video = VideoFileClip("segmentation_video.mp4")
audio = AudioFileClip("music.mp3")

final = video.set_audio(audio)
final.write_videofile("segmentation_final.mp4")