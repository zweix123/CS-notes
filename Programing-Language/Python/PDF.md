## Intro

+ Python处理PDF文件时常用的第三方库：
	+ `PyPDF2`：页面管理
	+ `pdfplumer`：内容管理
		>前身是`pdfminer`


## PyPDF2
```python
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
def split_pdf(infn, outfn):
    pdf_output = PdfFileWriter()
	with open(infn, 'rb')  as f:
		pdf_input = PdfFileReader(f)
	#页面数量
    page_count = pdf_input.getNumPages()
    print(page_count)
    # 将 pdf 前5页
    for i in range(5):
        pdf_output.addPage(pdf_input.getPage(i))
	with open(outfn, 'wb') as f:
		pdf_output.write(f)
def merge_pdf(pdf_folder, outfn):
	"""将多个文件合并为一个文件"""
    pdf_output = PdfFileWriter()
	#这里文件夹中只有pdf文件
	pdfs = os.listdur(os.path.join(pdf_folder))
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))
```

## pdfplumer
+ 踩坑
	+ 在win10下，需要安装软件[ImageMagick](https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows)和Ghostscript
		>神奇的是，这些都能通过scoop下

```python
import os
import pdfplumber

def pdf_to_imgs(filepath):
    res_folder = os.path.join(os.getcwd(), "Result")
    os.makedirs(resfolder)
    pdf = pdfplumber.open(filepath)
    for page in pdf.pages:
        print(page.page_number, page.width, page.height)
        # page.extract_text()
        # page.extract_table()
        
        
        img = page.to_image()
        img.save(os.path.join(res_folder, str(page.page_number) + ".jpg"))
    
    pdf.close()

if __name__ == "__main__":
    pdf_to_imgs("tar.pdf")
```