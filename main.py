# -*- coding: utf-8 -*-
from lib.flask import Flask
from blueprint.entryPage import entryPage
from blueprint.testPage import testPage
from scripts.check_vm_status import get_cpu_idle

app = Flask(__name__)
app.register_blueprint(entryPage)
app.register_blueprint(testPage)


host = [

        'systest-site1-deployer',
        'systest-site1-forward1',
        'systest-site2-forward1',
        'systest-site-master',
        'systest-site1-idx1',
        'systest-site1-idx2',
        'systest-site1-idx3',
        'systest-site1-idx4',
        'systest-site1-idx5',
        'systest-site2-idx1',
        'systest-site2-idx2',
        'systest-site2-idx3',
        'systest-site1-sh1',
        'systest-site1-sh2',
        'systest-site1-sh3',
        'systest-site2-sh1',
        'systest-site-spare'

        # 'sta-site-fwd1',
        # 'sta-site-fwd2',
        # 'sta-site-deployer',
        # 'sta-site-master',
        # 'sta-site1-idx1',
        # 'sta-site1-idx2',
        # 'sta-site1-idx3',
        # 'sta-site1-idx4',
        # 'sta-site1-idx5',
        # 'sta-site2-idx1',
        # 'sta-site2-idx2',
        # 'sta-site2-idx3',
        # 'sta-site1-sh1',
        # 'sta-site1-sh2',
        # 'sta-site1-sh3',
        # 'sta-site2-sh1',
        # 'sta-site-spare'

        # '10.66.130.2',
        # '10.66.130.3',
        # '10.66.138.75', ### forward2
        # '10.66.129.192',
        # '10.66.129.195',
        # '10.66.129.83',
        # '10.66.129.209',
        # '10.66.129.85',
        # '10.66.129.139',
        # '10.66.129.75',
        # '10.66.128.122',  ### site1-sh2
        # '10.66.129.91',
        # '10.66.137.164',
        # '10.66.137.162',
        # '10.66.137.165',
        # '10.66.137.163',
        # '10.66.138.48'
    ]


if __name__ == '__main__':
    # app.run(debug=True)
    for h in host:
        print get_cpu_idle(h, 'root', 'sp1unk', 22, 'Cpu')