from flask import Flask, render_template, request
from PIL import Image
import imageio
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def create_gif():
    # Get the uploaded pictures
    pictures = request.files.getlist('pictures')
    
    # Save the pictures to disk
    picture_paths = []
    for picture in pictures:
        picture_path = os.path.join('uploads', picture.filename)
        picture.save(picture_path)
        picture_paths.append(picture_path)
    
    # Load the pictures
    image_list = []
    for picture_path in picture_paths:
        img = Image.open(picture_path)
        image_list.append(img)
    
    # Create the GIF
    duration = 0.5 # time between frames in seconds
    gfile = 'my_gif.gif'
    file_path = os.path.join('./../GifMaker/static', gfile)
    imageio.mimsave(file_path, image_list, duration=duration, loop=0)
    #print(gfile)
    return render_template('result.html', output_file=gfile)

if __name__ == '__main__':
    app.run(debug=True)