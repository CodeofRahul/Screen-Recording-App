from moviepy.editor import VideoFileClip, concatenate_videoclips

def cut_video(input_path, start_time, end_time, output_path):
    clip = VideoFileClip(input_path).subclip(start_time, end_time)
    clip.write_videofile(output_path)

def join_videos(video_paths, output_path):
    clips = [VideoFileClip(path) for path in video_paths]
    final = concatenate_videoclips(clips)
    final.write_videofile(output_path)
