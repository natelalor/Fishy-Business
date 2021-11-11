from flask import Flask, render_template, request
import json
#import mysql.connector
#import RPi.GPIO as GPIO
import time

app = Flask(__name__)


"""
GPIO.setmode(GPIO.BOARD)

#horizontal motor setup
HORIZ_POWER = 10
HORIZ_GROUND = 11
HORIZ_ENA = 12
HORIZ_RIGHT = 13
HORIZ_LEFT = 14

GPIO.setup(HORIZ_RIGHT, GPIO.OUT)
GPIO.setup(HORIZ_LEFT, GPIO.OUT)
GPIO.setup(HORIZ_ENA, GPIO.OUT)
GPIO.output(HORIZ_RIGHT, GPIO.LOW)
GPIO.output(HORIZ_LEFT, GPIO.LOW)
horiz_power = GPIO.PWM(HORIZ_ENA, 20)

#vertical motor setup
VERT_POWER = 10
VERT_GROUND = 11
VERT_ENA = 12
VERT_UP = 13
VERT_DOWN = 14

GPIO.setup(VERT_UP, GPIO.OUT)
GPIO.setup(VERT_DOWN, GPIO.OUT)
GPIO.setup(VERT_ENA, GPIO.OUT)
GPIO.output(VERT_UP, GPIO.LOW)
GPIO.output(VERT_DOWN, GPIO.LOW)
vert_power = GPIO.PWM(VERT_ENA, 20)

#string motor setup
STRING_POWER = 10
STRING_GROUND = 11
STRING_ENA = 12
STRING_UP = 13
STRING_DOWN = 14

GPIO.setup(STRING_UP, GPIO.OUT)
GPIO.setup(STRING_DOWN, GPIO.OUT)
GPIO.setup(STRING_ENA, GPIO.OUT)
GPIO.output(STRING_UP, GPIO.LOW)
GPIO.output(STRING_DOWN, GPIO.LOW)
string_power = GPIO.PWM(STRING_ENA, 20)
"""


#main route
#================================
#startup
@app.route("/", methods=["GET"])
def homeStartup():
    return render_template("index.html", title="index", name="Ty Allembert")
#Index
@app.route("/index.html", methods=["GET"])
def homeIndex():
    return render_template("index.html", title="index", name="Ty Allembert")
#Leaderboard
@app.route("/leaderboard.html", methods=["GET"])
def homeLeaderboard():
    """database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()

    # Your query to return records with ID 20 through 30 [inclusive]
    # from the test_data table
    query = "SELECT * FROM finalProject;"

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    database.close()"""
    return render_template("leaderboard.html", title="Leaderboard", name="Ty Allembert")
#How to play
@app.route("/howToPlay.html", methods=["GET"])
def homeHowTo():
    return render_template("howToPlay.html", title="How to Play", name="Ty Allembert")
#================================

#Motors
#================================
#vertical arm up
@app.route("/vertical_up", methods=["POST"])
def vertical_up():
    print("up")
    #make arm go up
    return "up"

#vertical arm down
@app.route("/vertical_down", methods=["POST"])
def vertical_down():
    print("down")
    #make arm go down
    return "down"

#horizontal spin right
@app.route("/horizontal_right", methods=["POST"])
def horizontal_right():
    print("right")
    #make motor spin right
    return "right"

#horizontal spin left
@app.route("/horizontal_left", methods=["POST"])
def horizontal_left():
    print("left")
    #make motor spin left
    return "left"

#========String Motor==========
#String up
@app.route("/string_up", methods=["POST"])
def string_up():
    print("String up")
    #make motor spin left
    return "String up"
    
#String down
@app.route("/string_down", methods=["POST"])
def string_down():
    print("String down")
    #make motor spin left
    return "String down"