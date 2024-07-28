from moviepy.editor import VideoFileClip
import os

def cut_the_video(input_file,output_file_name, start_time, end_time):

    video = VideoFileClip(input_file)
    trimmed_video = video.subclip(start_time, end_time)
    trimmed_video.write_videofile(output_file_name)
    trimmed_video.close()
    return output_file_name

def time_to_seconds(time):
    time = time.split(".")
    if len(time) == 2:
        return int(time[0])*60 + int(time[1])
    elif len(time) == 3:
        return int(time[0])*3600 + int(time[1])*60 + int(time[2])
    else:
        return int(time[0])

    
videos = [
     {
        'title': "Intro",
        'start_time': "0.31",
        'end_time': "4.43"
    },
    {
        'title': "Era of AI Influencers",
        'start_time': "4.43",
        'end_time': "13.40"
    },
     {
        'title': "Zoya Chatbot",
        'start_time': "13.40",
        'end_time': "18.41"
    },
    {
        'title': "Create Image for Chatbot",
        'start_time': "18.41",
        'end_time': "34.44"
    },
    {
        'title': "Define persona for Chatbot",
        'start_time': "34.44",
        'end_time': "46.22"
    },
    {
        'title': "Creating the Chatbot",
        'start_time': "46.22",
        'end_time': "59.11"
    },
    {
        'title': "Crash Course",
        'start_time': "1.1.20",
        'end_time': "1.8.26"
    },
    {
        'title': "Add Animation to Image",
        'start_time': "1.8.26",
        'end_time': "1.11.52"
    },
]

input_file = "create-your-ai-girlfriend.mp4"
output_dir_name = "create-your-ai-girlfriend-videos"

if not os.path.exists(output_dir_name):
    os.makedirs(output_dir_name)

for video in videos:
    output_path = os.path.join(output_dir_name,f"{video['title']}.mp4")
    cut_the_video(input_file, output_path,time_to_seconds(video['start_time']),time_to_seconds(video['end_time']))
