# -*- coding: utf-8 -*-
from lib.flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

entryPage = Blueprint('entry_page', __name__, template_folder='templates')

@entryPage.route('/', defaults={'page': 'index'})
@entryPage.route('/<page>')
def show(page):
	print(page, file=sys.stderr)
	try:
		return render_template('pages/%s.html' % page)
	except TemplateNotFound:
		return page
