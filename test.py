#Test kiểm tra mô hình train
from tensorflow.keras.models import load_model
model=load_model('classifer_VietNameseFOOD.h5')
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
test_img=load_img('pho.jpg',target_size=(150,150))
import numpy as np
test_img= img_to_array(test_img)
test_img=test_img/255
test_img=np.expand_dims(test_img,axis=0)
result=model.predict(test_img)
if round(result[0][0])==1:
   prediction="BÁNH BAO"
elif round(result[0][1])==1:
   prediction="BÁNH MÌ"
elif round(result[0][2])==1:
   prediction="BÁNH TRÁNG NƯỚNG"  
elif round(result[0][3])==1:
   prediction="BÁNH TRƯNG"  
elif round(result[0][4])==1:
   prediction="BÁNH TRUNG THU"  
elif round(result[0][5])==1:
   prediction="BÁNH XÈO"  
elif round(result[0][6])==1:
   prediction="CHẢ GIÒ"  
elif round(result[0][7])==1:
   prediction="CƠM TẤM"  
elif round(result[0][8])==1:
   prediction="GỎI CUỐN"  
elif round(result[0][9])==1:
   prediction="PHỞ"  
print('=====> ĐÂY LÀ MÓN: ' + prediction)