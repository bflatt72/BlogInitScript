#!/usr/local/bin/ python3

import time, os, glob, subprocess


title = input("Title:   ")
cat = input("Category:  ")
tags = input("Tags:  ")
d = time.strftime('%Y-%m-%d')

path = "/Users/FlattDev/Documents/Blog/bflatt72.github.io/_posts"

os.chdir(path)

f = open("%s-%s.md" % (d, title), "w+")

print("---", file=f)
print("layout: post", file=f)
print("Title: %s\r" % title, file=f)

if cat: print("Categories: %s\r" % cat, file=f)
if tags: print("Tags: %s\r" % tags, file=f)
print("---", file=f)
f.close()

list_of_files = glob.glob('/users/FlattDev/Documents/Blog/bflatt72.github.io/_posts/*.md')
latest_file = max(list_of_files, key=os.path.getctime)

subprocess.call(['code', latest_file])

