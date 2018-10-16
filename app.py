from flask import Flask, render_template, request
from werkzeug import secure_filename
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('app.html')

@app.route('/uploader', methods = ['POST'])
def upload_file1():
      if request.method == 'POST':
          pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
          f = request.files['file']
          x1 = request.form['x1'][0]
          y1 = request.form['y1']
          x2 = request.form['x2']
          y2 = request.form['y2']
          f.save(secure_filename(f.filename))
          img = Image.open(f.filename)
          img2 = img.crop((int(x1) , int(y1), int(x2), int(y2)))
          img2.save("img2.png")
          text = pytesseract.image_to_string("img2.png")
          return text

		
if __name__ == '__main__':
   app.run(debug = True)
