#!/usr/local/bin/python3

import datetime as dt
import sys
import argparse

def generate_post(title):
    """Description
    generate a post
    @param param:  Description
    @type  param: string

    @return:  Description
    @rtype :  Type

    @raise e:  Description
    """
    today_date = dt.datetime.today().strftime("%Y-%m-%d")
    filename = '_posts/' + '-'.join([today_date, title.replace(' ', '-')]) + ".markdown"
    post = ['---', 'layout: post', 'title: {0}'.format(title), 'date: {0}'.format(today_date), 'tags:', '- ', 'categories:', '- ' , "author: Jason", '---', '**title**']
    with open (filename, 'w') as output:
        output.write('\n'.join(post))

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='add new post')
    parse.add_argument('title', help="post title as a string")
    args = parse.parse_args()

    generate_post(args.title)
