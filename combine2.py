import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
'''
> fig out how to combine clips
1. moviepy >> ffmpeg in python
2. diff clips hav diff size, fps, ratio
3. merge all into one taking into acc of diff
4. no loss off qual, no crops only pads
'''
def combine_videos():
#part1
# Set the path to the folder containing the videos
    folder_path = os.getcwd()
# Get a list of all video file names in the folder
    video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

#part2
# Find the maximum video height and width
    max_height = 0
    max_width = 0
    for file in video_files:
        clip = VideoFileClip(file)
        max_height = max(max_height, clip.size[1])
        max_width = max(max_width, clip.size[0])
        clip.close()
# Define a function to process each video file
    def process_video_file(file):
        clip = VideoFileClip(file)
        # Resize the clip to the maximum height and width
        if clip.size[1] < max_height or clip.size[0] < max_width:
            padded_clip = clip.resize((max_width, max_height))
        else:
            padded_clip = clip
        # Set the frame rate to 30 fps coz reddit said so sthu
        if clip.fps != 30:
            padded_clip = padded_clip.set_fps(30)
        clip.close()
        return padded_clip

#part3
# Create a list of VideoFileClip objects from the video files
    video_clips = []
    for file in video_files:
        clip = VideoFileClip(os.path.join(folder_path, file))
        video_clips.append(clip)
# Concatenate the clips into a single video
    final_clip = concatenate_videoclips(video_clips, method='compose')
# Set the output file name and export the final clip
    final_clip.write_videofile('output.mp4')

