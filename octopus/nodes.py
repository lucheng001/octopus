#_*_ coding: utf-8 _*_

###########################
# des: octopus
# author: lucheng
###########################

import os
import sys
import yaml

PROJ_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.pardir)
NODE_FILE = os.path.join(PROJ_DIR, 'scripts/setup_k8s/group_vars/all.yml')


class NodeHandler(object):
    def __init__(self):
        f = open(NODE_FILE)
        self.data = yaml.safe_load(f).get('nodes', {})

    def get(self):
        return self.data

if __name__ == '__main__':
    print(NodeHandler().get())
