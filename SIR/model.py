import json

filename = 'data/data_1_29_list.json'
with open(filename) as f:
    pop_data = json.load(f)
    allcases = []
    traces = []
    for value in pop_data:
        area = value['provinceShortName']
        confirm = value['confirmedCount']
        case = []
        case.append(area)
        case.append(confirm)
        allcases.append(case)
        print(area + ": " + str(confirm) + " confirm cases.")

    for value in pop_data:
        area = value['provinceShortName']
        if area is not "武汉":
            case = ["武汉"]
            case.append(area)
            traces.append(case)

from snapshot_pyppeteer import snapshot
from pyecharts.charts import Geo
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from pyecharts.globals import ChartType, SymbolType

def geo_getmap() -> Geo:

    c = (
        Geo()
        .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
        )
        .add(
            "",
            allcases,
            type_=ChartType.EFFECT_SCATTER,
            # symbol_size="size",
            color="white",
        )
        .add(
            "",
            traces,
            type_=ChartType.LINES,
            # effect_opts=opts.EffectOpts(
            #     symbol=SymbolType.ARROW, symbol_size=6, color="red"
            # ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="2019-nCoV Trace Map(China)"))
    )
    make_snapshot(snapshot, c.render(), "tracemap.png")

def map_getmap() -> Map:
    c = (
        Map()
        .add(
            "Confirmed Cases by 1.29",
            allcases,
            "china"
            # type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=300, is_piecewise=True),
            title_opts=opts.TitleOpts(title="2019-nCoV Geo Map(China)"),
        )
    )
    make_snapshot(snapshot, c.render(), "geomap.png")

if __name__ == '__main__':
    geo_getmap()
    # map_getmap()
