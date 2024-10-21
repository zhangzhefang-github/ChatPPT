# test_calculate_sum.py

def calculate_sum(a, b):
    # 假设这是你正在调试的函数
    # 你可以根据你的实际函数定义来替换它
    return a + b

def test_calculate_sum():
    try:
        # 测试案例：例如 2 + 3 应该等于 5
        assert calculate_sum(2, 3) == 6, "Test case 1 failed"
        assert calculate_sum(-1, 1) == 0, "Test case 2 failed"
        assert calculate_sum(0, 0) == 0, "Test case 3 failed"

        # 如果所有测试通过，返回成功信息
        print("All tests passed6")
        return True
    except AssertionError as e:
        print(e)
        return False

if __name__ == "__main__":
    # 调用测试函数并返回结果
    if test_calculate_sum():
        exit(0)  # 返回0表示测试通过
    else:
        exit(1)  # 返回1表示测试失败

