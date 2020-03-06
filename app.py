from flask import Flask, render_template
import tools.query_nvidia as qNV
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
import random
import time
import os
import multi_tab
from pyecharts.globals import CurrentConfig
# CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"
CurrentConfig.PAGE_TITLE = "614 GPU INFO"
app = Flask(__name__)



app = Flask(__name__, static_folder="templates")
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

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

@app.route("/", methods=['GET', 'POST'])
def index():
    # c = multi_tab.draw_tab()
    c = multi_tab.draw_tab()
    # os.remove('templates/tab.html')
    c.render('templates/tab.html')
    return render_template("tab.html")
    # return render_template("index.html")

@app.route("/tabChart")
def draw_multi_tab_chart():
    # gpu_summary_log = qNV.query_GPU_status('nvidia-smi', 'PID')
    # c = bar_base()
    c = multi_tab.draw_tab()
    return c

# @app.route("/pieChart")
# def draw_pie_chart():
#     # gpu_summary_log = qNV.query_GPU_status('nvidia-smi', 'PID')
#     p = pie_base()
#     return p.dump_options_with_quotes()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
