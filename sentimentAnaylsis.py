import re
from textblob import TextBlob
from enum import Enum

# Based on the explanation
# https://www.microsoft.com/reallifecode/2015/11/29/emotion-detection-and-recognition-from-text-using-deep-learning/
class Emotion(Enum):
    Anger = 1
    Disgust = 2
    Sad = 3
    Happy = 4
    Surprise = 5
    Fear = 6
    Neutral = 7
    
def calculateEmotion(sentimentAggr):
    if sentimentAggr == 0 :
        return Emotion.Neutral
    if sentimentAggr < -0.8 :
        return Emotion.Anger
    if sentimentAggr < -0.6 :
        return Emotion.Fear
    if sentimentAggr < -0.4 :
        return Emotion.Disgust
    if sentimentAggr < -0.2 :
        return Emotion.Sad
    if sentimentAggr > 0 :
        return Emotion.Happy
    if sentimentAggr > 0.6 :
        return Emotion.Surprise 

def clean(text):
        '''
        Utility function to clean text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

def get_sentiment(text):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean(text))
        sentiment = analysis.sentiment
        return sentiment
               

def main():
    while True:
        check = raw_input("Enter word or sentence: ")
        if check == "quit" or check == "exit" :
            break;

        sentiment = get_sentiment(check)
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
        # set sentiment
        aggrSenti = polarity * subjectivity if subjectivity != 0 else polarity
        emotion = calculateEmotion(aggrSenti)
        print(check + " | Polarity: " + str(polarity) + " | Subjectivity: " + str(subjectivity) + " | AgrrSenti: " + str(aggrSenti) + " | emotion: " + str(emotion))
   

if __name__ == "__main__":
    # calling main function
    main()    