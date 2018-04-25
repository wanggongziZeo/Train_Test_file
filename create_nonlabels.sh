#!/usr/bin/env sh
# 对扩充的样本创建列表标签文件。比如其中一幅图像存放为:
# output/0/000/000_rendered_aug_-00_00_01.jpg 0
DATA=/home/kb402/project/output
MY=/home/kb402/project

echo "Create AugNonLabels.txt..."
rm -rf $MY/AugNonLabels.txt
for i in $(ls $DATA)
do
for j in $(ls $DATA/$i)
do
find $DATA/$i/$j -name *.jpg | cut -d '/' -f5-9 >>$MY/AugNonLabels.txt
done
done

echo "All Done"
