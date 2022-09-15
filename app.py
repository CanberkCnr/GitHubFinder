from flask import Flask,redirect,url_for,render_template,request
import requests


url = "https://api.github.com/users/"

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    if request.method=='POST':
        name = request.form.get("githubname")
        response_user = requests.get(url + name)
        infos = response_user.json()
        response_repo = requests.get(url + name + "/repos")
        info_repo = response_repo.json()
        if "message" in infos:
            return render_template("index.html",error = "Kullanıcı Bulunamadı")
        else:
            return render_template('index.html', info = infos, info_repo = info_repo)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)