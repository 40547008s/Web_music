# 使用 Python slim 版本作为基础镜像
FROM python:3.11-slim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件到容器中
COPY requirements.txt .

# 安装 Python 模块
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用程序代码到容器中
COPY . .

# 暴露 Flask 应用的端口
EXPOSE 19876

# 使用 Gunicorn 启动 Flask 应用
CMD ["gunicorn", "--bind", "0.0.0.0:19876", "app:app"]
