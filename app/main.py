# coding: utf-8
from flask import render_template, request, redirect, url_for, Blueprint
from .data import PTList,targetList,imglist,bonelist

# APIkey=app.config.get("APIKEY")
main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
  return render_template("home.html", PTList=PTList, imglist=imglist, metacontent=u"汪骨外科診所為大北門地區第一間骨外科診所，旨在提供病患最有效的骨外科治療．")

@main.route("/target")
def target():
  return render_template("targetpage.html", targetList=targetList, metacontent=u"汪骨外科診所的主治項目．") 

@main.route("/boneMassMeasurement")
def boneMassMeasurement():
  return render_template("boneMassMeasurement.html", bonelist=bonelist, metacontent=u"汪骨外科診所提供的骨質密度檢測．")

@main.route("/google8029c7599236ab79.html")
def comfirm():
  return render_template("google8029c7599236ab79.html")

@main.route("/sitemap.xml")
def sitemap():
  return render_template("sitemap.xml")
