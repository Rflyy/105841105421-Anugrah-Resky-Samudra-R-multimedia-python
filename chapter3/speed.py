from moviepy.editor import vfx
from moviepy.editor import VideoFileClip



video = VideoFileClip('result.mp4')

short_video = video.subclip(0, 10)
sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('sped_up_result.mp4')