from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
import pandas as pd
import numpy as np
from pyecharts.globals import ThemeType
from tools import query_nvidia as QN
# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 100, 100]
# data = zip(attr, v1)



def new_label_opts():
    return opts.LabelOpts( position="center")



# gpu_summary_log = QN.query_GPU_status("nvidia-smi", "PID")
# gpu_df = pd.DataFrame(gpu_summary_log, columns=['PID', 'GPU', 'PID_PATH', 'MEM'])
# user_stat, gpu_util_stat, all_gpu_info = QN.status_analysis(gpu_df)
# gpu_online = gpu_util_stat.keys()



def draw_pie_chart(groupby_user, groupby_gpu, GPU_count=7) -> Pie:
    global pie, data
    base_radius = int(200 // GPU_count * 1.5)
    loc_x = base_radius
    loc_y = 20
    pie = Pie(init_opts=opts.InitOpts(width="1600px", height="900px", theme=ThemeType.ROMA))
    all_gpu_info = groupby_gpu['MEM'].sum()
    for i in range(GPU_count):
        if i in all_gpu_info.keys():
            current_gpu_list = groupby_gpu.get_group(i)[["PID_PATH", "MEM"]].values.tolist()
            aval_mem = 11 - all_gpu_info[i]
            data = [['可用', aval_mem]]
            data.extend(current_gpu_list)
        else:
            aval_mem = 11
            data = [['可用', aval_mem]]

        pie.add(
            "GPU:%s" % i,
            data,
            radius='%s' % base_radius,
            center=[str(loc_x // 3 * i) + '%', str(loc_y) + '%'],
            rosetype=None,
            label_opts=opts.LabelOpts(position='inside', font_size=10, is_show=False),
        )
    pie = pie.set_global_opts(title_opts=opts.TitleOpts(title="GPU Stat"))
    return pie

if __name__ == '__main__':
    GPU_count = 7
    gpu_summary_log = QN.query_GPU_status("nvidia-smi", "PID")
    gpu_df = pd.DataFrame(gpu_summary_log, columns=['PID', 'GPU', 'PID_PATH', 'MEM'])
    user_stat, gpu_util_stat, all_gpu_info = QN.status_analysis(gpu_df)
    draw_pie_chart(user_stat, gpu_util_stat)
    pie.render()



