from flask import Flask, request, jsonify, render_template


# 定义加法函数
def add(a, b):
    return a + b


# 定义减法函数
def subtract(a, b):
    return a - b


# 创建 Flask 应用
app = Flask(__name__)


# 定义首页路由，返回 HTML 表单页面
@app.route('/')
def index():
    return render_template('index.html')


# 处理计算请求的路由
@app.route('/result', methods=['GET'])
def calculate():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        operation = request.args.get('operation')

        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return render_template('result.html', result=result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
