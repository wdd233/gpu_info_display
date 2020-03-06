import os
import argparse
import pandas as pd
import re
import time

def get_args():
    parser = argparse.ArgumentParser(description="Instruction")
    parser.add_argument('-c', '--command', default='nvidia-smi', type=str,
                      help='linux commands')
    parser.add_argument('-k', '--keyword', default='PID', type=str,
                        help='xxx')
    parser.add_argument('-u', '--user', default='bobo', type=str,
                        help='Linux user name')
    args = parser.parse_args()
    return args


def query_GPU_status(cmd, user_name='bobo', keyword='PID'):
    user_list = '(liuq|wang|Zhaowei)'
    pat = '\d+'#PID为数字，通过查询数字找到pid
    pat2 = '\%s.+'%user_name#proc中查询bobo相关字段
    query_pid_cmd = "ls -l /proc/{}/cwd"
    result = os.popen(cmd)
    res = result.read().splitlines()
    flag = 0
    summary = []

    assert len(res) > 0, "Command Error"
    for _, line in enumerate(res):
        if line.find(keyword) != -1:
            flag = _
            break

    for line in res[flag + 2:-1]:
        raw_line_info = re.compile(pat).findall(line)
        pid_line = os.popen(query_pid_cmd.format(raw_line_info[1])).read()
        pid_find_results = re.compile(pat2).findall(pid_line)
        if len(pid_find_results) == 0:
            continue
        pid_path = pid_find_results[0]
        info_mem = int(raw_line_info[-1]) / 1024
        line_info = [raw_line_info[1], int(raw_line_info[0]), pid_path, round(info_mem, 2)]
        # print("GPU:{}    PID:{}  PATH:{}   Mem:{:.2f}Gb".format(*line_info))
        summary.append(line_info)
    return summary

def status_analysis(dataframe):
    groupby_user = dataframe.groupby('PID_PATH')
    groupby_GPU = dataframe.groupby('GPU')
    all_gpu_info = groupby_GPU['MEM'].sum()
    return groupby_user, groupby_GPU, all_gpu_info

if __name__ == '__main__':
    args = get_args()
    while (1):
        gpu_summary_logs = []
        print("========Time: %s==========" % time.strftime("%Y-%m-%d %H:%M:%S"))
        gpu_summary_logs = query_GPU_status(args.command, args.user, args.keyword)
        for line_info in gpu_summary_logs:
            print(" PID:{}   GPU:{}    PATH:{}   Mem:{:.2f}Gb".format(*line_info))
        gpu_df = pd.DataFrame(gpu_summary_logs, columns=['PID', 'GPU', 'PID_PATH', 'MEM'])
        user_stat, gpu_stat, all_gpu_info = status_analysis(gpu_df)
        print('=====Over======')
        time.sleep(20)


