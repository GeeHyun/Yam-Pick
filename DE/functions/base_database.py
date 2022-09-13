from yp.models import tb_food_img
from yp import db

import pandas as pd
import os
import config

food_dir = os.path.join(config.BASE_DIR, 'yp/static/img/food_rec')
food_list = list(map(lambda food: food.split('.')[0], os.listdir(food_dir)))

def base_database():
    df = pd.read_csv(config.BASE_DIR + "/functions/DB__ver2.csv")

    for i in range(len(df)):
        food = tb_food_img(food_name=df.iloc[i]['식품명'],
                        energy = df.iloc[i]['에너지'],
                        carbohydrate = df.iloc[i]['탄수화물'],
                        fat = df.iloc[i]['지방'] ,
                        protein = df.iloc[i]['단백질'],
                        moisture = df.iloc[i]['수분'],
                        vitamin_A = df.iloc[i]['비타민_A'],
                        vitamin_D = df.iloc[i]['비타민_D3'],
                        vitamin_E = df.iloc[i]['비타민_E'],
                        vitamin_C = df.iloc[i]['비타민:_C'],
                        folic_acid = df.iloc[i]['엽산'],
                        phosphorus = df.iloc[i]['인'],
                        sodium = df.iloc[i]['나트륨'],
                        potassium = df.iloc[i]['칼륨'],
                        manganese = df.iloc[i]['마그네슘'],
                        selenium = df.iloc[i]['셀레늄'],
                        dietary_fiber = df.iloc[i]['총_식이섬유'],
                        thiamin = df.iloc[i]['비타민_B1'],
                        riboflavin = df.iloc[i]['비타민_B2'],
                        niacin = df.iloc[i]['나이아신'],
                        calcium = df.iloc[i]['칼슘'],
                        magnesium = df.iloc[i]['마그네슘'],
                        iron = df.iloc[i]['철'],
                        zinc = df.iloc[i]['아연'],
                        copper = df.iloc[i]['구리'],
                        linolenic_acid = df.iloc[i]['리놀레산'],
                        a_linolenic_acid = df.iloc[i]['알파_리놀렌산'],
                        unsaturated_fatty_aci = df.iloc[i]['EPA+DHA']
                        )

        if food.food_name in food_list:
            food.food_img = f'{food_dir}/{food.food_name}.jpg'
        else:
            food.food_img = None
        db.session.add(food)
    db.session.commit()