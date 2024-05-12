
from textblob import TextBlob
import pyttsx3


engine = pyttsx3.init()
engine.say("Hello employee number 2178558883. We hope you had a great day pf work.It is time to submit your employee wellness statement")
engine.runAndWait()


print("Enter your employee wellness statement: ")
phrase = input("> ")
blob = TextBlob(phrase)
while blob.sentiment.polarity < 0.5:
    engine.say("Employee number 2178558883, that was not a very positive employee wellness statement.")
    engine.runAndWait()
    print("More postive please: ")
    phrase = input("> ")
    blob = TextBlob(phrase)
    
print("We appreciate you too!")
engine.say("Employee number 2178558883, Thank you for such a kind and postive statement! We here at the Ministry of Work appreciate you too!")
engine.runAndWait()