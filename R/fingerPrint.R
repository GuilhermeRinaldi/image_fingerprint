#install.packages("magick")
#install.packages("modeest")
#library(magick)
#library(modeest)

img <- image_read('path/name + .extension')
imgBitmap <- as.raster(img)
rows = dim(imgBitmap)[1]
cols = dim(imgBitmap)[2]
out <- image_draw(img)

for(row in 0:rows) {
  abline(h = row, col =  mfv(imgBitmap[row,1:cols]), lwd = 1 , lty = 1)  
}

image_write(out, path = "name + .extension", format = "extension")
