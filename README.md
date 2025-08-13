# Image cropper for training AI models
This python script creates a simple UI that allows to select an area on an image and save it as a cropped 512x512 image. 512x512 images are required to train models like stable diffusion. With a lot of training images, this script really saves a lot of time.

## Note from 2025
It used to be necessary to fine-tune an image model (like stable diffusion) with images of your face, so you could generate images with you in it. These images where 512x512 px, so with this tool you could quickly crop images from higher res sources to give them to the model. 

Since then, AI has advanced so much that most image generating models just need a single image to replicate your face, so this tool is probably no longer needed.

## How to use:

1. Create a folder called "rawImages", put your images in there.
2. Run the script in the folder that contains the "rawImages" folder.
3. The script will open each image. Select the area to be saved by dragging a selection rectangle with LMB.
4. Save the image by pressing enter, the image will be saved in a folder called "croppedImages", which is automatically created. The saved image is resized to 512x512 pixels. The next raw image will open.
