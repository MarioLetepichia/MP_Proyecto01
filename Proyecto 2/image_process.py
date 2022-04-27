from PIL import Image
import io

try:
    photo= '4.png'
except:
    print('Skipping unreadable image foo.png')


#open the image
img = Image.open(photo, mode='r') 
# resize the image
img = img.resize((300,300))
byteIO = io.BytesIO()
img.save(byteIO, format='PNG')
byteArr = byteIO.getvalue()