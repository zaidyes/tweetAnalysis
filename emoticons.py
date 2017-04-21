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
	
def calculateEmotion(sentimentAggr)
	if sentimentAggr == 0 :
		return Emotion.Neutral
	if sentimentAggr < -0.8 :
		return Emotion.Anger
	if sentimentAggr < -0.6 :
		return Emotion.Disgust
	if sentimentAggr < -0.4 :
		return Emotion.Sad
	if sentimentAggr < -0.2 :
		return Emotion.Fear
	if sentimentAggr > 0.2 :
		return Emotion.Happy
	if sentimentAggr > 0.6 :
		return Emotion.Surprise	
