from api.my_test import *


def test_tasklist():  # 获取用户今日任务
    """
    id = "29"
    """
    check_login()
    response = requests.get(get_url("/task/taskList"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_get_plan():  # 获取用户睡眠方案
    """
    id = "33"
    """
    check_login()
    response = requests.get(get_url("/sleepPlan/getPlan"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()
    # assert response.json()['data']['logs_num'] > 3


def test_robot():  # 获取机器人窗口
    """
    id = "31"
    """
    check_login()
    response = requests.get(get_url("/chat/robot"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_health_add():  # 提交每日睡眠小知识
    """
    id = "35"
    """
    check_login()
    data1 = {'section_no': '1'}
    response = requests.post(url=get_url("/health/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_mood_add():  # 提交心情日记
    """
    id = "37"
    """
    check_login()
    data1 = {'mood_type': '0', 'other1': '好开心'}
    response = requests.post(url=get_url("/mood/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()
    assert response.json()['data']['mood_type'] == 0


def test_sleep_add():  # 提交睡眠日记
    """
    id = "39"
    """
    check_login()
    data1 = {'bed_time': '1668092400', 'sleep_time': '1668092400',
             'bed_action': '[{"option":"a","text":"吃零食或宵夜"}]',
             'before_sleep_action': '[{"option":"b","text":"喝酒或含咖啡因饮料"}]',
             'wakeup_time': '1668121200', 'getup_time': '1668121200',
             'all_night_no_sleep': '0', 'night_wakeup_times': '0',
             'night_wakeup_total': '0', 'day_sleep_times': '0',
             'day_sleep_total': '0', 'take_medicine': '0',
             'feel': '4', 'other': '无', 'day_time': '1668096000'}
    response = requests.post(url=get_url("/sleepLog/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_relax_add():  # 进行一次肌肉放松
    """
    id = "43"
    """
    check_login()
    data1 = {'relax_type': '103'}
    response = requests.post(url=get_url("/relax/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()
