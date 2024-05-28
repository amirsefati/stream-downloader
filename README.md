
# Concatenating the downloaded chunked video

Many times, streamed videos send chunked video segments with new URLs to the client. This script helps concatenate these videos.



## steps
1.find pattern of new url to download 
2.create loop to download all video and save with "requests" Python Package


## Installation

Install python packages
```bash
pip install moviepy requests
```

Run project
```bash
  git clone <repo>
  cd stream-downloader
  python download.py
```

If use Mac operaiton system install FFmpeg 
```bash
brew install ffmpeg
```
and set environment in file
```bash
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
```
