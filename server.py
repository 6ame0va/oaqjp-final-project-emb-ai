from flask import Flask, request, render_template, url_for, redirect, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_route():
    textToAnalyze = request.form.get(textToAnalyze)
    response_analyzed = emotion_detector(textToAnalyze)

    anger = response_analyzed['anger']
    disgust = response_analyzed['disgust']
    fear = response_analyzed['fear']
    joy = response_analyzed['joy']
    sadness = response_analyzed['sadness']
    dominant_emotion = response_analyzed['dominant_emotion']

    return ("For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}.")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
