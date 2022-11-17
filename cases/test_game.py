from api.my_test import *


def test_log_list_kaola():  # 查看考拉摸摸历史训练记录
    check_login()
    data1 = {'game_type': '400'}
    response = requests.post(get_url("/game/logList"),
                             data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['game_type'] == 400


def test_log_list_zj():  # 查看最佳组合历史训练记录
    check_login()
    data1 = {'game_type': '401'}
    response = requests.post(get_url("/game/logList"),
                             data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['game_type'] == 401


def test_kl_add():  # 提交考拉摸摸- 不返回任何课程
    check_login()
    data1 = {'reaction_time': '0', 'y_trouble': '0', 'x_alertness': '0'}
    response = requests.post(get_url("/game/addCangShuMoMoLog"),
                             data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['courses'] == []


def test_kl_add01():  # 提交考拉摸摸- 返回工具学习
    check_login()
    data1 = {'reaction_time': '0', 'y_trouble': '100', 'x_alertness': '200'}
    response = requests.post(get_url("/game/addCangShuMoMoLog"),
                             data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['courses'] != []


def test_zj_add():  # 提交最佳组合- 返回心情日记
    check_login()
    data1 = {'negative_times': '2', 'best_match': '0', 'total_time': '257816'}
    response = requests.post(get_url("/game/addZuiJiaZuHeLog"),
                             data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['tools'][0]['title'] == "心情日记"


def test_zj_add01():  # 提交最佳组合- 返回课程
    check_login()
    data1 = {'negative_times': '10', 'best_match': '0', 'total_time': '257816'}
    response = requests.post(get_url("/game/addZuiJiaZuHeLog"),
                             data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['courses'] != []


def test_zj_add02():  # 提交最佳组合- 返回睡眠问卷
    check_login()
    data1 = {'negative_times': '17', 'best_match': '25', 'total_time': '257816'}
    response = requests.post(get_url("/game/addZuiJiaZuHeLog"),
                             data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['tools'][1]['title'] == "睡眠信念和态度问卷"


def test_zj_add03():  # 提交最佳组合- 返回睡眠问卷
    check_login()
    data1 = {'negative_times': '17', 'best_match': '25', 'total_time': '257816'}
    response = requests.post(get_url("/game/addZuiJiaZuHeLog"),
                             data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['tools'][1]['title'] == "睡眠信念和态度问卷"

