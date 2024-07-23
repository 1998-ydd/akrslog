"""
# 我的第一个应用
这是我们首次尝试使用数据创建表格：
"""

import streamlit as st
import pandas as pd
import re


def gendict(namelist:list)->dict:
    return {item:[] for item in namelist}

def get_process(Dict,line):    
    try:
        pattern = r'[-]?\d{3,}\.\d{1,}'
        matches = re.findall(pattern, line)
        keys = [i for i in Dict]
        if len(matches) == 2:
            Dict["time"].append(line.split()[0] + " " + line.split()[1])
            for i,j in zip(keys[1:],matches):
                Dict[i].append(j)
        else:
            print(line)
            print(f"列表长度出错：{len(matches)}")
    except Exception as e:
        # 当发生异常时，执行此代码块
        print(line)
        print("发生了一个错误：", e)
        
def get_MapPos(Dict,line):    
    try:
        pattern = r'\[\d{1,}\,\s*\d{1,}\]'
        matches = re.findall(pattern, line)
        matches = re.findall(r'\d+',matches[0])
        keys = [i for i in Dict]
        if len(matches) == 2:
            Dict["time"].append(line.split()[0] + " " + line.split()[1])
            for i,j in zip(keys[1:],matches):
                Dict[i].append(j)
        else:
            print(line)
            print(f"列表长度出错：{len(matches)}")
    except Exception as e:
        # 当发生异常时，执行此代码块
        print(line)
        print("发生了一个错误：", e)
#工艺参数
keyword_process = [
        "LeftBondModule - 当前力控值",
        "记录上次键合位置为",
        "当前键合位置Map坐标为",
]
Process = gendict(["time","Force","High"])

uploaded_file = st.file_uploader("上传日志文件", type=["txt", "log"])

if uploaded_file is not None:
    for line in uploaded_file:
        if keyword_process[0] in line:
            get_process(Process,line)
    df = pd.DataFrame(Process)
    st.table(df)
