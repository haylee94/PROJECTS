'''
터미널에서 'Python app.py'를 실행하면
index.html 파일이 뜨게 됨
debug모드로 띄워놓고, 브라우저 새로고침하면서 수정!
'''

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')
    
# report 페이지에 주요 변수들과 함수들을 정의해 준다.

@app.route('/report')
def report():
#입력받은 userid를 변수로 사용한다는 선언이다.
    userid = request.args.get('userid')

# 기본적으로 False로 시작하고 아래에서 True일 경우 덮어씌워진다.
    lower_letter = False
    upper_letter = False
    num_end = False

    # 아까 짰던 코드들을 넣어주자.
    upper_letter = any(c.isupper() for c in userid)
    lower_letter = any(c.islower() for c in userid)
    num_end = userid[-1].isdigit()
    
    report = lower_letter & upper_letter & num_end

# 사용될 모든 변수들을 render_template에 정의해주어야 html에서 작동할 수 있다. 
    return render_template('report.html',userid=userid, lower=lower_letter, upper = upper_letter, num_end=num_end, report=report)

if __name__ == '__main__':
    app.run(debug=True)