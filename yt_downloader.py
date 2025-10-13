import sys
import os
from yt_dlp import YoutubeDL

def download_best(url):
    # Options for highest quality download with audio
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # best video and audio, merged
        'merge_output_format': 'mp4',          # merge into mp4 container
        'outtmpl': '%(title)s.%(ext)s',        # output filename
        'noplaylist': True,                    # single video only
        'ignoreerrors': True,
        'quiet': False,
        'postprocessors': [{                   # ensure FFmpeg merging
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
        'progress_hooks': [progress_hook]
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} at {d['_speed_str']}", end='\r')
    elif d['status'] == 'finished':
        print(f"\nDownload complete, now post-processing (merging audio/video)...")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python yt_downloader.py <YouTube URL>")
        sys.exit(1)

    url = sys.argv[1]
    download_best(url)
    print("✅ Done! Check your current directory for the downloaded video.")

