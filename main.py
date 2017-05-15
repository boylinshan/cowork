# -*- coding: utf-8 -*-
import Globals

from web.lib.flask import Flask
from web.module.cluster import clusterPage

app = Flask(__name__, static_url_path='/web/static', static_folder='web/static')
app.register_blueprint(clusterPage)

if __name__ == '__main__':
    # Globals.CLUSTER =
    app.run(debug=True)
