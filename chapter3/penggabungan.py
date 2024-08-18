from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

# Memuat file video
video = VideoFileClip('result.mp4')

short_video = video.subclip(0, 10)

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')