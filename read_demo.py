# import pandas as pd

# 读取 CSV 文件
# df = pd.read_csv("air_quality.csv", parse_dates=["date"])
# 查看前 5 行
# print(df.head(7))

# 顺便看看数据结构
#print("\n行数、列数:", df.shape) #练过了注释掉
#print("列名:", list(df.columns))
#print(df.info())
#print(df["date"].dt.day_name())
#print(df["aqi"])
#print(df["aqi"].mean())
#print(df["aqi"].max())
#print(df[["date","aqi"]])
#print(df["aqi"]>100)
#print(df[df["aqi"]>100])
#print(df[(df["aqi"]>50)&(df["aqi"]<=100)])
#print(df[(df["aqi"]<40)|(df["aqi"]>100)]) #练过了注释掉
# print(df[["date","pm25"]])
# print(df[df["aqi"]<=50])
# print(df[df["aqi"]<=50].shape)
# print(df[(df["aqi"]>50)&(df["date"].dt.day_name().isin(["Saturday","Sunday"]))])
# df.sort_values('pm25')
# print(df.sort_values('pm25', ascending=False))
# print(df.sort_values(['city', 'aqi'], ascending=[True, False]))
# print(df['pm25'].mean())
import pandas as pd

data = {
    'date': pd.date_range('2026-06-01', periods=30),
    'city': ['福州']*15 + ['厦门']*15,
    'PM2.5': [28, 42, 55, 38, 61, 33, 47, 72, 29, 51, 44, 68, 36, 58, 41,
              31, 45, 39, 52, 27, 63, 35, 48, 30, 56, 40, 66, 34, 49, 43],
    'AQI':   [45, 68, 82, 60, 95, 52, 74, 108, 46, 79, 70, 101, 57, 88, 65,
              49, 71, 62, 80, 44, 97, 55, 75, 48, 85, 63, 99, 54, 76, 67]
}
df = pd.DataFrame(data)
# count=df[(df['city']=='福州')&(df['PM2.5']>50)].shape[0]
# print("福州PM2.5超标天数：",count)
# count_all=df[df['city']=='福州']['AQI'].mean()
# count_cover=df[(df['city']=='福州')&(df['PM2.5']>50)]['AQI'].mean()
# print(f'福州全部日子AQI均值:,{count_all:.1f}')
# print(f'福州超标日AQI均值:,{ count_cover:.1f}')
# print(f'福州超标日比全部日子AQI均值高了,{count_cover-count_all:.1f}')
fz=df[df['city']=='福州']
count=fz.sort_values('PM2.5',ascending=False).head(3)
print(count[['date','PM2.5','AQI']])