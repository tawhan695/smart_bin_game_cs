import cv2 
import os
#validation
path = r'E:/smart_bin_game_cs/train/data/validation/plastic'
save_path = 'E:/smart_bin_game_cs/train/data/validation/plastic'  #บันทึก ไปยัง ...
name = 'plastic'
# plastic glass metal
n = 0
# for folder in folders:
for image in os.scandir(path):
        
        n+=1
        # print(image.path)
 
        img = cv2.imread(image.path)
        width = 224
        height = 224
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  
  
        print('Resized Dimensions : ', resized.shape)  
        
        
        cv2.imwrite(save_path+'/'+name+str(n)+'.jpg',resized)
        # print(save_path+'/'+name+str(n)+'.jpg')
        # cv2.imshow("Resized image", resized)  
        # cv2.waitKey(1)   

print(n)