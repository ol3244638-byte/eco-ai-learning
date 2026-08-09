"""air_report.py —— 空气质量日报统计工具

读取城市空气质量监测 CSV,逐日调用 aqi_level() 判定级别,输出
各级别天数统计和污染最重日,并将带级别的完整结果导出为 CSV。

处理流程:
    load_data() → add_level() → summarize() / find_worst_day() → 导出

输入文件:
    同目录下的 fuzhou_air.csv,需包含 date 和 aqi 两列
    (实际数据还含 city / pm25 / pm10 / so2,本脚本原样保留不处理)

输出文件:
    同目录下的 report_output.csv,在原表基础上追加
    「等级」「颜色」「健康建议」三列,以 utf-8-sig 编码保存
    (带 BOM,便于 Excel 直接双击打开不乱码)

分级标准:HJ 633—2026
"""
import pandas as pd
from aqi_level import aqi_level
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "fuzhou_air.csv"      # 以脚本自身位置定位,避免受运行时工作目录影响
DATE_COL = "date"
AQI_COL = "aqi"
LEVEL_ORDER = ["优", "良", "轻度污染", "中度污染", "重度污染", "严重污染"]


def load_data(path):
    """读取监测数据 CSV,并将日期列解析为 datetime 类型。

    Args:
        path (str | pathlib.Path): CSV 文件路径。

    Returns:
        pandas.DataFrame: 原始数据表,DATE_COL 列已转为 datetime64,
            其余列按 pandas 默认规则推断类型。

    Raises:
        FileNotFoundError: 路径不存在时由 pandas 抛出。
        ValueError: CSV 中缺少 DATE_COL 指定的日期列时抛出。
    """
    df = pd.read_csv(path, parse_dates=[DATE_COL])
    return df


def add_level(df):
    """为每一天的 AQI 追加级别、代表色和健康建议三列。

    对 AQI_COL 列逐行调用 aqi_level(),把返回的三元组展开成三列。

    注意:本函数直接在传入的 df 上新增列(原地修改),同时又把它
    返回。调用方拿到的返回值与传入对象是同一个 DataFrame,若需要
    保留原表不变,请先自行 df.copy()。

    Args:
        df (pandas.DataFrame): 含 AQI_COL 列的数据表。

    Returns:
        pandas.DataFrame: 追加了「等级」「颜色」「健康建议」三列的同一对象。

    Raises:
        KeyError: 表中不存在 AQI_COL 指定的列时抛出。
    """
    df[["等级", "颜色", "健康建议"]] = df[AQI_COL].apply(lambda x: pd.Series(aqi_level(x)))
    return df


def summarize(df):
    """按空气质量级别统计天数并打印。

    统计结果按 LEVEL_ORDER 定义的标准级别顺序重排,未出现的级别
    补 0 输出,以保证每次打印的行数和顺序一致、便于横向比较。

    本函数只负责打印,不返回统计结果。

    Args:
        df (pandas.DataFrame): 已经过 add_level() 处理、含「等级」列的数据表。

    Returns:
        None
    """
    counts = df["等级"].value_counts().reindex(LEVEL_ORDER, fill_value=0)
    for level, days in counts.items():
        print(f"{level}:{days}天")


def find_worst_day(df):
    """找出 AQI 最高的一天。

    按 AQI 降序排序后取首行。若存在多天 AQI 并列最高,返回其中
    在原表里出现次序最靠前的一天。

    Args:
        df (pandas.DataFrame): 含 AQI_COL 列的数据表。

    Returns:
        pandas.Series: 污染最重那一天的完整记录(含所有列)。

    Raises:
        IndexError: 传入空表时抛出。
    """
    return df.sort_values(AQI_COL, ascending=False).iloc[0]


def main():
    """脚本入口:读数据 → 打级别 → 打印统计与最重污染日 → 导出结果 CSV。"""
    df = load_data(CSV_PATH)
    df = add_level(df)
    print(df)
    print()
    summarize(df)
    print()
    worst = find_worst_day(df)
    print("=== 污染最重的一天 ===")
    print(f"{worst[DATE_COL].date()} AQI={worst[AQI_COL]} "
          f"{worst['等级']},{worst['健康建议']}")
    df.to_csv(BASE_DIR / "report_output.csv", index=False, encoding="utf-8-sig")
    print("\n已导出 report_output.csv")


if __name__ == "__main__":
    main()
