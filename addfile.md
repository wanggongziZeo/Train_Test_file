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