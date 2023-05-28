from moviepy.editor import VideoFileClip

def resize_video(input_file, output_file, width, height):
    clip = VideoFileClip(input_file)
    resized_clip = clip.resize((width, height))
    resized_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

# Usage example
input_file = 'too.mp4'
output_file = 'output.mp4'
width = 600
height = 500
resize_video(input_file, output_file, width, height)
