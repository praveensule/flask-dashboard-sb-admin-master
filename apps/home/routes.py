# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request ,jsonify
#from werkzeug import secure_filename
from flask_login import login_required
from jinja2 import TemplateNotFound

@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

@blueprint.route('/saveFile', methods=['GET', 'POST'])
def saveFile():
    print("test-->"+request.method)
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        #f.save(secure_filename(f.filename))
        d = "{'response':'success'}"
        return jsonify(d)
    else :
        d = "{'response':'failure'}"
        return jsonify(d)

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
