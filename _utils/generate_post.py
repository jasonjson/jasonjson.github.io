#!/usr/bin/python3


import os
import datetime as dt
import sys
import argparse

def generate_post(input_file):
    """Description
    generate a post
    @param param:  Description
    @type  param: string

    @return:  Description
    @rtype :  Type

    @raise e:  Description
    """

    today_date = dt.datetime.today().strftime("%Y-%m-%d")
    problem_num = input_file.split(".")[0]
    problem_name = input_file.split(".")[1].title()
    title = problem_name.replace("-", " ")
    output_file = '-'.join([today_date, problem_name.lower()]) + ".markdown"
    post = ['---', 'layout: post', 'title: {} - {}'.format(problem_num, title), 'date: {0}'.format(today_date), 'tags:', '- Leetcode', 'categories:', '- ' , "author: Jason", '---']
    with open (input_file, "r") as input:
        lines = input.read()
    with open (output_file, 'w') as output:
        output.write('\n'.join(post))
        output.write('\n\n```python\n' + lines + '```')

    os.remove(input_file)

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='add new post')
    parse.add_argument('filename', help="input filename")
    args = parse.parse_args()

    generate_post(args.filename)
