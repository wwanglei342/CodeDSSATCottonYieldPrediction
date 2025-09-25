import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates  # 从matplotlib.dates导入

# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# 读取Excel文件并加载数据
df = pd.read_excel('E:/博士科研任务留存/接单外快/韩祯祥_20250823_15000(待办)/code/23_1.xls')
# df = pd.read_excel('2023wth.xlsx')
# 提取指标名称和数据
indicators = df.columns[1:]  # 提取指标名称，排除第一列日期
dates = df['DAY']  # 提取日期列
data = df.iloc[:, 1:]  # 提取除日期外的数据列

# 创建图形和左侧的y轴
fig, ax1 = plt.subplots(figsize=(10, 6))  # 设置图形大小

# 绘制SRAD、TMAX、TMIN的散点连线图
for indicator in ['SRAD']:
    ax1.plot(dates, data[indicator], marker='o', markersize=3, linestyle='-', linewidth='1.5', color='r', label='Srad')
for indicator in ['TMAX']:
    ax1.plot(dates, data[indicator], marker='+', markersize=3, linestyle='--', linewidth='1.5', color='maroon', label='T_max')
for indicator in ['TMIN']:
    ax1.plot(dates, data[indicator], marker='+', markersize=3, linestyle='--', linewidth='1.5', color='darkcyan', label='T_min')

# 创建右侧的y轴
ax2 = ax1.twinx()  # 创建第二个y轴，共享x轴

# 设置右侧y轴的刻度范围为0到20
ax2.set_ylim(0, 20)

# 只在右侧y轴上绘制RAIN的柱状图
# ax2.bar(dates, data['RAIN'], color='teal', alpha=1, width=2, label='RAIN')
ax2.bar(dates, data['RAIN'], color='plum', alpha=1, width=2, label='RAIN')
# 添加图例
# ax1.legend(loc='upper left')
# ax2.legend(loc='upper right')
# ax1.legend()
# ax2.legend()
# 获取 ax1 和 ax2 的图例句柄和标签
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# 合并图例句柄和标签
handles = handles1 + handles2
labels = labels1 + labels2

# 合并图例并设置位置
# plt.legend(handles=handles, labels=labels, loc='upper right', bbox_to_anchor=(0.5, 0.5), ncol=1)
plt.legend(handles=handles, labels=labels, loc='upper left',  ncol=1)



# 设置 x 轴刻度数量为3，确保显示3个刻度
ax1.xaxis.set_major_locator(MaxNLocator(nbins=3))

# 格式化日期显示
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 使用matplotlib.dates.DateFormatter

# 控制x轴刻度的显示，选择每个月显示一个刻度
# ax1.xaxis.set_major_locator(mdates.MonthLocator())  # 也可以使用DayLocator()、WeekdayLocator()来调整显示频率
# 设置x轴最大刻度数量
max_ticks = 5  # 最多显示6个刻度
ax1.xaxis.set_major_locator(MaxNLocator(nbins=max_ticks))

# 自动旋转日期标签以避免重叠
plt.xticks(rotation=0)  # 设置旋转角度为 0，避免倾斜

# 设置字体大小
plt.xlabel('Date', fontsize=14)  # 设置x轴标签字体大小
# ax1.set_ylabel('Temperature(℃) & Solar radiation(MJ/m2)', fontsize=22)  # 设置左侧y轴标题字体大小
ax1.set_ylabel('Range of T(℃) and Srad(MJ/m^2)', fontsize=22)  # 设置左侧y轴标题字体大小
ax2.set_ylabel('Range of Rain(mm)', fontsize=22)  # 设置右侧y轴标题字体大小

# 设置x轴和y轴刻度字体大小
ax1.tick_params(axis='x', labelsize=18)  # 设置x轴刻度字体大小
ax1.tick_params(axis='y', labelsize=18)  # 设置y轴刻度字体大小
ax2.tick_params(axis='y', labelsize=18)  # 设置右侧y轴刻度字体大小

# # 在图上添加注释
# annotation_text1 = 'Max TMIN'  # 注释文本
# max_value1 = data['TMIN'].max()  # 获取最大值
# max_date1 = dates[data['TMIN'].idxmax()]  # 获取最大值对应的日期
# arrow_style1 = '->'  # 箭头样式
# arrow_color1 = 'black'  # 箭头颜色
# text_offset1 = 4  # 注释文本与箭头的垂直距离

# # 设置注释的位置和箭头样式
# ax1.annotate(annotation_text1, xy=(max_date1, max_value1), xytext=(max_date1, max_value1 + text_offset1),
#             arrowprops=dict(facecolor=arrow_color1, arrowstyle=arrow_style1,zorder=10), color='k', fontsize=14, zorder=20)

# # 在图上添加注释
# annotation_text2 = 'Max RAIN'  # 注释文本
# max_value2 = data['RAIN'].max()  # 获取最大值
# max_date2 = dates[data['RAIN'].idxmax()]  # 获取最大值对应的日期
# arrow_style2 = '->'  # 箭头样式
# arrow_color2 = 'black'  # 箭头颜色
# text_offset2 = 3  # 注释文本与箭头的垂直距离

# # 设置注释的位置和箭头样式
# ax1.annotate(annotation_text2,
#              xy=(max_date2, max_value2), 
#              xytext=(max_date2, max_value2 + text_offset2),
#             arrowprops=dict(facecolor=arrow_color2, arrowstyle=arrow_style2,zorder=10), 
#             color='k', fontsize=14, zorder=20,
#             )

# # 在图上添加注释
# annotation_text = 'Max TMAX'  # 注释文本
# max_value = data['TMAX'].max()  # 获取最大值
# max_date = dates[data['TMAX'].idxmax()]  # 获取最大值对应的日期
# arrow_style = '->'  # 箭头样式
# arrow_color = 'black'  # 箭头颜色
# text_offset = 3  # 注释文本与箭头的垂直距离

# # 设置注释的位置和箭头样式，zorder 确保注释在最上层，fontsize 调整字体大小
# ax1.annotate(annotation_text, 
#              xy=(max_date, max_value), 
#              xytext=(max_date, max_value + text_offset),
#              arrowprops=dict(facecolor=arrow_color, arrowstyle=arrow_style, zorder=10),
#              color='k', fontsize=14, zorder=20)  # 使用透明背景避免遮挡


# # 在图上添加注释
# annotation_text = 'Max SRAD'  # 注释文本
# max_value = data['SRAD'].max()  # 获取最大值
# max_date = dates[data['SRAD'].idxmax()]  # 获取最大值对应的日期
# arrow_style = '->'  # 箭头样式
# arrow_color = 'black'  # 箭头颜色
# text_offset = 3 # 注释文本与箭头的垂直距离

# # 设置注释的位置和箭头样式
# ax1.annotate(annotation_text, xy=(max_date, max_value), xytext=(max_date, max_value + text_offset),
#             arrowprops=dict(facecolor=arrow_color, arrowstyle=arrow_style, zorder=10), color='k', fontsize=14, zorder=20)

# 显示图形
plt.tight_layout()  # 调整图形布局，避免标签重叠
plt.show()
