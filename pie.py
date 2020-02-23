from pyecharts.charts import Bar, Pie
import pyecharts

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 100, 100]
data = zip(attr, v1)

pie = Pie()
pie.add('12', data, center=[500, 400])
pie.add('13', data, center=[500, 600])
pie.render()
