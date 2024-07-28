from flask import Flask, request, jsonify
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__)

@app.route('/cut_video', methods=['POST'])
def cut_video_api():
    data = request.get_json()
    input_file = data['input_file']
    output_file_name = data['output_file_name']
    start_time = data['start_time']
    end_time = data['end_time']

    def cut_the_video(input_file, output_file_name, start_time, end_time):
        video = VideoFileClip(input_file)
        trimmed_video = video.subclip(start_time, end_time)
        trimmed_video.write_videofile(output_file_name)
        trimmed_video.close()
        return output_file_name

    result = cut_the_video(input_file, output_file_name, start_time, end_time)
    return jsonify({'output_file_name': result})

if __name__ == '__main__':
    app.run(debug=True)