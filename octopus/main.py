#_*_ coding: utf-8 _*_

###########################
# des: octopus
# author: lucheng
###########################

import os
import sys

from prettytable import PrettyTable as PT

from nodes import NodeHandler

PROJ_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.pardir)
TR_NUM, _ = os.popen('stty size', 'r').read().split()
LOGO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf/logo.txt')
LOGO = open(LOGO_FILE).read()
ROW_NUM = int(int(TR_NUM)*2/3)


def color_print(p_str, color='white'):
    if color in ['red', 'r']:
        print('\033[1;31;40m{}\033[0m'.format(p_str))
    elif color in ['green', 'g']:
        print('\033[1;32;40m{}\033[0m'.format(p_str))
    elif color in ['yellow', 'y']:
        print('\033[1;33;40m{}\033[0m'.format(p_str))
    elif color in ['blue', 'b']:
        print('\033[1;36;40m{}\033[0m'.format(p_str))
    else:
        print('\033[1;37;40m{}\033[0m'.format(p_str))


class Octopus(object):
    def home(self):
        home_choices = {
            '1': 'Setup K8S cluster',
            '2': 'Configure cluster',
            '3': 'Deploy project',
            '0': 'Exit'
        }

        os.system('clear')
        print(''.center(ROW_NUM, '-'))
        print(LOGO)
        print(''.center(ROW_NUM, '='))
        for k, v in home_choices.items():
            print('> {}: {}'.format(k, v))
        print(''.center(ROW_NUM, '-'))

        choice = input('>> ')
        if choice == '0':
            sys.exit()
        elif choice == '2':
            self.conf()
        else:
            self.home()

    def conf(self):
        conf_choices = {
            '1': 'Add node',
            '2': 'Del node',
            '3': 'Back to home',
            '0': 'Exit'
        }

        os.system('clear')
        print(''.center(ROW_NUM, '-'))
        print('Cluster node infos ...')
        print(''.center(ROW_NUM, '='))

        node_table = PT()
        node_table.field_names = ["hostname", "ip(x.x.x.x/y)", "NIC", "node type"]
        nodes = NodeHandler().get()
        for k, v in nodes.items():
            node_table.add_row([v['hostname'], '{}/{}'.format(k, v['netmask']), v['nic'], v['node_role']])
        print(node_table)

        for k, v in conf_choices.items():
            print('> {}: {}'.format(k, v))
        print(''.center(ROW_NUM, '-'))

        choice = input('>> ')
        if choice == '0':
            sys.exit()
        elif choice == '3':
            self.home()
        else:
            self.conf()


if __name__ == '__main__':
    octopus = Octopus()
    octopus.home()

