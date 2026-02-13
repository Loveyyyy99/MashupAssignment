import sys
import os

# Allow importing from parent directory
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from mashup_core import (
    clear_folders,
    download_videos,
    cut_audios,
    merge_audios
)


def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("Number of videos and duration must be integers.")
        sys.exit(1)

    output_filename = sys.argv[4]

    if num_videos <= 10:
        print("Number of videos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("Audio duration must be greater than 20 seconds.")
        sys.exit(1)

    try:
        # 🧹 Clear old files first
        clear_folders()

        # 🎵 Run mashup process
        download_videos(singer, num_videos)
        mp3_files = cut_audios(duration)
        merge_audios(mp3_files, output_filename)

    except Exception as e:
        print("Error occurred:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
