from PIL import Image, ImageDraw
import statistics as st

img = Image.open('name + .extension')
rows = img.size[1]
cols = img.size[0]
out = Image.new('RGBA',(cols,rows),(0,0,0,0))
draw = ImageDraw.Draw(out)

colors = list(img.getdata())

for row in range(rows):
    startCol = cols*row
    endCol = cols*(row+1)
    color = st.mode(colors[startCol:endCol])
    draw.polygon([(0,row), (cols,row)], fill= color, outline=None)
        
out.save('name + .extension')


