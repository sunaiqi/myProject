from api.my_test import *
import time


def test_data_list():  # 查看睡眠日记
    """
    id = "104"
    """
    check_login()
    response = requests.get(get_url("/sleepLog/logDateList"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_get_log():  # 查看当日睡眠日记
    """
    id = "107"
    """
    check_login()
    now_time = str(int(time.time()))
    response = requests.get(get_url("/sleepLog/getLog?time=" + now_time),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_week_list():  # 查看周统计
    """
    id = "110"
    """
    check_login()
    response = requests.get(get_url("/patient/periodWeekList"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_week_log():  # 查看指定周统计数据
    """
    id = "137"
    """
    check_login()
    response = requests.get(get_url("/sleepLog/statWeekLog?last_week_begin_time=1667750400"
                                    "&last_week_end_time=1668268800&week_begin_time=1668355200"
                                    "&week_end_time=1668873600"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()
