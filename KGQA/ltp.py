# -*- coding: utf-8 -*-
from ltp import LTP

def cut_words(words):
    ltp = LTP()
    seg, hidden = ltp.seg([words])
    pos = ltp.pos(hidden)
    return seg, pos


def get_target_array(words):
    target_pos = ['nh', 'n']
    target_array = []
    seg_array,pos_array = cut_words(words)
    for i in range(len(pos_array)):
        if pos_array[i] in target_pos:
            target_array.append(seg_array[i])
    target_array.append(seg_array[1])
    return target_array
