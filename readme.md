# 深度学习训练数据和测试数据文件列表制作
使用脚本对自己的图片数据分为训练集和测试集，并制作列表文件
#
脚本以sh和python文件编写，清单如下，附有个文件说明   
* Images：包含原始图片的文件夹  
* lmarks：对应于原始图片文件的特征点
* create_lmarks_pts.sh：由特征点存放文件生成对应的特征点列表清单
* create_key.sh：生成图片文件名(如000)存放的列表清单
* create_nonlabels.sh：生成图片文件对应的没有标记的列表清单，方便使用脚本对该文件分为训练集和测试集，再生成标记
* image_key.py：和上create_key.sh功能一样
* lmarknew.py：检测并生成特征点文件
* result.py：将image_key,image_path_name,lmarks_path_name存放到一个文件内
* train_test_split.py：对result.py生成的文件分为训练数据和测试数据，同时进行标签。所有数据随机打乱，80%作为训练数据，20%作为测试数据。


## 补充内容说明
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

11. train_test_split.py  
由已经生成的所有文件的列表和标签文件，将文件分为训练集和测试集，分别保存为train.txt, test.txt
