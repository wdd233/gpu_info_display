from flask import Flask, render_template
# import tools.query_nvidia as qNV
# from pyecharts import options as opts
# from pyecharts.charts import Bar, Pie

import multi_tab
from pyecharts.globals import CurrentConfig

CurrentConfig.PAGE_TITLE = "614 GPU INFO"
app = Flask(__name__)


app = Flask(__name__, static_folder="templates")
app.jinja_env.auto_reload = True #自动加载
app.config['TEMPLATES_AUTO_RELOAD'] = True#自动加载template



@app.route("/", methods=['GET', 'POST'])
def index():

    c = multi_tab.draw_tab(GPU_NUMS=4, user_name='->')

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

