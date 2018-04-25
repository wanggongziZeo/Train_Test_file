#-*- coding:utf-8 -*-
# 生成特征点文件path_to_landmarks.txt
import sys
import os
import ntpath
import io
import cv2
import dlib
import shutil
import utils

# 读取图片列表清单，并生成相应的文件夹
# tmp_ims：存放裁剪的图片
# tmp_detect： 存放检测到的人脸图片，人脸边界，人脸68个特征点
if len(sys.argv) < 3 or len(sys.argv) > 5 :
		print "Usage: python testBatchModel.py <inputList> <outputDir>"
		exit(1)
fileList = sys.argv[1]
data_out = sys.argv[2]
needCrop = 1
trg_size = 250
predictor_path = "dlib_model/shape_predictor_68_face_landmarks.dat"
if len(sys.argv) > 3:
	needCrop = bool(sys.argv[3]=='1')
useLM = 1
if len(sys.argv) > 4:
	useLM    = bool(sys.argv[4]=='1')
if not os.path.exists(data_out):
	os.makedirs(data_out)
if needCrop:
	detector = dlib.get_frontal_face_detector()
	#if os.path.exists("lmarks/0"):
	#	shutil.rmtree('lmarks/0')
	#os.makedirs("lmarks/0")
	if useLM:
		predictor = dlib.shape_predictor(predictor_path)
# 创建保存新的文件名的文件lists.txt
path_to_landmarks = 'path_to_landmarks.txt'

##### Prepare images ##############################
with open(fileList, "r") as ins:
    for image_path in ins:
		path_to_image = image_path	# Images/0/011.jpg
		image_path = image_path[:-1]
		imname = ntpath.basename(image_path)
		imname = imname.split(imname.split('.')[-1])[0][0:-1]	# 011, 031
		head, tail = os.path.split(path_to_image)
		subname = head.split('/')[-1]
		image_key = imname	# image_key：011
		## 由上image_key, path_to_image有了
		path_to_lmarks_name = path_to_image.split('.')[0]
		## path_to_lmarks_name也有了
		
		subfilenamelmarks = 'lmarks/{}'.format(str(subname))
		# 创建保存特征点的文件和子文件
		if not os.path.exists(subfilenamelmarks):
			os.makedirs(subfilenamelmarks)
		
		img = cv2.imread(image_path)
		## If we do cropping on the image
		if needCrop:
			dlib_img = cv2.imread(image_path)
			img2 = cv2.copyMakeBorder(img,0,0,0,0,cv2.BORDER_REPLICATE)
			dets = detector(img, 1)
			if len(dets) == 0:
				print '> Could not detect the face, skipping the image...' + image_path
				# count += 1
				continue
			f = file(path_to_landmarks, 'a+')
			f.write(path_to_image)
			detected_face = dets[0]
			cv2.rectangle(img2, (detected_face.left(),detected_face.top()), \
				(detected_face.right(),detected_face.bottom()), (0,0,255),2)
			if useLM:
				shape = predictor(dlib_img, detected_face)
				nLM = shape.num_parts
				fileout = open(subfilenamelmarks+'/'+imname+".pts","w")
				for i in range(0,nLM):
					fileout.write("%f %f\n" % (shape.part(i).x, shape.part(i).y))
				fileout.close()		
