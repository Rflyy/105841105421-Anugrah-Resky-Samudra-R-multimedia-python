from moviepy.editor import vfx
from moviepy.editor import VideoFileClip

# Memuat file video
video = VideoFileClip('result.mp4')

short_video = video.subclip(0, 10)
reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('reversed_result.mp4')