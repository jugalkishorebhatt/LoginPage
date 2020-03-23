import traceback
import logging
from google.appengine.ext import ndb


def guestbook_key(guestbook_name):    
    return ndb.Key('Guestbook', guestbook_name)

class StoreRetrieveData(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    phone = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Login:

   def __init__(self):
      pass

   
from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
login = Login()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/change',methods = ['POST', 'GET'])
def changeName():
   try:
      if request.method == 'POST':
         user = request.form['ExistingName']
         print user
         return redirect(url_for('success',name = user))
      else:
         user = request.args.get('ExistingName')
         print user
         return redirect(url_for('success',name = user))
   except:
      print "Change except"
      return render_template('ChangeName.html')

@app.route('/update',methods = ['POST', 'GET'])
def updateName():
   try:
      if request.method == 'POST':
         user= request.form['OldPassword']
         return redirect(url_for('success',name = user))
      else:
         user = request.args.get('OldPassword')
         return redirect(url_for('success',name = user))
   except:
      print "UpdatePassword except"
      return render_template('UpdatePassword.html')

@app.route('/success/<name>')
def success(name):
   return render_template('success.html', string_variable=name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   try:
      if request.method == 'POST':
         user = request.form['nm']
         #StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__storeData(user)
         store = StoreRetrieveData(parent=guestbook_key(user))
         #ancestor_key = ndb.Key("user", user)
         store.name = "SampleName"
         store.phone = "999 999 999"
         store.email = "jugal.bhatt@gmail.com"
         store.put()
         return redirect(url_for('success',name = user))
      else:
         user = request.args.get('nm')
         #StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__storeData(user)
         store = StoreRetrieveData(parent=guestbook_key(user))
         #ancestor_key = ndb.Key("user", user)
         store.name = "SampleName"
         store.phone = "999 999 999"
         store.email = "jugal.bhatt@gmail.com"
         store.put()
         return redirect(url_for('success',name = user))
   except:
      print "login Exception - hello.py"
      logger.error("Main Method, config file", traceback.print_exc())
     

if __name__ == '__main__':
    app.run(debug=True)
