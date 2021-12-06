from PyPDF2 import PdfFileReader,PdfFileWriter

def rotate_pages(filepath,angle,page_num):
    try:
        pdf_reader = PdfFileReader(filepath)
    except FileNotFoundError:
        return {'error' : 'File not found.'}
    pdf_writer = PdfFileWriter()

    if page_num > pdf_reader.numPages:
        return {'error' : 'page index out of range'}

    for pno in range(pdf_reader.numPages):
        page= pdf_reader.getPage(pno)
        if pno == page_num-1:
            try:
                page.rotateClockwise(angle)
            except AssertionError:
                return {'error' : 'numbers must be multiple of 90'}
        pdf_writer.addPage(page)

    with open(filepath,'wb') as f:
        pdf_writer.write(f)
    
    return filepath

