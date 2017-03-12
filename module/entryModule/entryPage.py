# -*- coding: utf-8 -*-
from lib.flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from tools.LogManager import LogManager

entryPage = Blueprint('entry_page', __name__, template_folder='templates')

@entryPage.route('/', defaults={'page': 'index'})
@entryPage.route('/<page>')
def show(page):
	a = LogManager().get_logger(__name__)
	a.info(page)
	try:
		return render_template('pages/%s.html' % page)
	except TemplateNotFound:
		return page
