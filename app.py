from flask import Flask, render_template
import utils.query_nvidia as qNV
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
import random
import time
app = Flask(__name__)



app = Flask(__name__, static_folder="templates")


def bar_base():
    c_time = time.strftime("%Y-%m-%d %H:%M:%S")
    c = (
        Bar()#与上面的一致
            .add_xaxis(["GPU:0", "GPU:1", "GPU:2", "GPU:3", "GPU:4", "GPU:5", "GPU:6"])
            .add_yaxis("显存", [random.randint(10, 100) for _ in range(7)])
            .set_global_opts(title_opts=opts.TitleOpts(title="bobo GPU", subtitle=c_time))
    )
    return c

def pie_base():
    c_time = time.strftime("%Y-%m-%d %H:%M:%S")
    attr = [1, 2, 3]
    value = [1, 2, 3]
    p = (
        Pie().add('12', zip(attr, value)).add('12', zip(attr, value)).set_global_opts(title_opts=opts.TitleOpts(title="bobo GPU", subtitle=c_time))
    )
    return p

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/barChart")
def draw_bar_chart():
    # gpu_summary_log = qNV.query_GPU_status('nvidia-smi', 'PID')
    # c = bar_base()
    c = pie_base()
    return c.dump_options_with_quotes()

# @app.route("/pieChart")
# def draw_pie_chart():
#     # gpu_summary_log = qNV.query_GPU_status('nvidia-smi', 'PID')
#     p = pie_base()
#     return p.dump_options_with_quotes()

if __name__ == "__main__":
    app.run()
