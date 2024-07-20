"""
# 我的第一个应用
这是我们首次尝试使用数据创建表格：
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  '第一列': [1, 2, 3, 4,5],
  '第二列': [10, 20, 30, 40,50]
})

df