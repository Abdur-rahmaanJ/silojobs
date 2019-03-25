

import random
from jinja2 import Environment, FileSystemLoader
import json


def generate(file_in_templates, **kwargs):
    outpath = file_in_templates
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(file_in_templates)

    output = template.render(kwargs)
    print(output, file=open(outpath, 'w', encoding='utf8'))

n1 = ['orange', 'apple', 'pear', 'grape']

def id():
    return '{}-{}'.format(random.choice(n1), random.choice(n1))

with open("data/recruiting.json", "r") as read_file:
    recruitment = json.load(read_file)

generate('index.html', page_name='index', 
    US='is-white', R='is-info', F='is-info', O='is-info', W='is-info')

generate('recruiting.html', page_name='index', datas=recruitment['data'],
    US='is-info', R='is-white', F='is-info', O='is-info', W='is-info')

generate('contact.html', page_name='index',
    US='is-info', R='is-info', F='is-info', O='is-info', W='is-info')

generate('freelancers.html', page_name='index',
    US='is-info', R='is-info', F='is-white', O='is-info', W='is-info')

generate('world.html', page_name='index',
    US='is-info', R='is-info', F='is-info', O='is-info', W='is-white')

generate('oddjobs.html', page_name='index',
    US='is-info', R='is-info', F='is-info', O='is-white', W='is-info')

print('build: ', id(), random.randint(0, 1000))