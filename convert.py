import pypandoc
import os
import qianfan

from utils import getOrGeneratePathByDay

def markdown_to_docx(markdown_text, output_file="output.docx", dir_path='./'):
    """将 Markdown 文本转换为 docx 文件。

    Args:
        markdown_text: Markdown 文本。
        output_file: 输出 docx 文件名。
    """
    

    pypandoc.convert_text(markdown_text, 'docx', format='markdown', outputfile=output_file, cworkdir=dir_path)
    return 

def generate_exam():
    chat_comp = qianfan.ChatCompletion()

    resp = chat_comp.do(model="ERNIE-4.0-Turbo-8K", messages=[{
        "role": "user",
        "content": """请生成一份小升初奥数考试试卷，包含以下内容：
        试卷名称：小升初奥数考试试卷
        题型及数量：
            填空题：5道
            选择题：5道
            计算题：4道
            应用题：3道
        知识点：计算、数论、几何、行程、应用题、计数、组合
        难度等级：中等
    输出格式：markdown"""
    }])
    print(resp)
    dir_path = getOrGeneratePathByDay("./docs")
    file_name = "output.docx"
    try:
        markdown_to_docx(resp["body"]["result"],output_file=file_name, dir_path=dir_path)
    except Exception:
        print('--------error')
    return "{}/{}".format(dir_path, file_name)
