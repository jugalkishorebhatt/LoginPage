import traceback
import logging
from actions import StoreRetrieveData


class Login:
   
   
   def __init__(self):
      self.updating = ""
   
from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logining = Login()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/change/')
def changePage():
    return render_template('ChangeName.html')

@app.route('/changeSubmit',methods = ['POST', 'GET'])
def changeName():
   #fields = SaveDict.SaveDict()._SaveDict__getDict()
   fields = {}
   try:
      if request.method == 'POST':
         
         fields['id'] = logining.updating['id']
         fields['stuPassword'] = logining.updating['stuPassword']
         fields['stuName'] = request.form['NewName']
         print('Student Fields: '+ str(fields))
         print('Student Id Field: '+fields['id'])
         print("Updated Values Password:"+str(logining.updating['stuPassword']))
         StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__saveData(fields['id'],fields)
         #SaveDict.SaveDict()._SaveDict__updateDict(fields)
         return redirect(url_for('success', name=fields['id']))
   except:
      print("Change except")
      logger.error("changeName Method, config file", traceback.print_exc())
      return render_template('index.html')

@app.route('/update/')
def updatePage():
    return render_template('UpdatePassword.html')
 
@app.route('/updateSubmit',methods = ['POST', 'GET'])
def updatePassword():
   #fields = SaveDict.SaveDict()._SaveDict__getDict()
   fields = {}
   try:
      if request.method == 'POST':
         fields['id'] = logining.updating['id']
         fields['stuPassword']= request.form['NewPassword']
         fields['stuName'] = logining.updating['stuName']
         StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__saveData(fields['id'],fields)
         #SaveDict.SaveDict()._SaveDict__updateDict(fields)
         return redirect(url_for('success', name=fields['id']))
   except:
      print("UpdatePassword except")
      return render_template('index.html')

@app.route('/register')
def registerPage():
    return render_template('register.html')

@app.route('/registerSubmit',methods = ['POST', 'GET'])
def register():
    fields = {}
    try:
      if request.method == 'POST':
         fields['id']= request.form['stuId']
         fields['stuName']= request.form['stuName']
         fields['stuPassword']= request.form['pwd']
         #SaveDict.SaveDict()._SaveDict__updateDict(fields)
         #StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__setStudentId(fields['id'])
         #print('register SetStudentId: '+ StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__getStudentId())
         #save.setStudentId(fields['id'])
         print("StudentId: "+fields['id'])
         print("StudentName: "+fields['stuName'])
         print("StudentPassword: "+fields['stuPassword'])
         print("Student: "+str(fields))
         print("Testing Logining Data: "+ str(logining.updating))
         logining.updating = fields
         
         print("Updated Values:"+str(logining.updating))
         
         StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__saveData(fields['id'],fields)
         return redirect(url_for('success', name=fields['id']))
    except:
      print("Register except")
      logger.error("register Method, config file", traceback.print_exc())
      return render_template('register.html')
   

@app.route('/success/<name>')
def success(name):
   return render_template('success.html', string_variable=name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   try:
      if request.method == 'POST':
         user = request.form['nm']
         pwd = request.form['pwd']
         retValue = StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__getUser(user,pwd)
         #password = StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__getUser(pwd)
         
         print('userName {}: {}'.format("Testing", retValue[0]))
         print('PasswordName {}: {}'.format("Testing", retValue[1]))
         if (retValue[0] and pwd == retValue[1]):
            #print('Flag: '+pwd == retValue[1])
            #if(pwd == retValue[1]):
            print('login func if {}: {}'.format("Testing", pwd))
            #StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__setStudentId(user)
            #print('Login SetStudentId: '+ StoreRetrieveData.StoreRetrieveData()._StoreRetrieveData__getStudentId())
            return redirect(url_for('success',name = user)) 
         else:
            print('login func else {}: {}'.format("Testing", userName))
            return redirect(url_for('registerPage'))      

   except:
      print("login Exception - login.py")
      logger.error("login Method, config file", traceback.print_exc())
      return redirect(url_for('registerPage'))
      
      
if __name__ == '__main__':
    app.run(debug=True)