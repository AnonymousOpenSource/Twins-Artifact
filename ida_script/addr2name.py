# -*-coding:utf-8-*-

import idaapi
import idc
import pickle
import os
import idautils
from idaapi import get_func
import ida_nalt
import decimal



idaapi.auto_wait()

addr2name = {}
for seg_ea in Segments():
    if idc.get_segm_name(seg_ea) != ".text":
        continue
    text_start, text_end = get_segm_start(seg_ea), get_segm_end(seg_ea)
    for function_ea in Functions(text_start, text_end):
        funcname = get_func_name(function_ea)
        addr2name[hex(function_ea)] = funcname
with open("addr2name.pkl", "wb") as f:
    pickle.dump(addr2name, f)

idc.qexit(0)