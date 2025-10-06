import os
from pymediainfo import MediaInfo

def get_total_video_duration(directory_path):
    video_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm','.ts']
    total_duration_seconds = 0

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.splitext(file)[1].lower() in video_extensions:
                try:
                    media_info = MediaInfo.parse(file_path)
                    for track in media_info.tracks:
                        if track.track_type == "Video" and track.duration:
                            total_duration_seconds += float(track.duration) / 1000  # ms to sec
                            break
                except Exception as e:
                    print(f"⚠️ Error processing {file_path}: {e}")

    return total_duration_seconds

def format_seconds_to_hms(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = int(seconds % 60)
    return f"{hours}h {minutes}m {remaining_seconds}s"

if __name__ == "__main__":
    # 👇 Replace this with your target folder path
    directory_path = "D:\Coding\BittenTech"

    print(f"🔍 Scanning directory (including subfolders): {directory_path}")
    total_duration = get_total_video_duration(directory_path)
    formatted_duration = format_seconds_to_hms(total_duration)

    print(f"\n📽️ Total video duration: {formatted_duration}")
