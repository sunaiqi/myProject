from api.my_test import *


def test_relax_types_101():  # 查看放松列表-减压游戏是否显示
    """
    id = "134"
    """
    check_login()
    response = requests.get(get_url("/relax/contentTypes"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][0]['relax_type_title'] == "减压游戏"


def test_relax_types_102():  # 查看放松列表-呼吸放松
    """
    id = "113"
    """
    check_login()
    response = requests.get(get_url("/relax/contentTypes"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][1]['relax_type_title'] == "呼吸放松"


def test_relax_types_103():  # 查看放松列表-肌肉放松
    """
    id = "116"
    """
    check_login()
    response = requests.get(get_url("/relax/contentTypes"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][2]['relax_type_title'] == "肌肉放松"


def test_relax_types_104():  # 查看放松列表-想象放松
    """
    id = "119"
    """
    check_login()
    response = requests.get(get_url("/relax/contentTypes"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][3]['relax_type_title'] == "想象放松"


def test_relax_types_105():  # 查看放松列表-正念训练
    """
    id = "122"
    """
    check_login()
    response = requests.get(get_url("/relax/contentTypes"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][4]['relax_type_title'] == "正念训练"


def test_relax_types_106():  # 查看放松列表-自然白噪音
    """
    id = "125"
    """
    check_login()
    response = requests.get(get_url("/relax/contentTypes"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][5]['relax_type_title'] == "自然白噪音"


def test_relax_types_107():  # 查看放松列表-生活白噪音
    """
    id = "128"
    """
    check_login()
    response = requests.get(get_url("/relax/contentTypes"),
                            headers=header)
    code = response.json()['code']
    assert code == 200
    assert response.json()['data'][6]['relax_type_title'] == "生活白噪音"


def test_game_add():  # 提交游戏
    """
    id = "131"
    """
    check_login()
    data1 = {'relax_type': '101'}
    response = requests.post(get_url("/relax/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_breathe_add():  # 提交呼吸放松
    """
    id = "140"
    """
    check_login()
    data1 = {'relax_type': '102'}
    response = requests.post(get_url("/relax/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_muscle_add():  # 提交肌肉放松
    """
    id = "143"
    """
    check_login()
    data1 = {'relax_type': '103'}
    response = requests.post(get_url("/relax/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_imagine_add():  # 提交想象放松
    """
    id = "146"
    """
    check_login()
    data1 = {'relax_type': '104'}
    response = requests.post(get_url("/relax/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_mindfulness_add():  # 提交正念放松
    """
    id = "149"
    """

    check_login()
    data1 = {'relax_type': '105'}
    response = requests.post(get_url("/relax/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_natural_add():  # 提交自然白噪音
    """
    id = "152"
    """
    check_login()
    data1 = {'relax_type': '106'}
    response = requests.post(get_url("/relax/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()


def test_life_add():  # 提交生活白噪音
    """
    id = "155"
    """
    check_login()
    data1 = {'relax_type': '107'}
    response = requests.post(get_url("/relax/addLog"), data=data1,
                             headers=header)
    code = response.json()['code']
    assert code == 200
    assert 'data' in response.json()
