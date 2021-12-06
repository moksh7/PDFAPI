from flask import Flask, request

from rotate_pdf_pages import rotate_pages

app = Flask(__name__)

@app.route('/',methods=['POST'])
def rotate():
    if request.method == 'POST':
        file_path = request.form.get('file_path')
        angle_of_rotation = int(request.form.get('angle_of_rotation'))
        page_number = int(request.form.get('page_number'))
        
        modfied_file=rotate_pages(file_path,angle_of_rotation,page_number)

        return modfied_file



if __name__ == '__main__':
    app.run(debug=True)
