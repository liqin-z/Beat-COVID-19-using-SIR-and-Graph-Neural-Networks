import json

filename = 'data/prettydata.json'
with open(filename) as f:
    pop_data = json.load(f)
    allcases = []
    for value in pop_data:
        if (value['day'] == "1.26" and value['country'] == "中国"):
            area = value['area']
            confirm = value['confirm']
            case = []
            case.append(area)
            case.append(confirm)
            allcases.append(case)
            print(area + ": " + str(confirm) + " confirm cases.")

from snapshot_pyppeteer import snapshot
from pyecharts.charts import Geo
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from pyecharts.globals import ChartType, SymbolType

def geo_getmap() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "Confirmed Cases",
            allcases,
            # type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True),
            title_opts=opts.TitleOpts(title="2019-nCoV Heat Map(China)"),
        )
    )
    make_snapshot(snapshot, c.render(), "geo.png")

def map_getmap() -> Map:
    c = (
        Map()
        .add(
            "Confirmed Cases",
            allcases,
            "china"
            # type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True),
            title_opts=opts.TitleOpts(title="2019-nCoV Heat Map(China)"),
        )
    )
    make_snapshot(snapshot, c.render(), "map.png")

if __name__ == '__main__':
    # geo_getmap()
    map_getmap()
