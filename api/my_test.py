import requests


url = 'https://wlxltest.wangli-tech.com:24443'
header = {
          "ACCESS-TOKEN": "null",
          "Accept": "*/*",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive",
          "Content-Length": "0",
          "Origin": "https://testxspg.wangli-tech.com",
          "Referer": "https://testxspg.wangli-tech.com/",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-site",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
          "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          "userType": "3"
}
params = {"number": "13", "password": "13"}


def check_result(response, code=200):  # 检查结果
    assert response.status_code == 200
    assert response.json()['code'] == code


def get_url(path):  # 获取完整url
    return url + path


def login(number="zywd1", password="zywd1"):  # 登录
    params['number'] = number
    params['password'] = password
    response = requests.post(url=get_url("/login/login/num-name?"),
                             params=params,
                             headers=header)
    return response


# print(login())


def check_login():  # 检查是否登陆 未登陆情况登陆并设置到header
    if 'access-token' not in header:
        response = login()
        check_result(response)
        header['access-token'] = response.json()['data']['token']




