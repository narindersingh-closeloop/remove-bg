import sys

from PIL import Image
from transparent_background import Remover

# get image file path
file_path = sys.argv[1]

# Load model
remover = Remover() # default setting

# Usage for image
img = Image.open(file_path).convert('RGB') # read image

filename = file_path.split('/')[-1].split('.')[0]

out = remover.process(img) # default setting - transparent background

# out = remover.process(img, type='rgba') # same as above
# out = remover.process(img, type='map') # object map only
# out = remover.process(img, type='green') # image matting - green screen
# out = remover.process(img, type='blur') # blur background
# out = remover.process(img, type='overlay') # overlay object map onto the image
# out = remover.process(img, type='samples/background.jpg') # use another image as a background

output_file_path = "/edit_images/edited_" + filename + ".png"

Image.fromarray(out).save("public" + output_file_path) # save result

print(output_file_path)
