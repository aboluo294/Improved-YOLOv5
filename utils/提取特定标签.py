import os

# 设置文件夹路径
folder_path = 'D:/yolov5模型改进/x-walnut模型/datasets只有验证和测试/images/test'

# 创建一个列表来存储结果
result = []

# 遍历文件夹下的所有文件
for filename in os.listdir(folder_path):
    # 只处理 txt 文件
    if filename.endswith('.txt'):
        # 打开文件并读取第一行
        with open(os.path.join(folder_path, filename), 'r') as f:
            first_line = f.readline().strip()
            # 查找开头含 0 的标签
            if first_line.startswith('1'):
                result.append(filename)

# 打印结果
print("Files with 0 label:")
for file in result:
    print(file)