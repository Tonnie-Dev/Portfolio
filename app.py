from flask import Flask,render_template,request

from flask_mail import Mail,Message


app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "felixmurimi280@gmail.com"
app.config['MAIL_PASSWORD'] =  "16Fj79%01"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_message', methods=['GET','POST'])
def send_message():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']

        message = Message(subject,name,sender="feixmurimi280@gmail.com",recipients=[email])

        message.body = msg

        mail.send(message)

        success = "Message Sent"

        return render_template("result.html",success=success)



if __name__ =="_main_":
    app.run(debug=True)