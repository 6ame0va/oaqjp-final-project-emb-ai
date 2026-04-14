import requests
import json
"""
Function to run emotion detection using the appropriate Emotion Detection function.
"""

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    someObj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json=someObj, headers=header)
    # Parse response as json
    parsed_response = json.loads(response.text)
    # Collect specific traits to return
    anger_score = parsed_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = parsed_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = parsed_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = parsed_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = parsed_response['emotionPredictions'][0]['emotion']['sadness']
    # Collect all in a dic for futher parsing
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)
    # Collect the larget in the lisrt

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
