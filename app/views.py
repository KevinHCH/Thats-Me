import os
import html

from flask import (render_template, jsonify,
									 request, send_from_directory,
									 send_file, redirect,
									 url_for, make_response,
									 flash)
from werkzeug.utils import secure_filename
from pathlib import Path
from app import utils as ut

from datetime import datetime
from pathlib import Path

from . import db
from pprint import pprint

handler = db.get_db()


def index():
	return render_template("public/index.html")
"""
Funcion que se ejecutaria en todas las peticiones
"""
def router_middleware():
	if request.path.startswith("/admin"):
		return redirect(url_for("admin_login"))
	pass

def is_authenticated():
	if request.cookies.get("auth") is None: 
		return redirect(url_for("admin_login"))

def is_admin(email, password):
	query = '''select * 
					 	 from users 
						 where concat(mail_handle,'@',mail_server) = %s
						 and password = %s 
						 and role_id = 1'''
	
	handler.execute(query, [email, password])
	user = handler.fetchone()
	
	return user if user else False

def is_set_cookie(cookie):
	query = '''select cookie
							from users
							where cookie = %s'''
	handler.execute(query, [cookie])
	user = handler.fetchone()

	return user if user else False

def set_admin_cookie(user_id, cookie):
	query = '''update users
							set cookie = %s
							where id = %s'''
	handler.execute(query, [cookie, user_id])
	handler.connection.commit()
	return True if handler.rowcount > 0 else False
	
def insert_image(*args):
	name, path, tags, user_id = args
	query = '''INSERT INTO public.photos
					("name", "path", tags, user_id)
					VALUES (%s,%s,%s,%s)'''
	handler.execute(query,[name, path, tags, user_id])
	handler.connection.commit()
	pass

def save_description(description):
	query = '''
						update users
						set description = %s
						where id = %s
					'''
	user_id = request.cookies.get("uid")
	handler.execute(query, [description, user_id])
	handler.connection.commit()
	
def get_description():
	query = '''select description from users where id = 2'''
	# handler.execute(query,[user_id])
	handler.execute(query)
	return handler.fetchone()["description"]

def index_admin():
	cookie = request.cookies.get("auth")
	if request.path.startswith("/admin") and not cookie:
		return redirect(url_for("admin_login"))

	return render_template("admin/index.html")

def admin():
	if request.path.startswith("/admin") and request.method == "POST":
		
		user_email = request.form.get("email")
		password = request.form.get("password")

		admin = is_admin(user_email, password)
		
		if admin:
			month = 3600 * 24 * 30
			cookie = ut.md5(f"__::{admin['id']}:_:{admin['mail_handle']}::__")
			set_admin_cookie(admin['id'], cookie)
			response = make_response(redirect(url_for("index_admin")))	
			response.set_cookie("auth", cookie, month)
			response.set_cookie("uid", str(admin["id"]), month)
			
			return response
		else:
			flash("The email or password are invalid, try it again.")
			return render_template("admin/login.html")

	if request.cookies.get("auth") is None: 
		return redirect(url_for("admin_login"))
	else:
		cookie = request.cookies.get("auth")
		user = is_set_cookie(cookie)
		return redirect(url_for("index_admin")) if user else redirect(url_for("admin_login"))


def admin_login():
	return render_template("admin/login.html")

def add_img():
	STORAGE_PATH = Path().cwd() / "storage" 
	current_date = datetime.now().strftime("%Y%m%d")
	is_authenticated()
	if request.method == "POST":
		name = request.form.get("name")
		tags = request.form.get("tags")
		img = request.files["img"]

		extension = img.filename[img.filename.rfind("."):]
		img_name = secure_filename(f"{current_date}_{name}{extension}")
		img.save(f"{STORAGE_PATH}/{img_name}")
		user_id = request.cookies.get("uid")
		insert_image(name, img_name, tags, user_id)
		flash('The image is saved')
		return redirect(url_for("add_img"))
		
	return render_template("admin/addImages.html")

def edit_about():
	if request.method == "POST":
		description = html.escape(request.form.get("editor"))
		save_description(description)
		flash("Your description has been updated")
	
	user_id = request.cookies.get("uid")
	current_description = html.unescape(get_description())
	
	return render_template("admin/editAboutMe.html", description=current_description)

def about():
	description = html.unescape(get_description())
	return render_template("public/about.html", description=description)

def list_all_images():
	query = "select name, path from photos"
	handler.execute(query)
	imgs = handler.fetchall()
	return render_template("public/images.html", imgs=imgs)
	