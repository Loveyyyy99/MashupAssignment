import shutil

def clear_folders():
    folders = [
        os.path.join("cli", "downloads"),
        os.path.join("cli", "cut_audios"),
        os.path.join("cli", "final_output")
    ]

    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder, exist_ok=True)
import os
import subprocess
from yt_dlp import YoutubeDL
from pathlib import Path


def download_videos(singer, num_videos):
    download_path = os.path.join("cli", "downloads")
    os.makedirs(download_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': False
    }

    search_query = f"ytsearch{num_videos}:{singer} songs"

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


def cut_audios(duration):
    download_path = os.path.join("cli", "downloads")
    cut_path = os.path.join("cli", "cut_audios")
    os.makedirs(cut_path, exist_ok=True)

    mp3_files = []

    for file in os.listdir(download_path):
        input_file = os.path.join(download_path, file)
        output_file = os.path.join(
            cut_path,
            os.path.splitext(file)[0] + ".mp3"
        )

        cmd = [
            'ffmpeg',
            '-y',
            '-i', input_file,
            '-t', str(duration),
            '-acodec', 'libmp3lame',
            '-ab', '192k',
            '-ar', '44100',
            '-ac', '2',
            '-map_metadata', '-1',
            output_file
        ]

        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        mp3_files.append(output_file)

    return mp3_files


def merge_audios(mp3_files, output_filename):
    final_path = os.path.join("cli", "final_output")
    os.makedirs(final_path, exist_ok=True)

    list_file = os.path.join(final_path, "concat_list.txt")

    with open(list_file, "w", encoding="utf-8") as f:
        for file_path in mp3_files:
            abs_path = Path(file_path).resolve()
            f.write(f"file '{abs_path}'\n")

    output_path = os.path.join(final_path, output_filename)

    cmd = [
        'ffmpeg',
        '-y',
        '-f', 'concat',
        '-safe', '0',
        '-i', list_file,
        '-acodec', 'libmp3lame',
        '-ab', '192k',
        '-ar', '44100',
        '-ac', '2',
        output_path
    ]

    subprocess.run(cmd)

    print("Mashup created successfully.")
