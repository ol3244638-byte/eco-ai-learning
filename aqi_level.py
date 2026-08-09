"""aqi_level.py —— 空气质量指数(AQI)分级模块

依据 HJ 633—2026《环境空气质量指数(AQI)技术规定》,将 AQI 数值
映射为空气质量级别、对应代表色和健康影响提示。

本模块被 air_report.py 导入使用。直接运行本文件时,会用一组
覆盖各级别边界值的样例数据做自测。

分级区间(闭区间上界):
    0—50 优 / 51—100 良 / 101—150 轻度污染 /
    151—200 中度污染 / 201—300 重度污染 / >300 严重污染
"""


def aqi_level(aqi):
    """根据 AQI 数值返回空气质量级别、代表色和健康建议。

    分级依据 HJ 633—2026。判定采用闭区间上界,即 AQI=50 判为「优」,
    AQI=51 判为「良」,其余各级同理。

    Args:
        aqi (int | float): 空气质量指数。标准定义的有效范围为 0—500,
            本函数不做范围校验:传入负数会返回「优」,传入大于 500 的
            数值会返回「严重污染」。调用方需自行保证输入有效。

    Returns:
        tuple[str, str, str]: 三元组 (级别, 代表色, 健康建议)。
            例如 ("良", "黄色", "极少数异常敏感人群应减少户外活动")。

    Examples:
        >>> aqi_level(45)
        ('优', '绿色', '各类人群可正常活动')
        >>> aqi_level(110)[0]
        '轻度污染'
    """
    if aqi <= 50:
        return "优", "绿色", "各类人群可正常活动"
    elif aqi <= 100:
        return "良", "黄色", "极少数异常敏感人群应减少户外活动"
    elif aqi <= 150:
        return "轻度污染", "橙色", "敏感人群减少外出"
    elif aqi <= 200:
        return "中度污染", "红色", "一般人群适量减少户外运动，敏感人群一般不外出"
    elif aqi <= 300:
        return "重度污染", "紫色", "敏感人群停止户外运动，一般人群减少户外运动"
    else:
        return "严重污染", "褐红色", "敏感人群应当留在室内，一般人群停止户外运动"


if __name__ == "__main__":
    # 自测用例:取各级别的边界值,验证临界判定是否落在正确区间
    aqi_list = [43, 52, 100, 101, 151, 150, 500]
    counts = {}
    for i, aqi in enumerate(aqi_list, start=1):
        category, color, advice = aqi_level(aqi)
        print(f"第{i}天,AQI={aqi} {category} {color} {advice}")
        if category in counts:
            counts[category] = counts[category] + 1
        else:
            counts[category] = 1
    for category, days in counts.items():
        print(f"{category}：{days}天")
