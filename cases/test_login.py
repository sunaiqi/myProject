from api.my_test import *


def test_agreement():  # 登录页查看用户协议和隐私政策
    """
    id = "41"
    """
    response = requests.get(url="https://wmhtml.wangli-tech.com/PrivacyAgreement/index.html",
                            headers=header)
    assert "隐私政策" in response.content.decode("utf-8")

#正确用户名和密码

def test_phone_empty():  # 手机号为空，返回200
    """
    id = "17"
    """
    response = login(phone='')
    assert response.status_code == 200


def test_phone_err():  # 手机号不存在，返回400
    """
    id = "25"
    """
    response = login(phone='11100000000')
    assert response.json() == {'code': 400, 'msg': '该手机号还未注册！'}


def test_patient_end():  # 疗程被终止
    """
    id = "27"
    """
    response = login(phone='13000000002')
    assert response.json() == {'code': 400, 'msg': '您的主治医生已中止您的当前治疗，请与主治医生联系!'}


def test_vcode_err():  # 验证码错误，返回400
    """
    id = "19"
    """
    check_login()
    response = login(vcode='123')
    assert response.json() == {"msg": "验证码错误", "code": 400}


def test_login_success():  # 登录成功，返回200
    """
    id = "15"
    """
    response = login()
    check_result(response)


def test_get_info():  # 登录成功后获取用户个人信息
    """
    id = "21"
    """
    check_login()
    response = requests.get(get_url("/patient/currentPatientDetail"),
                            headers=header)
    check_result(response)


def test_get_period():  # 获取用户疗程信息成功
    """
    id = "23"
    """
    check_login()
    response = requests.get(url + "/patient/periodTimeDetail",
                            headers=header)
    check_result(response)
