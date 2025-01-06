import sys
import os
from pathlib import Path
import subprocess

def get_ffmpeg_path():
    """Get the appropriate ffmpeg path based on OS"""
    if os.name == 'nt':  # Windows
        return Path(r"C:\ffmpeg\bin\ffmpeg.exe")
    else:  # Linux/Unix
        return 'ffmpeg'  # Assuming it's in PATH

def download_youtube(url: str, format_type: str) -> None:
    """
    Download YouTube video in either MP3 or MP4 format.
    
    Args:
        url (str): YouTube video URL
        format_type (str): Either 'mp3' or 'mp4'
    """
    # Validate format type
    if format_type.lower() not in ['mp3', 'mp4']:
        raise ValueError("Format type must be either 'mp3' or 'mp4'")
    
    # Get the appropriate paths based on OS
    if os.name == 'nt':  # Windows
        ytdlp_path = Path(r"C:\Users\michu\yt-dlp.exe")
    else:  # Linux/Unix
        ytdlp_path = 'yt-dlp'  # Assuming it's in PATH
        
    ffmpeg_path = get_ffmpeg_path()
    
    # Set up the command based on format type
    if format_type.lower() == 'mp3':
        command = [
            str(ytdlp_path),
            '--ffmpeg-location', str(ffmpeg_path),
            '-x',  # Extract audio
            '--audio-format', 'mp3',
            '--audio-quality', '0',  # Best quality
            '-o', '%(title)s.%(ext)s',  # Output template
            url
        ]
    else:  # mp4
        command = [
            str(ytdlp_path),
            '--ffmpeg-location', str(ffmpeg_path),
            '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            '-o', '%(title)s.%(ext)s',
            url
        ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Successfully downloaded in {format_type} format!")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <youtube_url> <format_type>")
        print("Format type must be either 'mp3' or 'mp4'")
        sys.exit(1)
    
    url = sys.argv[1]
    format_type = sys.argv[2]
    
    try:
        download_youtube(url, format_type)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()