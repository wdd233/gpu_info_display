from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Tab, Pie, Line
from pyecharts.components import Table


def table_base(headers, rows, title="GPU Util") -> Table:
    table = Table()
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title=title)
    )
    return table

if __name__ == '__main__':

    table_example = table_base()
    table_example.render('table.html')