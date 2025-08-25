from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import nltk
from newspaper import Article
import validators


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello ,!"


@app.route("/sms", methods=['POST'])

def sms_reply():
    """Respond to incoming calls with a single message."""
    # Fetch the message
    msg = request.form.get('Body')
    if validators.url(msg):

        
        nltk.download('punkt')
        try:
            article = Article(msg)
            article.download()
            article.parse()
            article.nlp()
            tit = article.title
            res = article.summary
            ext = "Title : \n" + tit  + ".\n" + "\n" + "Summary : \n" + res
            resp = MessagingResponse()
            resp.message("{}".format(ext))
            return str(resp)
        except:
            resp = MessagingResponse()
            resp.message("⚠️ URL Invalid ! Kindly send valid one.")
            return str(resp)

    elif msg == "Hi" or msg == "hi":
        resp = MessagingResponse()
        resp.message("Hi, I am Karen 👋 , a Twilio Bot. I will summarise any news , article , blog in text and send to you 📒 . Send only valid URL for the result. Hell Yeah!✅ - Project made by Kishore for Cloud Native Hackathon.")
        return str(resp)
    
    else :
        resp = MessagingResponse()
        resp.message("⚠️ Kindly Send Valid URL")
        return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)







