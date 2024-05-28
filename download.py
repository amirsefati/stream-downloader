import requests
import tempfile
from moviepy.editor import VideoFileClip, concatenate_videoclips

video_urls = ["", ""]

video_paths = []
for url in video_urls:
    response = requests.get(url)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as file:
        file.write(response.content)
        video_paths.append(file.name)

video_clips = [VideoFileClip(path) for path in video_paths]

final_clip = concatenate_videoclips(video_paths)

output_path = "final_video.mp4"

final_clip.write_videofile(output_path, codec="libx264")

for clip in video_clips:
    clip.close()
