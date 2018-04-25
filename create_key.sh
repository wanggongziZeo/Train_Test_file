#!/usr/bin/env sh
# 生成样本类别标签（训练集和测试集放在一起，后续分开）
DATA=/home/kb402/project/path_to_landmarks.txt
MY=/home/kb402/LIST

echo "Create image_key.txt..."
rm -rf $MY/image_key.txt
find $DATA -name *.pts | cut -d '/' -f7 >>$MY/image_key.txt


echo "All done"
