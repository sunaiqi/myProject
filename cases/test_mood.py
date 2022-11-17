from api.my_test import *


def test_log_list():  # 查看心情日记列表
    check_login()
    response = requests.get(url=get_url("/mood/logList"), headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_mood_add_0():  # 提交心情-开心
    check_login()
    data1 = {'mood_type': '0', 'other1': '开心', 'other2': '', 'other3': ''}
    response = requests.get(url=get_url("/mood/logList"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['mood_type'] == '0'


def test_mood_add_01():  # 提交心情- 平淡
    check_login()
    data1 = {'mood_type': '1', 'other1': '不开心', 'other2': '', 'other3': ''}
    response = requests.get(url=get_url("/mood/logList"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['mood_type'] == '1'


def test_mood_add_02():  # 提交心情- 不开心
    check_login()
    data1 = {'mood_type': '2', 'other1': '不开心', 'other2': '', 'other3': ''}
    response = requests.get(url=get_url("/mood/logList"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['mood_type'] == '2'




