# -*- coding: utf-8 -*-
import const
import Globals

from lib.flask import Flask
from blueprint.entryPage import entryPage
from blueprint.testPage import testPage
from scripts import test
from tools import methods

import os

# from scripts.check_vm_status import get_cpu_idle

app = Flask(__name__)
app.register_blueprint(entryPage)
app.register_blueprint(testPage)


if __name__ == '__main__':
    Globals.vm_info = methods.init_env()
    print 2
    # Globals.cluster = methods.parse_yml_config_file(name='stability_multisite')
    app.run(debug=True)
