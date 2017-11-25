#coding:utf-8
import pymysql
from jinja2 import Environment,FileSystemLoader
import os,sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

PATH = os.path.dirname(os.path.abspath(__file__))

#设置jinja2的环境(trim_blocks=True,lstrip_blocks = True,去掉jinja2产生的空行)
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=True,lstrip_blocks = True)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_index_html(tableName,data):
    fname = "results/%s.js"%tableName
    context = {
    	'tableName':tableName,
        'data':data
    }
    with open(fname, 'w') as f:
        html = render_template('index.html', context)
        f.write(html) 

def main():
	data=[]
	data.push(1)
	data.push(2)
    create_index_html("test",data)

########################################
if __name__ == "__main__":
    main()
    




