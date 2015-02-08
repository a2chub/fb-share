#!/usr/bin/env python
#coding:utf-8

from google.appengine.ext.webapp.util import run_wsgi_app

from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)

@app.route('/#/api/article/<id>')
@app.route('/api/article/<id>')
def api(page_type='default', id=000):
  ret_data = {'id':id}
  return json.dumps( ret_data )

@app.route('/')
@app.route('/article/<page_id>')
@app.route('/#/article/<page_id>')
def index(page_id=0):
  print "+" * 80
  print page_id
  print "+" * 80
  if page_id == 0:
     ret_data = {'page_id':str(page_id),
      "og_image": "http://possible-fabric-792.appspot.com/img/top.png",
      "og_site_name" : "top site name",
      "og_title" : u"ここはトップよん",
      "og_desc" : u"fbが動的なページとtopページをクロール仕分けてくれるか",
      "og_url" : "http://possible-fabric-792.appspot.com/article/%s"%(page_id)
    }
  else:
    ret_data = {'page_id':str(page_id),
       "og_image": "http://possible-fabric-792.appspot.com/img/article.png",
       "og_site_name" : u"記事のサイトですぇ",
       "og_title" : u"%s番目の記事ページ"%(page_id),
       "og_desc" : u"fbが動的なページとtopページをクロール仕分けてくれるか",
       "og_url" : "http://possible-fabric-792.appspot.com/article/%s"%(page_id)
    }

  return render_template("index.html", ret_data = ret_data )

if __name__ == '__main__':
  run_wsgi_app(app)

