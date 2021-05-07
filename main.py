from flask import Flask
from config import DevConfig


app = Flask(__name__)

# Get the config from object of DevConfig
# 使用config.from_object() 而不使用app.config['DEBUG'] 是因为这样可以加载 class DevConfig的配置变量集合,
# 而不需要一项一项的添加和修改。
app.config.from_object(DevConfig)

# 指定URL = '/'的路由规则
# 当访问 http://server_ip/GET(Default) 时,call home()
@app.route('/')
def home():
    return '<h1>zxy真美,love u</h1>'



if __name__ == "__main__":
    #Entry the application
    app.run()










