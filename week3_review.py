import pandas as pd
df=pd.read_csv("air_quality.csv", parse_dates=["date"])
print(df.head(7))
over_days =df[df['pm25']>75]
print(over_days)
print("PM2.5 超标的为",over_days.shape[0],"天")
aqi_mean_all=df['aqi'].mean()
aqi_mean_over=over_days['aqi'].mean()
print(f'福州全部日子AQI均值:{aqi_mean_all:.1f}')
print(f'福州超标日子AQI均值:{aqi_mean_over:.1f}')
count_down=df.sort_values('pm25', ascending=False).head(3)
print(count_down)