import numpy as np
import pandas as pd
import os 


'''수질 데이터의 기준값 데이터 생성. 기준값 이상이면 부적합
'''

df = pd.DataFrame({
    '기준':['taste','smell','color','pH','NTU','residual_chlorine','DO','BOD','COD'],
    '기준값':['무미','무취','5', '5.8~8.5', '0.5', '4', '5', '6', '6']})

print(df)
