from PIL import Image
import numpy as np
from skimage import transform
import tensorflow as tf

class_names = ['간장게장', '갈비구이', '갈비찜', '갈비탕', '갈치구이', '갈치조림', '감자전', '감자조림', '감자탕', '갓김치', '건새우볶음', '경단', 
               '계란말이', '계란찜', '고등어구이', '고등어조림', '고사리나물', '고추튀김', '곱창구이', '곱창전골', '김밥', '김치볶음밥', '김치전', 
               '김치찌개', '깍두기', '깻잎장아찌', '꼬막찜', '꽁치조림', '꿀떡', '나박김치', '닭갈비', '닭볶음탕', '더덕구이', '도토리묵', '동그랑땡', 
               '동태찌개', '된장찌개', '두부김치', '두부조림', '땅콩조림', '떡갈비', '떡볶이', '라면', '라볶이', '막국수', '만두', '매운탕', '멍게', 
               '메추리알장조림', '멸치볶음', '무국', '무생채', '물냉면', '물회', '미역국', '미역줄기볶음', '배추김치', '백김치', '보쌈', '부추김치', 
               '북엇국', '불고기', '비빔냉면', '비빔밥', '삼겹살', '삼계탕', '새우볶음밥', '새우튀김', '소세지볶음', '송편', '수육', '수정과', '수제비', 
               '숙주나물', '순대', '순두부찌개', '시금치나물', '시래기국', '식혜', '알밥', '애호박볶음', '약과', '약식', '양념게장', '양념치킨', '어묵볶음', 
               '연근조림', '열무김치', '오이소박이', '오징어채볶음', '오징어튀김', '우엉조림', '유부초밥', '육개장', '육회', '잔치국수', '잡곡밥', '잡채', 
               '장어구이', '장조림', '전복죽', '제육볶음', '조개구이', '조기구이', '족발', '주꾸미볶음', '주먹밥', '짜장면', '짬뽕', '쫄면', '찜닭', 
               '총각김치', '추어탕', '칼국수', '코다리조림', '콩국수', '콩나물국', '콩나물무침', '파김치', '파전', '피자', '해물찜', '호박전', '호박죽', 
               '홍어무침', '황태구이', '회무침', '후라이드치킨', '훈제오리']

def image_preprocessing(filepath, IMAGE_SIZE=150):
   np_image = Image.open(filepath)
   np_image = np.array(np_image).astype('float32')/255
   np_image = transform.resize(np_image, (IMAGE_SIZE, IMAGE_SIZE, 3))
   np_image = np.expand_dims(np_image, axis=0)
   
   return np_image

def image_prediction_result(filepath, model_dir, model_name, n=5): 
  image = image_preprocessing(filepath)
  model = tf.keras.models.load_model(model_dir + model_name)
  y_preds = model.predict(image)
  y_preds_top = np.argsort(-y_preds)[:, :n] # 높은 순서대로 5개 결과 반환
  
  top1 = class_names[y_preds_top[0,0]]
  top2to5 = [class_names[idx] for idx in y_preds_top[0,1:n]]

  return {"TOP1" : top1, "TOP2to5" : top2to5}