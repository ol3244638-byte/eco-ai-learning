def aqi_level(aqi):
    if aqi <= 50:
        return "优","绿色","各类人群可正常活动"
    elif aqi<= 100:
        return "良","黄色","极少数异常敏感人群应减少户外活动"
    elif aqi<= 150:
        return "轻度污染","橙色","敏感人群减少外出"
    elif aqi<= 200:
        return "中度污染","红色","一般人群适量减少户外运动，敏感人群一般不外出"
    elif aqi<= 300:
        return "重度污染","紫色","敏感人群停止户外运动，一般人群减少户外运动"
    else:
        return "严重污染","褐红色","敏感人群应当留在室内，一般人群停止户外运动"

aqi_list=[43,52,100,101,151,150,500]
counts={}
for i,aqi  in enumerate(aqi_list, start=1):
    category,color,advice=aqi_level(aqi)
    print(f"第{i}天,AQI={aqi} {category} {color} {advice}")
    if category in counts:
        counts [category]=counts[category] +1
    else:
        counts [category]=1
for category,days in counts.items():
    print(f"{category}：{days}天")


    


    