from flask import Flask, render_template
import utils.query_nvidia as qNV
from pyecharts import options as opts
from pyecharts.charts import Bar
import random
import time
app = Flask(__name__)



app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c_time = time.strftime("%Y-%m-%d %H:%M:%S")
    c = (
        Bar()
            .add_xaxis(["GPU:0", "GPU:1", "GPU:2", "GPU:3", "GPU:4", "GPU:5", "GPU:6"])
            .add_yaxis("显存", [random.randint(10, 100) for _ in range(7)])
            .set_global_opts(title_opts=opts.TitleOpts(title="bobo GPU", subtitle=c_time))
    )
    return c

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/barChart")
def draw_bar_chart():
    # gpu_summary_log = qNV.query_GPU_status('nvidia-smi', 'PID')
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()
