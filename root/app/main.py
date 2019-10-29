# coding: utf-8
from flask import render_template, make_response, request, redirect, url_for, Blueprint, current_app as app
from math import ceil
from .data import PTList, targetList, imglist, bonelist

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
  AC_PER_PAGE = 4
  # Fetch announcement from db and sort it by date
  announcements = list(app.config['MONGO_COLLECTION_ANNOUNCEMENT'].find({}, {'_id': False}).sort('date', -1))
  # Page the list per 4 announcements
  total_pages =  ceil(len(announcements) / AC_PER_PAGE)
  res = make_response(render_template("home/home.jinja2", ac_per_page=AC_PER_PAGE, announcements=announcements, total_pages=total_pages, PTList=PTList, imglist=imglist, metacontent=u"佳里汪骨外科診所為大北門地區第一間骨外科診所，本網站提供汪骨外科看診時間，最新公告以及地址。"))
  res.headers['Link'] = '</static/img/front.jpg>; as=image; rel=preload, </static/img/map.png>; as=image; rel=preload'
  return res

@main.route("/target")
def target():
  return render_template("home/targetpage.jinja2", targetList=targetList, metacontent=u"汪骨外科診所的主治項目。") 

@main.route("/boneMassMeasurement")
def boneMassMeasurement():
  return render_template("home/boneMassMeasurement.jinja2", bonelist=bonelist, metacontent=u"汪骨外科診所提供的骨質密度檢測。")

@main.route("/google8029c7599236ab79.jinja2")
def comfirm():
  return render_template("google8029c7599236ab79.jinja2")
