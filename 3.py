# 接收用户输入的账号和密码，如果账号为'admin'，密码为'admin888'，
# 则提示用户登录成功，其他情况则提示用户名或密码输入错误，只有3次输入机会。


n = 1
while n <= 3:
    username = input('用户名：')
    password = input('密码：')
    if username == 'admin':
        if password == 'admin888':
            print('登录成功')
            break
        else:
            print('密码错误')
            print(f'您还有{3 - n}次输入机会')
    else:
        print('用户名错误')
        print(f'您还有{3 - n}次输入机会')
    n += 1

