以下是一个完整的 docker-compose.yml 文件，用于配置一个包含 Nginx 和 Flask 的 Web 服务。Nginx 将作为反向代理服务器，Flask 应用程序在后端运行，并通过 Gunicorn 作为 WSGI 服务器来处理请求。

docker-compose.yml

创建一个 Dockerfile 文件，用于构建 flask_app 服务：

在项目目录下创建一个 requirements.txt 文件，列出 Flask 和其他需要的 Python 模块：

最后，为 Nginx 创建一个自定义的配置文件 nginx.conf，将请求转发到 Flask 应用的 Gunicorn 服务器：


部署和运行
完成以上文件的创建后，在项目目录中运行以下命令来构建和启动服务：

```
docker-compose up --build
```
此配置将建立一个 Nginx 服务器作为反向代理，Flask 应用将处理用户的 YouTube 转 MP3 请求，并通过 Gunicorn 作为 WSGI 服务器来处理 Flask 的请求。Flask 应用的外部端口映射为 8080，内部服务端口为 19876。
