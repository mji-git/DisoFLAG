# -*- coding: utf-8 -*-
# @Author: Yihe Pang
# @Date:   2023-06-12 11:54:07
# @Last Modified by:   Yihe Pang
# @Last Modified time: 2023-06-14 15:16:27
import sys
import os
import numpy as np
import datetime
import random
from protTrans.features_gene_T5 import get_embedding_T5
import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    args = sys.argv
    input_file_name = args[1] # input fasta file
    name = input_file_name.split("/")[-1].split(".")[0]
    print("Processing name:", name)

    # feature path
    nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M")
    randomNum=random.randint(0,10)
    T5_embedding_path = f'./temp/embeddings/T5/{name}'
    
    if not os.path.isdir(T5_embedding_path):
        os.makedirs(T5_embedding_path)

    get_embedding_T5(input_file_name, T5_embedding_path)
