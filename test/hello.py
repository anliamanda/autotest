import pytest
# @pytest.mark.parametrize("input,expected",[("3+5",8),("2+5",7),("3*5",15)])
# def test_eval(input,expected):
# 	print("------------")
# 	print(eval(input))
#
# @pytest.mark.parametrize("x",[1,2])
# @pytest.mark.parametrize("y",[8,9,10])
# def test_multi(x,y):
# 	print(f"组合相乘{x}*{y}={x*y}")
	
# @pytest.fixture(params=[1,2,3,'linda'])
# def test_Data(req):
# 	return req.param
#
# def test_one(test_Data):
# # 	print('\ntest data:%s'%test_Data)
#
#
# user_Data=['amanda','jerry']
# @pytest.fixture(scope="module")
# def login_r(request):
# 	user=request.param
# 	print(f"\n 打开首页登陆，登陆用户：{user}")
#
#
# # #indirect=True 把login_r传过来的参数当作函数执行
# @pytest.mark.parametrize("login_r",user_Data,indirect=True)
# def test_login(login_r):
# 	a=login_r
# 	print(f"测试用例中login返回值:{a}")
# 	assert a !="tom"


@pytest.mark.parametrize(["a","b"],[(10,8),(5,7),(7,15)])
def test_param(a,b):
	print(a+b)