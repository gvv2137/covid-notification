from flask import Flask, render_template, request, redirect
import requests
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route("/")
def hello_world():
    myHtmlData = getData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myHtmlData, 'html.parser')

    spanA = soup.find("li", {'class': 'bg-blue'}).find_all('strong', {'class': 'mob-hide'})[1].get_text()
    a = spanA.split()
    active_cases = a[0]

    spanD = soup.find("li", {'class': 'bg-green'}).find_all('strong', {'class': 'mob-hide'})[1].get_text()
    d = spanD.split()
    discharge_cases = d[0]

    spanX = soup.find("li", {'class': 'bg-red'}).find_all('strong', {'class': 'mob-hide'})[1].get_text()
    x = spanX.split()
    Deaths = x[0]

    Total_cases = int(active_cases) + int(discharge_cases) + int(Deaths)

    return render_template('index.html', active_cases=active_cases, discharge_cases=discharge_cases, Deaths=Deaths, Total_cases=Total_cases)

@app.route("/about")
def about():
    return render_template('aboutus.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)