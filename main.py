import os.path
import re
import jieba
import numpy as np
from collections import Counter
import sys

# 读取文件
def load_text(text_path):
    # 打开文件
    text_file = open(text_path, 'r', encoding='utf-8')
    # 读取文件
    all_text = text_file.read()
    # 返回字符串
    return all_text
# 过滤掉符号只剩中文
def filter_text(text):
    # 过滤中文符号和英文字母
    sep = "[^\u4e00-\u9fa5]"
    # 使用re库的sub函数进行替换
    finish_text = re.sub(sep, '', text)
    return finish_text
# 提取关键词
def get_import(text):
    finish_text = jieba.lcut(text)
    return finish_text
# 进行相似度比较
def compare(str1,str2):
    # 统计各个关键字的个数
    str1_num = (Counter(str1))
    str2_num = (Counter(str2))
    str1_array = []
    str2_array = []
    # 统计关键字的频率
    for temp in set(str1 + str2):
        str1_array.append(str1_num[temp])
        str2_array.append(str2_num[temp])
    # 把列表化为数组
    str1_array = np.array(str1_array)
    str2_array = np.array(str2_array)
    # 余弦相似度算法
    result = str1_array.dot(str2_array) / (np.sqrt(str1_array.dot(str1_array)) * np.sqrt(str2_array.dot(str2_array)))
    # 数组转为浮点数，保留两位小数
    num = np.float64(np.around(result,decimals=2)).item()
    return  num

# 输出
def output(number):
    # float转字符串
    str0 = str(number)
    # 获取输出路径
    output_path = sys.argv[3]
    # 打开文件
    openfile = open(output_path,'w',encoding='utf-8')
    # 写入
    openfile.write(str0)
    #关闭文件
    openfile.close()


def main():
    original_text = sys.argv[1]
    Plagiarism_text = sys.argv[2]
    text1 = load_text(original_text)
    text2 = load_text(Plagiarism_text)
    text11 = filter_text(text1)
    text22 = filter_text(text2)
    text111 = get_import(text11)
    text222 = get_import(text22)
    result = compare(text111,text222)
    print(result)
    output(result)
    return result

if __name__ == '__main__':
    main()
