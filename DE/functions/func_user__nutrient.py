# 체중 대비 백분율 (PIBW, Percent of Ideal Body Weight)
def standard_weight(sex, height):
    if sex == 1:
        weight_s = (height / 100) * (height / 100) * 22
    
    if sex == 0:
        weight_s = (height / 100) * (height / 100) * 21
    return weight_s


def adjusted_weight(weight, weight_s):
    weight_a = weight_s + (weight - weight_s) * 0.25
    return weight_a

def calorie_counting(sex, age, height, weight_a, PA):
    PA_list = {'1':1, '2':1.12, '3':1.27, '4':1.45}
    PA = PA_list[PA]

    if sex == 1:
        calorie = 662 - (9.53 * age) + PA*((539.6 * (height / 100)) + (15.91 * weight_a))
    
    if sex == 0:
        calorie = 354 - (6.91 * age) + PA*((726 * (height / 100)) + (9.36 * weight_a))
    
    return calorie

def necessary_nutrients(sex, age, weight, calorie):
    carbohydrate = (calorie * 0.55) / 4
    fat = (calorie * 0.15) / 8
    protein = (calorie * 0.3) / 4
    moisture = weight * 35
    vitamin_A = 0.005 * age * 0.03 * weight * 1.1 * (100/40)
    vitamin_D = 10
    vitamin_E = 12
    vitamin_C = 2000
    folic_acid = 320
    phosphorus = 700
    sodium = 1500
    potassium = 3500
    manganese = 11
    selenium = 60
    if sex == 1:
        dietary_fiber = 30
        thiamin = 1
        riboflavin = 1.3
        niacin = 16
        calcium = 800
        magnesium = 360
        iron = 10
        zinc = 10
        copper = 850
        linolenic_acid = 13
        a_linolenic_acid = 16
        unsaturated_fatty_aci = 210
    if sex == 0:
        dietary_fiber = 20
        thiamin = 0.9
        riboflavin = 1
        niacin = 14
        calcium = 700
        magnesium = 280
        iron = 14
        zinc = 8
        copper = 650
        linolenic_acid = 10
        a_linolenic_acid = 12
        unsaturated_fatty_aci = 150

    total_dic = {'carbohydrate' :carbohydrate ,'fat' :fat ,'protein': protein ,'moisture': moisture ,
    'vitamin_A': vitamin_A ,'vitamin_D': vitamin_D ,'vitamin_E': vitamin_E ,'vitamin_C': vitamin_C ,
    'folic_acid': folic_acid ,'phosphorus': phosphorus ,'sodium': sodium ,'potassium': potassium ,
    'manganese': manganese ,'selenium' :selenium ,'dietary_fiber' :dietary_fiber ,'thiamin': thiamin ,
    'riboflavin' :riboflavin ,'niacin': niacin ,'calcium' :calcium ,'magnesium': magnesium ,'iron': iron ,
    'zinc': zinc ,'copper': copper ,'linolenic_acid' :linolenic_acid ,'a_linolenic_acid' :a_linolenic_acid ,
    'unsaturated_fatty_aci': unsaturated_fatty_aci}

    return total_dic


## 영한 변환
en_ko_dict = {'carbohydrate' : '탄수화물' ,'fat' :'지방' ,'protein ' : '단백질' ,'moisture ' : '수분' ,
'vitamin_A' : '비타민_A' ,'vitamin_D' : '비타민_D3' ,'vitamin_E' : '비타민_E' ,'vitamin_C' : '비타민_C' ,
'folic_acid' : '엽산' ,'phosphorus' : '인' ,'sodium ': '나트륨' ,'potassium': '칼륨' ,
'manganese' : '마그네슘' ,'selenium' :'셀레늄' ,'dietary_fiber' : '총_식이섬유' ,'thiamin ': '비타민_B1' ,
'riboflavin' : '비타민_B2' ,'niacin' : '나이아신' ,'calcium' :'칼슘' ,'magnesium' : '마그네슘' ,'iron' : '철' ,
'zinc' : '아연' ,'copper' : '구리' ,'linolenic_acid' : '리놀레산' ,'a_linolenic_acid' : '알파_리놀렌산' ,
'unsaturated_fatty_aci' : 'EPA-DHA'}

## 순서
# 1. standard_weight(sex, height) -> return weight_s
#  본인의 '표준 체중'을 구한다
# 2. adjusted_weight(weight, weight_s) -> return weight_a
#  표준 체중과 실제 체중을 이용하여 '조정 체중'을 구한다 
# 3. calorie_counting(sex, age, height, weight_a, PA) -> return calorie
#  성별, 나이, 키, 조정 체중, 활동량을 이용하여 '필요 에너지'를 구한다 
# 4. necessary_nutrients(sex, age, weight, calorie) -> return total_dic
#  성별, 나이, 실제 체중, 필요 에너지를 이용하여 필요 영양소를 구한다.
# ! 표준 체중에 가까워 지기 위한 영양성분만 계산 가능 = 목표 설정 불가능!...

## 활동량 구분
# 1 -> 일주일에 1~3회 운동
# 2 -> 일주일에 4~5회 운동
# 3 -> 강도 높은 운동 3~4회
# 4 -> 강도 높은 운동 6~7회

from datetime import datetime
def user_age(birthday, standard = datetime.now()):
    if type(birthday) == str:
        birthday = datetime.strptime(birthday, '%Y-%m-%d')

    if standard.month - birthday.month > 0:
        age = standard.year - birthday.year
    elif standard.month == birthday.month:
        if standard.day - birthday.day >= 0:
            age = standard.year - birthday.year
        else:
            age = standard.year - birthday.year - 1
    else:
        age = standard.year - birthday.year - 1
    
    return age