#!/usr/bin/env sh
# 生成样本特征点pts文件，文件来源于lmrks文件夹，存放在LIST文件夹下
DATA=/home/kb402/face_augmentation/lmarks
MY=/home/kb402/LIST

echo "Create lmarks.txt..."
rm -rf $MY/lmarks.txt
for i in $(seq 0 24)
do
find $DATA/$i -name *.pts | cut -d '/' -f5-9 >>$MY/lmarks.txt
done
echo 'Done'
