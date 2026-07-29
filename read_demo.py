import pandas as pd

# 读取 CSV 文件
df = pd.read_csv("air_quality.csv", parse_dates=["date"])
# 查看前 5 行
# print(df.head())

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
print(df[["date","pm25"]])
print(df[df["aqi"]<=50])
print(df[df["aqi"]<=50].shape)
print(df[(df["aqi"]>50)&(df["date"].dt.day_name().isin(["Saturday","Sunday"]))])