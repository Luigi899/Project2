'''
This part of the program is the encoder.
It will encode our message into the image.
'''

#Required module: PIL
from PIL import Image

#Definition to encode message into image.
def encode_message(img, msg):
    #Check message length & mode
    limit = len(msg)

    if(limit>255):
        print("The message is too long. Keep it under 255 characters.")
        return False
    if(img.mode != "RGB"):
        print("Image needs to be in RBG mode.")
        return False

    #Creating image copy to encode
    encoded = img.copy()
    width, height = img.size
    counter = 0
    
    for x in range(height):
        for y in range(width):
            #Variables holding pixel values
            r, g, b = img.getpixel((y,x))
            if x == 0 and y == 0 and counter < limit:
                ascii_code = limit
            elif counter <= limit:
                char = msg[counter-1]
                #Getting ASCII value
                ascii_code = ord(char)
            else:
                #Set ascii value to red
                ascii_code = r

            #Encoding message into pixel red value
            encoded.putpixel((y, x), (ascii_code, g, b))
            counter += 1
    print("Message has been encoded.")
    return encoded

#Whatever image we decide to use converted to .bmp
ori_img = "secret.bmp" 
img = Image.open(ori_img)
encoded_img = "enc_" + ori_img

#Message to encode into image
msg = "Something"

img_encoded = encode_message(img,msg)
if img_encoded:
     # save the image with the hidden text
     import os
     os.startfile(encoded_img)
     print("{} saved!".format(encoded_img))
     password = input('Enter password : ')
     if(password==1234):
          #print(password)
          print("Secret Message : " + msg)  # test
          img_encoded.save(encoded_img)
          # view the saved file, works with Windows only
          # behaves like double-clicking on the saved file
