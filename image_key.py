#-*- coding:utf-8 -*-
# 生成图片名文件，如001
import os
filename = 'path_to_landmarks.txt'
imagekey = 'image_key.txt'

filee = open(filename)
lines = filee.readlines()
for line in lines:
	head,tail = os.path.split(line)
	tail = tail.split('.')[0]
	f = file(imagekey, 'a+')
	f.write(tail+'\n')
filee.close()
