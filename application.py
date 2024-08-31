from flask import Flask, render_template, request
import os
import aiml
#from autocorrect import spell
from autocorrect import Speller

import time
spell = Speller(lang='en')
app = Flask(__name__)

BRAIN_FILE="./pretrained_model/my_modelv1.dump"
k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)



@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')



@app.route("/dstv",  methods=['GET', 'POST'])
def channels():
    #payment.makePayment(10)
    #print("paying")
    #import requests
  
    return render_template("/dstv.html",
    
        title='learn',
        posts=""
    )

 
 
@app.route("/exam",  methods=['GET', 'POST'])
def markExam():
    #payment.makePayment(10)
    #print("paying")
    #import requests
  
    return render_template("/marker.html",
    
        title='learn',
        posts=""
    )

@app.route("/test",  methods=['GET', 'POST'])
def pay():
    #payment.makePayment(10)
    #print("paying")
    #import requests
 
   
    print("done")
    return render_template("/today.html",
    
        title='learn',
        posts=""
    )


@app.route("/product",  methods=['GET', 'POST'])
def product():
    print("doin nothin")
   
    return render_template("/product.html",
    
        title='learn',
        posts=""
    )

@app.route("/product/bolo",  methods=['GET', 'POST'])
def bolo():
   
    return render_template("/bolo.html",
    
        title='learn',
        posts=""
    )




@app.route('/thanks.html', methods=['GET', 'POST'])
def contacts():
    uname = request.form['Name']
    email=request.form["Email"]
    use_msg=request.form["Message"]
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = 'contact@schweetzsoftware.solutions'
    msg['Subject'] = 'A User sent a message'
    message =uname+" "+ use_msg
    msg.attach(MIMEText(message))
    try:
        mailserver = smtplib.SMTP('schweetzsoftware.solutions',587)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        #Send email here
        
        mailserver.login('contact@schweetzsoftware.solutions', 'O#6E#5E7,%&1')
        
        mailserver.sendmail(email,'contact@schweetzsoftware.solutions',msg.as_string())
        print ("success")
        return render_template("thanks.html")

    except Exception as e:
        # Print any error messages to stdout
        print("please try again")
        print(e)
    finally:
        mailserver.quit()

         
         
 

 
@app.route("/")
def home():
    return render_template("index.html",
    
        title='Home Page',
        posts=""
    )



@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    query = [spell(w) for w in (query.split())]
    question = " ".join(query)
    response = k.respond(question)
    if response:
        time.sleep(1)
        return (str(response))
    else:
        return (str(":)"))

print("tes..")
if __name__ == "__main__":
    app.run()
    #app.run(host='0.0.0.0', port='5000')


