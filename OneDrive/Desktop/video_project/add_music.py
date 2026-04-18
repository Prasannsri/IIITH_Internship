from moviepy.editor import VideoFileClip, AudioFileClip

video = VideoFileClip("output_video.mp4")
audio = AudioFileClip("music.mp3")

final = video.set_audio(audio)
final.write_videofile("final_output.mp4")