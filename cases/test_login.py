from myProject.api.my_test import *


def test_number_password_correct():  # 正确用户名和密码
    """
    id = '1'
    """
    response = login()
    assert response.status_code == 200
    assert response.json()['code'] == 200
    assert response.json()['data']['token']


def test_number_empty():  # 用户名为空
    """
    id = '2'
    """
    response = login(number="")
    assert response.json() == {"msg": "该用户还未注册，请在中控端注册", "code": -1}
    assert response.status_code == 200


def test_password_empty():  # 密码为空
    """
    id = "3"
    """
    response = login(password="")
    assert response.json() == {"msg": "密码错误", "code": -2}
    assert response.status_code == 200


def test_password_error():  # 密码错误
    """
    id = "4"
    """
    response = login(password="zywd11")
    assert response.status_code == 200
    assert response.json() == {"msg": "密码错误", "code": -2}


def test_number_unregistered():  # 用户名未在中控注册
    """
    id = "5"
    """
    response = login(number="decade", password="decade")
    assert response.status_code == 200
    assert response.json() == {"msg": "该用户还未注册，请在中控端注册", "code": -1}

# def test_phone_empty():  # 手机号为空，返回200
#     """
#     id = "17"
#     """
#     response = login(phone='')
#     assert response.status_code == 200


# def test_phone_err():  # 手机号不存在，返回400
#     """
#     id = "25"
#     """
#     response = login(phone='11100000000')
#     assert response.json() == {'code': 400, 'msg': '该手机号还未注册！'}
#
#
# def test_patient_end():  # 疗程被终止
#     """
#     id = "27"
#     """
#     response = login(phone='13000000002')
#     assert response.json() == {'code': 400, 'msg': '您的主治医生已中止您的当前治疗，请与主治医生联系!'}
#
#
# def test_vcode_err():  # 验证码错误，返回400
#     """
#     id = "19"
#     """
#     check_login()
#     response = login(vcode='123')
#     assert response.json() == {"msg": "验证码错误", "code": 400}
#
#
# def test_login_success():  # 登录成功，返回200
#     """
#     id = "15"
#     """
#     response = login()
#     check_result(response)
#
#
# def test_get_info():  # 登录成功后获取用户个人信息
#     """
#     id = "21"
#     """
#     check_login()
#     response = requests.get(get_url("/patient/currentPatientDetail"),
#                             headers=header)
#     check_result(response)
#
#
# def test_get_period():  # 获取用户疗程信息成功
#     """
#     id = "23"
#     """
#     check_login()
#     response = requests.get(url + "/patient/periodTimeDetail",
#                             headers=header)
#     check_result(response)
