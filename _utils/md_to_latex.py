#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def convert(path, latex_file):
    with open(latex_file, "a+") as output:
        files = os.listdir(path)
        files.sort(reverse=True)
        for f in files:
            found = False
            with open(f, "r") as input:
                title = ""
                for line in input.readlines():
                    if "title" in line:
                        title = line.strip()
                        continue
                    if line.strip() == "``` python" or line.strip() == "```python":
                        output.write("\\newpage\n\\section{" + title + "}\n")
                        output.write("\\begin{lstlisting}\n")
                        found = True
                    elif found:
                        if line.strip() == "```":
                            output.write("\\end{lstlisting}\n")
                            break
                        else:
                            output.write(line)

convert(".", "code_latex")
