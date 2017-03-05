#!/Users/yuanyuanliu/miniconda3/bin/python

import datetime as dt
import sys

def generate_post(title):
    today_date = dt.datetime.today().strftime("%Y-%m-%d")
    filename = '../_posts/' + '-'.join([today_date, title]) + ".markdown"
    post = ['---', 'layout: post', 'title: {0}'.format(title), 'date: {0}'.format(today_date), 'tags:', '- ', 'categories:', '- ' , "author: Jason", '---', '<p><strong><em>header</em></strong></p>']
    with open (filename, 'w') as output:
        output.write('\n'.join(post))

if __name__ == "__main__":
    title = sys.argv[1]
    generate_post(title)
