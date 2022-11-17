from api.my_test import *


def test_content_list_1():  # 查看第一阶段课程列表
    """
    id = "45"
    """
    check_login()
    response = requests.get(get_url("/course/contentList?stage_no=1"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['stage_test']['stage_no'] == 1


def test_content_list_2():  # 查看第二阶段课程列表
    """
    id = "49"
    """
    check_login()
    response = requests.get(get_url("/course/contentList?stage_no=2"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['stage_test']['stage_no'] == 2


def test_content_list_3():  # 查看第三阶段课程列表
    """
    id = "51"
    """
    check_login()
    response = requests.get(get_url("/course/contentList?stage_no=3"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['stage_test']['stage_no'] == 3


def test_content_list_4():  # 查看第四阶段课程列表
    """
    id = "53"
    """
    check_login()
    response = requests.get(get_url("/course/contentList?stage_no=4"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['stage_test']['stage_no'] == 4


def test_stage_add_01():  # 提交第一阶段小测
    """
    id = "55"
    """
    check_login()
    data1 = {'answer': '1:b,2:a,3:c,4:c,5:a,6:b,7:d,8:b,9:a,10:c,11:b', 'stage_no': '1'}
    response = requests.post(url=get_url("/stageTest/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['ok_percent'] == 100


def test_stage_add_02():  # 提交第二阶段小测
    """
    id = "57"
    """
    check_login()
    data1 = {'answer': '1:a,2:a,3:a,4:b,5:a,6:b,7:a,8:b,9:c,10:a,11:a,12:c', 'stage_no': '2'}
    response = requests.post(url=get_url("/stageTest/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['ok_percent'] == 100


def test_stage_add_03():  # 提交第三阶段小测
    """
    id = "59"
    """
    check_login()
    data1 = {'answer': '1:b,2:b,3:b,4:d,5:b,6:b,7:d,8:a,9:a,10:b', 'stage_no': '3'}
    response = requests.post(url=get_url("/stageTest/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['ok_percent'] == 100


def test_stage_add_04():  # 提交第四阶段小测
    """
    id = "61"
    """
    check_login()
    data1 = {'answer': '1:b,2:b,3:b,4:b,5:a,6:a,7:d', 'stage_no': '4'}
    response = requests.post(url=get_url("/stageTest/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data']['ok_percent'] == 100


def test_course_add():  # 提交课程观看记录
    """
    id = "63"
    """
    check_login()
    data1 = {'percent': '100', 'section_no': '1'}
    response = requests.post(url=get_url("/course/addLog"), data=data1, headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


    

