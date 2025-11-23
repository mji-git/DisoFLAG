# -*- coding: utf-8 -*-
# @Author: Yihe Pang
# @Date:   2022-05-05 15:21:05
# @Last Modified by:   Yihe Pang
# @Last Modified time: 2023-06-14 22:39:15
import numpy as np 
import os
from protT5 import protT5


def load_file_2_data(file_path, reverse=False):
	loadfile = open(file_path,"r") 	
	load_f = []
	line_id = 1
	for line in loadfile:
		line=line.strip('\n')
		load_f.append(line)
		line_id += 1
	loadfile.close()

	load_data = []
	for i in range(len(load_f)):
		if i % 2 == 0:
			load_data.append(load_f[i:i+2])    #one data:  [0]--id  [1]--seq   
	# print("load_file: ",file_path,"    data length: ",len(load_data))  

	if reverse:
		print("Reversing")
		load_data.reverse()
	print("First item:", load_data[0][1])
	return load_data

def data_feature_2_file(data, feature_path):

	
	sequences_Example = []
	for i in range(len(data)):
		sequences_Example.append(data[i][1])

	model_path = "./protTrans/prot_t5_xl_uniref50"

	for i in range(len(sequences_Example)):

		input_sequences = []
		input_sequences.append(sequences_Example[i])
		
		seq_name = data[i][0].replace('>','') 
		out_name = os.path.join(feature_path, seq_name+'.npy')
		"""
		next_seq_name = data[i+20][0].replace('>','')
		next_out_name = os.path.join(feature_path, next_seq_name+'.npy')
		if os.path.exists(next_out_name):
			print("next out name exists, assuming another process is running, terminating 1 early before:", out_name, next_out_name)
			return
		"""
		if not os.path.exists(out_name) and len(sequences_Example[i]) <= 2000:
		# if not os.path.exists(feature_path + seq_name+'.npy'):

			features = protT5(model_path,input_sequences)
			# print("success one:",features)

			if not os.path.isdir(feature_path):
				os.makedirs(feature_path)
			
			np.save(out_name, features[0])
			# print("finish write....",seq_name)
		else:
			print("pass likely exists:", out_name)


def get_embedding_T5(data_file,feature_path):
	test_data = load_file_2_data(data_file)
	print("processing sequences:",len(test_data))
	data_feature_2_file(test_data, feature_path)

