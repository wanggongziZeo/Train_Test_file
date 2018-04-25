#-*- coding:utf-8 -*-
# 将三个文件(txt)的内容进行拼接
# 各文件每一行存放在新文件的每一行
# results1.txt：先将前两个文件进行拼接生成
# result.list：最终生成的新的文件列表，保存为list文件
# 打开文件path_to_images.txt（可读），作为fa
# 打开文件path_to_landmarks.txt（可读），作为fb
# 同时需要打开文件image_key.txt（可读），作为fc
# 创建新文件result.txt（可写），作为fd
with open('path_to_images.txt','r') as fa:  
    with open('path_to_landmarks.txt','r') as fb:  
        with open('result1.txt','w') as fc:  
            for line in fa:  
                fc.write(line.strip('\r\n')+',')
                fc.write(fb.readline()) 

with open('image_key.txt','r') as fa:  
    with open('result1.txt','r') as fb:  
        with open('result.list','w') as fc:  
            for line in fa:  
                fc.write(line.strip('\r\n')+',')
                fc.write(fb.readline()) 
