# GPU资源展示(GPU Util Display)
### 功能(Capability)
用饼图展示服务器GPU的使用情况，包括GPU使用的明细['PID', 'GPU', 'PATH', 'Mem']表格  
Display GPU util by PieChart, including ['PID', 'GPU', 'PATH', 'Mem']
### 环境需要(Requirement)
`pip install `
 - flask
 - pyechart （用pip安装）
 - pandas,

### 实现原理(Methods)
正则化匹配`nvidia-smi`返回的结果，然后正则化匹配关键词提取GPU信息，使用pandas进行数据统计，
然后用pyecharts绘图，flask后端部署，必要时可以用frp进行转发，映射到公网  
Extracting keywords by Regular matching; Summary by pandas; Deploy by flask, Drawing with pyecharts   

### 运行(Run)
```
source activate flask环境
python app.py
```  
使用了了本地5000端口(Binding with localhost:5000)
