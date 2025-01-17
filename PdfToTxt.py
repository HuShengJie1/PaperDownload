import fitz  # PyMuPDF


def pdf_to_txt(pdf_path, txt_path):
    # 打开 PDF 文件
    doc = fitz.open(pdf_path)

    # 打开输出的 TXT 文件
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        # 遍历 PDF 中的每一页
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # 获取当前页
            text = page.get_text()  # 提取文本
            txt_file.write(text)  # 写入到 TXT 文件

    print(f"PDF 转换完成，文本已保存为 {txt_path}")


# 使用示例
pdf_path = '1.pdf'  # 替换为你的 PDF 文件路径
txt_path = 'output.txt'  # 输出的 TXT 文件路径
pdf_to_txt(pdf_path, txt_path)
