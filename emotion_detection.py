import requests
"""
Function to run emotion detection using the appropriate Emotion Detection function.
"""

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    someObj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json=someObj, headers=header)
    return response.text