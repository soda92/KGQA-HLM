# -*- coding: utf-8 -*-
from ltp import LTP


def cut_words(words):
    ltp = LTP()
    seg, hidden = ltp.seg([words])
    pos = ltp.pos(hidden)
    return seg, pos


def get_target_array(words):
    arr = []
    seg, pos = cut_words(words)
    for k in zip(seg[0], pos[0]):
        if k[1] in ('nh', 'n'):
            arr.append(k[0])
    return arr
