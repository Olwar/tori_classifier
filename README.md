# tori_classifier
### A Computer Vision Model to recognize what object is in a picture
Our model's goal was to identify if there is a chair in a picture or not. We trained a Neural Network Computer Vision model with 2233  images of chairs and equal amount of non-chair images. All images were user-posted images scraped from Tori.fi. No other additional user data was collected. The model achieved accuracy of 88% at classifying images of chairs and non-chairs.

The model can be used to autofill the sale category for an object (for now, only a chair). User uploads an image of an object and the model identifies the object in the image and then the output is used to autofill the category in the sale listing, e.g. for a chair the category would be 'Sisustus ja huonekalut > Pöydät ja tuolit'."

Given more time, computing power and larger training sets of data much higher accuracy is easily achieved.

Usage:
1. Run `bash install.sh` to install all the necessary packages required
2. Run `python3 outputter.py`
3. Program's GUI opens up
4. Insert path to image
5. Program will tell if it's a chair or not
