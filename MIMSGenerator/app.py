#!/usr/bin/env python

import string
import random
import shelve
import os
from subprocess import check_output
import flask
from flask import request, abort
from os import environ

app = flask.Flask(__name__)
app.debug = True

meme_db = shelve.open("meme.db")
shortUrlDict={}
meme_id = 0;
###
# Home Resource:
# Only supports the GET method, returns a homepage represented as HTML
###
@app.route('/', methods=['GET'])
def home():
    """Builds a template based on a GET request"""
    return flask.render_template(
            'meme.html')

###
# Home Resource:
# Only supports the GET method, returns a homepage represented as HTML
###
@app.route('/about', methods=['GET'])
def about():
    """Builds a template based on a GET request"""
    return flask.render_template(
            'about.html')
    
###
# Random character generator:
# Helper function to automatically spit out a short URL path"
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

###
# Meme Generator
# Will save the Memes in the dictionary
###
@app.route('/saveMeme', methods=['POST'])
def saveMeme():
    id = id_generator()#'''"lui.gi/"+ ''' 
    img = request.form['img'];
    topText = request.form['top']
    bottomText = request.form['bottom']
    meme = []
    meme.append(topText)
    meme.append(img)
    meme.append(bottomText)
    meme_db[id]=meme
    return id

@app.route('/meme')
def meme():
    return flask.render_template("meme.html")
   
@app.route('/meme/<path:url>', methods=["GET"])
def getMeme(url):
      """Redirects to the meme after looking up the association if it exists. Otherwise throws error"""
      if isinstance(url, unicode):
          url = url.encode('utf-8')
      try:
        meme=meme_db[url]
      except KeyError:
        meme="error"        
      if(meme=="error"):
        return flask.render_template('error.html'), 404       
      else:
        img = meme[1]
        top = meme[0]
        bottom = meme[2]
        return flask.render_template("memeTemplate.html",img=img, top=top, bottom=bottom)
    
if __name__ == "__main__":
   # app.run(port=int(environ['FLASK_PORT']))
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  
    
