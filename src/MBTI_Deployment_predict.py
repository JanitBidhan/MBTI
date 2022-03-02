import requests
from bs4 import BeautifulSoup
import re
import pickle
from nltk.stem import WordNetLemmatizer

from twitterPull import *
import time

import os

def predictCore(targetText, vectorizer, model, labelEncoder):

    def replaceLinks(url):

          if type(url) is list:
            returnAppendedVal = ''
            for item in url:
                returnAppendedVal += replaceLinks(item)
                returnAppendedVal += ' '
            
            return returnAppendedVal

          returnVal = ''

          if not ('youtube.com' in url or 'youtu.be' in url): 
            return returnVal
          
          if 'attachment' in url or 'youtube-' in url:
            return returnVal
          # print(url)
          try:
              get_url = requests.get(url)
              get_text = get_url.text
              soup = BeautifulSoup(get_text, "html.parser")
          except:
              return returnVal

          if not soup.select('title'):
            return returnVal

          if 'youtube' in url or 'youtu.be' in url:
              title = str(soup.select('title')[0])
              r1 = re.findall(r"(?s)(?<=<title>)(.+?)(?=</title>)",title)
              returnVal = r1[0][:-10]

          return returnVal

    replaceLinks(["http://personalitycafe.com/istp-articles/76785-recognizing-inferior-function-istp.html", "https://www.youtube.com/watch?v=OZhotG08rU4", "www.pinterest.com"])


    def clean_text_single(data):
        
        data_length=[]
        lemmatizer=WordNetLemmatizer()
        cleaned_text=[]
        
        sentence = data

        sentence=sentence.lower()
            
        tempLinks = [i[0] for i in re.findall('((http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))', sentence)]

        sentence=re.sub('((http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))', ' ' ,sentence)

        sentence += replaceLinks(tempLinks)

        sentence=re.sub('[^0-9a-z]',' ',sentence)


        return sentence, len(sentence)



    cleaned_text, data_length = clean_text_single(targetText)


    target_text=vectorizer.transform([targetText]).toarray()

    mbtiType = labelEncoder.inverse_transform(model.predict(target_text))

    
    # Test all model outputs
    # models = os.listdir('models/')
    # for modelName in models:
    #     if '.pkl' in modelName and 'xgb' not in modelName:
    #         with open(f'models/{modelName}', 'rb') as f:
    #             model = pickle.load(f)

    #         print(modelName,labelEncoder.inverse_transform(model.predict(target_text)))

    return mbtiType[0]

def predictMBTI(targetText, textType):

    import pickle
    from nltk.stem import WordNetLemmatizer

    class Lemmatizer(object):
        def __init__(self):
            self.lemmatizer = WordNetLemmatizer()
        def __call__(self, sentence):
            return [self.lemmatizer.lemmatize(word) for word in sentence.split() if len(word)>2]

    with open('models/vectorizer.pk', 'rb') as f:
        vectorizer = pickle.load(f)

    with open('models/model_cat-Links.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('models/target-encoder.pk', 'rb') as f:
        labelEncoder = pickle.load(f)

    if textType == 'twitter':

        targetText = twitterPull(targetText)

    mbtiType = predictCore(targetText, vectorizer, model, labelEncoder)

    print(type(mbtiType))

    return mbtiType