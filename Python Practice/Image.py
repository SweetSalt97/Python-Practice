#Image in Python
from PIL import Image
filename = r"C:\Users\Ashut\OneDrive\Pictures\Holi.jpg"
#Note C:\Users\Ashut\OneDrive\Pictures\Holi.jpg didnt gave error
#So I added 'r' before it to produce raw string 
img = Image.open(filename)
img.show()
