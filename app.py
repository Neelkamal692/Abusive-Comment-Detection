import gradio as gr
from gradio.components import Text
import joblib
import clean
import nltk
nltk.download('wordnet')
import numpy as np
import language_detection
import requests
import os

print("all imports worked")
# Load pre-trained model
model = joblib.load('model_joblib.pkl')
print("model load ")
tf = joblib.load('tf_joblib.pkl')
print("tfidf load ")

token = os.getenv("HF_TOKEN")

def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/Hate-speech-CNERG/hindi-abusive-MuRIL"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
    
# Define function to predict whether sentence is abusive or not
def predict_abusive_lang(text):
    print("original text ", text)
    
    lang = language_detection.en_hi_detection(text)
    print("language detected ", lang)
    
    if lang=='eng':
        cleaned_text = clean.text_cleaning(text)
        print("cleaned text ", text)
        text = tf.transform([cleaned_text])
        print("tfidf transformation ", text)
        prediction = model.predict(text)
        print("prediction ", prediction)
        if len(prediction)!=0 and prediction[0]==0:
            return ["NA", cleaned_text]
        elif len(prediction)!=0 and prediction[0]==1:
            return ["AB",cleaned_text]
        else :
            return ["Please write something in the comment box..","No cleaned text"]
    elif lang=='hi':
        
        print("using hugging face api")
        output = query({
        "inputs": text#"खान चाचा को मेरा सला"
        })
        print(output, len(output))
        # if(len(output))
        l_0 = float(output[0][0]['score'])
        l_1 = float(output[0][1]['score'])
        if  output[0][0]['label']=='LABEL_1' :
            if l_0>l_1:
                return ["AB",text]
    
        else :
            return ["NA",text]
        
    else :
        return ["UN","No cleaned text"]
    
           
# text = '":::::: 128514 - & % ! @ # $ % ^ & * ( ) _ + I got blocked for 30 minutes, you got blocked for more than days. You is lost.  www.google.com, #happydiwali, @amangupta And I don\'t even know who the fuck are you.  It\'s a zero! \n"'
# predict_abusive_lang(text)

# Define the GRADIO output interfaces
output_interfaces = [
    gr.outputs.Textbox(label="Result"),
    gr.outputs.Textbox(label="Cleaned text")
]
app = gr.Interface(predict_abusive_lang, inputs='text', outputs=output_interfaces, title="Abuse Classifier", description="Enter a sentence and the model will predict whether it is abusive or not.")
#Start the GRADIO app
app.launch()