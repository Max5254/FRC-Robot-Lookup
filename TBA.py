import requests
import datetime
import sys
import pyimgur
import urllib2
import urllib
import json
import webbrowser
from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template


now = datetime.datetime.now()

#imgur API
client_id = '553a684bfb74c46'
im = pyimgur.Imgur(client_id)
client_secret = 'a3c9db6724915332b454256493cbb0e854db1e5e'



# This whole project was based on some code by @gersteinj.
# Thanks for the initial code!

initials = 'MW'
github = "https://github.com/Max5254/"
teamToHighlight = str("5254")  # Enter your own team here!

baseURL = 'http://www.thebluealliance.com/api/v2/'
header = {'X-TBA-App-Id': 'frc5254:thepythonalliance:beta'}  # Yay, version strings....


@route('/')
@route('/index.html')
def index():
    return '<a href="/hello">Go to Hello World page</a>'

@route('/hello')
def hello():
    return '<h1>HELLO WOLRD</h1>'


class tba:

    def get_team_name(self, team_no):

        myRequest = (baseURL + 'team/frc' + str(team_no))
        response = requests.get(myRequest, headers=header)
        jsonified = response.json()
        return jsonified['nickname']

    def img(self, teamNumber):
        #teamNumber = raw_input("please enter a team number: ")
        myRequest = (baseURL + 'team/frc' + str(teamNumber) + '/'+ str(now.year) + "/media")
        response = requests.get(myRequest, headers=header)
        jsonified = response.json()
        #print(jsonified)
        key = ""
        if jsonified != None:
            type = jsonified[0]['type']
            if type == "imgur":
                key = jsonified[0]['foreign_key']
                #print key
            image = im.get_image(key)
            #print(image.link)
            imgURL = ("www." + str(type)  + ".com/" + str(key))
            return image.link



tba = tba()
#tba.img()

@route('/Team/:TeamNumber')
def ShowImage(TeamNumber):
    imgURL = tba.img(TeamNumber)
    return '<h1>Team %s 2016 Robot<br><img src=%s></h1>' % (TeamNumber, imgURL)

run(host='localhost', port=8000, reloader=True)
