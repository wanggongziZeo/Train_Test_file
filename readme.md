# 内容说明
1. Images文件夹  
里面存放的原始图片，每种类别的图片各存一个文件夹

2. lmarks  
存放Images文件夹下各文件的特征点，由于特征点不可见缘故，该文件数量比Images文件数量少

3. path_to_images.txt  
存放文件夹Images各jpg文件的路径

4. path_to_landmarks.txt  
存放文件夹lmarks各pts文件的路径

5. create_filelist.sh  
生成文件path_to_images.txt、path_to_landmarks.txt

6. create_key.sh  
生成样本类别标签（训练集和测试集放在一起，后续分开）

7. create_lmarks_pts.sh  
生成样本特征点pts文件，文件来源于lmrks文件夹，存放在LIST文件夹下lmarks.txt

8. image_key.py  
生成图片名文件:image_key.txt，存放如001

9. lmarknew.py  
生成特征点文件path_to_landmarks.txt

10. result.py  
将三个文件(txt)的内容进行拼接  
各文件每一行存放在新文件的每一行  
results1.txt：先将前两个文件进行拼接生成  
result.list：最终生成的新的文件列表，保存为list文件

11. ## train_test_split.py  
由已经生成的所有文件的列表和标签文件，将文件分为训练集和测试集，分别保存为train.txt, test.txt
