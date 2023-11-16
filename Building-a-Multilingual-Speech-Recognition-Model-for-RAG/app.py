from flask import Flask, render_template, request, jsonify
from src.utils import saveAudio, saveVideo, getAudio
from src.model import getAudioModelPipeline, getSummaryModelPipeline

app = Flask(__name__)
audio_model = getAudioModelPipeline()
summary_model = getSummaryModelPipeline()


@app.route('/uploadAudio', methods=['POST'])
def upload_file():

    try:
        if 'audio' not in request.files:
            return {'error': 'No audio file provided'}, 400

        audio_file = request.files['audio']
        if audio_file:
            audioPath = saveAudio(audio_file)
            result = audio_model(audioPath)
            result = result["text"]
            result = summary_model(result)
            return jsonify({'message': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/uploadVideo', methods=['POST'])
def upload():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400

        video_file = request.files['video']
        if video_file:
            videoPath = saveVideo(video_file)
            audioPath = getAudio(videoPath)
            result = audio_model(audioPath)
            result = result["text"]
            result = summary_model(result)
            return jsonify({'message': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
