import re
from textblob import TextBlob

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
        polarity = analysis.sentiment.polarity
        # set sentiment
        return str(polarity)
       

def main():
    while True:
        check = raw_input("Enter word or sentence: ")
        if check == "quit" or check == "exit" :
            break;

        print(check + ": " +  get_sentiment(check))
   

if __name__ == "__main__":
    # calling main function
    main()    