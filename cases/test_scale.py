from api.my_test import *


def test_scale_type_500():  # 查看历史评估统计-失眠评估
    check_login()
    response = requests.get(get_url("/scale/logList?scale_type=500"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][0]['scale_type'] == 500


def test_scale_type_501():  # 查看历史评估统计-不合理想法
    check_login()
    response = requests.get(get_url("/scale/logList?scale_type=501"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][0]['scale_type'] == 501


def test_scale_type_502():  # 查看历史评估统计-焦虑
    check_login()
    response = requests.get(get_url("/scale/logList?scale_type=502"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][0]['scale_type'] == 502


def test_scale_type_503():  # 查看历史评估统计-抑郁
    check_login()
    response = requests.get(get_url("/scale/logList?scale_type=503"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][0]['scale_type'] == 503


def test_scale_add_500():  # 提交睡眠评估-无睡眠问题
    check_login()
    data1 = {'scale_type': '500', 'answer': '1:0,2:0,3:0,4:0,5:0,6:0,7:0'}
    response = requests.post(get_url("/scale/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['score'] == 0
    assert response.json()['result'] == '根据你的作答信息，你目前的睡眠情况很好，虽然在最近可能会有一些失眠的症状，但并不严重。如果你对目前的睡眠状态感到满意，那可以继续坚持之前的睡眠习惯，维持稳定的睡眠。如果你对目前的睡眠并不是很满意，可以通过学习睡眠卫生教育的知识，或者在入睡之前尝试放松训练的方式调整睡眠。'


def test_scale_add_501():  # 提交睡眠评估-无睡眠问题
    check_login()
    data1 = {'scale_type': '501', 'answer': '1:4,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:4,11:4,12:4,13:4,14:4,15:4,16:4,'
                                            '17:4,18:4,19:4,20:4,21:4,22:4,23:4,24:4,25:4,26:4,27:4,28:4,29:4,30:4'}
    response = requests.post(get_url("/scale/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['score'] == 1


def test_scale_add_502():  # 提交睡眠评估-无焦虑和抑郁
    check_login()
    data1 = {'scale_type': '502', 'answer': '1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0'}
    response = requests.post(get_url("/scale/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['yiyuLevel'] == '没有抑郁状态'
    assert response.json()['jiaolvLevel'] == '没有焦虑状态'





