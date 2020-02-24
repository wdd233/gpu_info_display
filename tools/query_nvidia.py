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
    args = parser.parse_args()
    return args


def query_GPU_status(cmd, keyword='PID'):
    pat = '\d+'#PID为数字，通过查询数字找到pid
    pat2 = '\/bobo.+'#查询bobo相关字段
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
        pid_path = re.compile(pat2).findall(pid_line)[0]
        line_info = [raw_line_info[1], int(raw_line_info[0]), pid_path, int(raw_line_info[-1]) / 1024]
        # print("GPU:{}  PATH:{}   Mem:{:.2f}Gb PID:{}".format(*line_info))
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
        gpu_summary_log = []
        print("========Time: %s==========" % time.strftime("%Y-%m-%d %H:%M:%S"))
        gpu_summary_log = query_GPU_status(args.command, args.keyword)
        gpu_df = pd.DataFrame(gpu_summary_log, columns=['PID', 'GPU', 'PID_PATH', 'MEM'])
        user_stat, gpu_stat, all_gpu_info = status_analysis(gpu_df)
        print('=====Over======')
        time.sleep(20)


