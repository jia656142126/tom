import csv
import psutil
import time


# with open('data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Name', 'Age', 'City'])
#     writer.writerow(['John', '25', 'New York'])
#     writer.writerow(['Emily', '30', 'London'])

# csvfile.close()

# 获取CPU信息
cpu_percent = psutil.cpu_percent(interval=1)  # 获取当前CPU使用率（百分比）
cpu_count = psutil.cpu_count(logical=True)  # 获取CPU逻辑核心数量

# 获取内存信息
memory = psutil.virtual_memory()  # 获取内存使用情况
memory_total = memory.total  # 总内存大小
memory_available = memory.available  # 可用内存大小
memory_percent = memory.percent  # 内存使用率（百分比）

print("CPU 使用率: {}%".format(cpu_percent))
print("CPU 核心数量: {}".format(cpu_count))
print("总内存大小: {:.2f} GB".format(memory_total / (1024**3)))
print("可用内存大小: {:.2f} GB".format(memory_available / (1024**3)))
print("内存使用率: {}%".format(memory_percent))
for item in range(100):
    time.sleep(1)
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["CPU 使用率: {}%".format(cpu_percent), "CPU 核心数量: {}".format(cpu_count), "总内存大小: {:.2f} GB".format(memory_total / (1024**3)),"可用内存大小: {:.2f} GB".format(memory_available / (1024**3)),"内存使用率: {}%".format(memory_percent)])

# 数据已追加到文件

csvfile.close()


with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
    for row in reader:
        print(row)
