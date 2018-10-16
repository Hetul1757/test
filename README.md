## Problem Statement
1. Develop a web page to upload an image with a rectangle filled with text.
2. A space to provide coordinates for top-left and bottom-right edge of the rectangle.
3. Then OCR just the rectangle using any tool and display the text.

## Requirements
- python 3.0+
- pytesseract
- pillow
- Flask

## Implemenration
1. Html page is created to input Image and its Coordinates which needs to be OCR.(templates/app.html)
2. Flask api is created to upload the Image from local directory.
3. Crop that Image according to given coordinates.
4. Use pytesseract's image_to_string to OCR Image.
5. Return the OCR text.

## Results
Front Page 1:
![alt text](https://github.com/Hetul1757/test/blob/master/Results/OCR_1.PNG)
Input Image 1:
![alt text](https://github.com/Hetul1757/test/blob/master/Results/OCR_1.PNG)
Cropped Image 1:
![alt text](https://github.com/Hetul1757/test/blob/master/Results/OCR_1.PNG)
Result 1:
![alt text](https://github.com/Hetul1757/test/blob/master/Results/OCR_1.PNG)
Front page 2:
![alt text](https://github.com/Hetul1757/test/blob/master/Results/OCR_1.PNG)
Input Image 2:
![alt text](https://github.com/Hetul1757/test/blob/master/Results/OCR_1.PNG)
Cropped Image 2:
![alt text](https://github.com/Hetul1757/test/blob/master/Results/OCR_1.PNG)
Result 2:
![alt text](https://github.com/Hetul1757/test/blob/master/Results/OCR_1.PNG)
