'''
设置路由和后端逻辑
'''
from flask import Flask, render_template
from config import Config
from models import db, Project

# 创建 Flask 应用
app = Flask(__name__)
app.config.from_object(Config)

# 初始化数据库
db.init_app(app)

# 创建数据库表（适配 Flask 2.3+ 和 Python 3.11）
with app.app_context():
    db.create_all()

# 路由：主页
@app.route("/")
def index():
    return render_template("index.html")

# 路由：关于我
@app.route("/about")
def about():
    return render_template("about.html")

# 路由：项目列表
@app.route("/projects")
def projects():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)