import requests

url = 'https://mddtest.wangli-tech.com:5443'
header = {"Content-Type": "application/x-www-form-urlencoded", "client-version": "v1.0.8", "device-type": "0",
          "user-type": "0"}
data = {"phone": '15811289038', "vcode": '999999'}


def check_result(response, code=200):  # 检查结果
    assert response.status_code == 200
    assert response.json()['code'] == code


def get_url(path):  # 获取完整url
    return url + path


def login(phone='15811289038', vcode='999999'):  # 登录
    data['phone'] = phone
    data['vcode'] = vcode
    response = requests.post(url=get_url("/login/login"),
                             data=data,
                             headers=header)
    return response


def check_login():  # 检查是否登陆 未登陆情况登陆并设置到header
    if 'access-token' not in header:
        response = login()
        check_result(response)
        header['access-token'] = response.json()['data']['token']
