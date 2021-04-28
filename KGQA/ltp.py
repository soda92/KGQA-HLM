# -*- coding: utf-8 -*-
import ltp
import os
LTP_DATA_DIR = 'D:/code/research/Down/ltp-model-tiny'  # ltp模型目录的路径


def cut_words(words):
    segmentor = ltp.Segmentor()
    seg_model_path = os.path.join(LTP_DATA_DIR, 'ltp.model')
    segmentor.load(seg_model_path)
    words = segmentor.segment(words)
    array_str = "|".join(words)
    array = array_str.split("|")
    segmentor.release()
    return array


def words_mark(array):
    # 词性标注模型路径，模型名称为`pos.model`
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
    postagger = ltp.Postagger()  # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    postags = postagger.postag(array)  # 词性标注
    pos_str = ' '.join(postags)
    pos_array = pos_str.split(" ")
    postagger.release()  # 释放模型
    return pos_array


def get_target_array(words):
    target_pos = ['nh', 'n']
    target_array = []
    seg_array = cut_words(words)
    pos_array = words_mark(seg_array)
    for i in range(len(pos_array)):
        if pos_array[i] in target_pos:
            target_array.append(seg_array[i])
    target_array.append(seg_array[1])
    return target_array
