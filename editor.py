import cv2
from moviepy.editor import VideoFileClip, concatenate_videoclips

def cut_video(input_path, start_time, end_time, output_path):
    """
    Cut a portion of the video from start_time to end_time and save it to output_path.
    """
    try:
        clip = VideoFileClip(input_path).subclip(start_time, end_time)
        clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        clip.close()
    except Exception as e:
        raise RuntimeError(f"Failed to cut video: {str(e)}")


def join_videos(video_paths, output_path):
    """
    Join multiple videos into a single video and save it to output_path.
    """
    try:
        clips = [VideoFileClip(path) for path in video_paths]
        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        for clip in clips:
            clip.close()
    except Exception as e:
        raise RuntimeError(f"Failed to join videos: {str(e)}")
