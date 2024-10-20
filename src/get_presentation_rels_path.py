import os
from zipfile import ZipFile

def get_presentation_rels_path(pptx_file: str) -> str:
    """
    获取presentation.xml.rels文件的路径。
    
    :param pptx_file: PPTX文件的路径
    :return: presentation.xml.rels文件的绝对路径
    """
    # 检查文件是否存在
    if not os.path.isfile(pptx_file):
        raise FileNotFoundError(f"文件 '{pptx_file}' 未找到。")

    # 解压缩PPTX文件
    with ZipFile(pptx_file, 'r') as zip_ref:
        # 列出所有文件
        file_list = zip_ref.namelist()
        
        # 检查presentation.xml.rels是否存在
        rels_file_name = 'ppt/_rels/presentation.xml.rels'
        if rels_file_name in file_list:
            return rels_file_name  # 返回相对路径
            
    raise FileNotFoundError(f"文件 '{rels_file_name}' 未在 '{pptx_file}' 中找到。")

# 示例使用
pptx_file_path = 'templates/LGBTQIA Pride Month presentation.pptx'
presentation_rels_path = get_presentation_rels_path(pptx_file_path)
print(f"找到的presentation.xml.rels文件路径：{presentation_rels_path}")

import zipfile
import os

def read_presentation_rels(pptx_file: str):
    """
    读取presentation.xml.rels文件的内容
    
    :param pptx_file: PPTX文件的路径
    :return: presentation.xml.rels的内容
    """
    # 检查文件是否存在
    if not os.path.isfile(pptx_file):
        raise FileNotFoundError(f"文件 '{pptx_file}' 未找到。")
    
    rels_file_name = "ppt/_rels/presentation.xml.rels"
    
    # 解压缩PPTX文件并读取presentation.xml.rels内容
    with zipfile.ZipFile(pptx_file, 'r') as zip_ref:
        # 检查presentation.xml.rels是否存在
        if rels_file_name in zip_ref.namelist():
            with zip_ref.open(rels_file_name) as rels_file:
                content = rels_file.read()
                print(content.decode('utf-8'))  # 打印文件内容（XML格式）
        else:
            raise FileNotFoundError(f"文件 '{rels_file_name}' 未在 '{pptx_file}' 中找到。")


read_presentation_rels(pptx_file_path)
