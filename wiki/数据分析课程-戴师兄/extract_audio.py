#!/usr/bin/env python3
from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path, output_path):
    """Extract audio from video to mp3"""
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_path)
    clip.close()
    print(f"Extracted: {output_path}")

if __name__ == "__main__":
    videos = [
        "告别一切重复枯燥任务，CLI+Skill搭建浏览器AI自动化框架[00].mp4",
        "告别一切重复枯燥任务，CLI+Skill搭建浏览器AI自动化框架[01].mp4"
    ]
    
    for video in videos:
        if os.path.exists(video):
            audio_name = os.path.splitext(video)[0] + ".mp3"
            extract_audio(video, audio_name)
