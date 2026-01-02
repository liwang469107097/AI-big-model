import random

stu_info = []


def update_info():
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询学生信息')
    print('5.遍历所有学生信息')
    print('6.退出系统')


def read_file(fname):
    global stu_info
    stu_info = []
    with open(fname, 'r', encoding='utf-8') as f_in:
        while True:
            line = f_in.readline().strip()
            if line:
                temp_list = line.split(',')
                stu_info.append({'id': int(temp_list[0]), 'name': temp_list[1], 'tel': temp_list[2]})
            else:
                break


def write_file(fname):
    with open(fname, 'w+', encoding='utf-8') as f_out:
        for info in stu_info:
            f_out.write(str(info['id']) + ',' + info['name'] + ',' + info['tel'] + '\n')
        f_out.flush()
        print('写入成功')


def add_info():
    stu_name = input('请输入学生姓名：')
    stu_tel = input('请输入学生手机号：')
    while True:
        stu_id = random.randint(1000000, 9999999)
        if stu_id not in stu_info:
            stu_info.append({'id': stu_id, 'name': stu_name, 'tel': stu_tel})
            print('学生信息录入成功！')
            break


def delete_info():
    stu_id = int(input('请输入需要删除的学生id：'))
    # 判断这个学生id是否存在
    for info in stu_info:
        if stu_id == info['id']:
            stu_info.remove(info)
            print(f'编号{stu_id}的学生信息删除成功！')
            break
    else:
        print(f'输入错误,没有编号{stu_id}的学生信息')


def change_info():
    stu_id = int(input('请输入需要修改的学生id：'))
    stu_name = input('请输入修改后的学生姓名：')
    stu_tel = input('请输入修改后的学生手机号：')
    for info in stu_info:
        if stu_id == info['id']:
            stu_info.remove(info)
            stu_info.append({'id': stu_id, 'name': stu_name, 'tel': stu_tel})
            print(f'编号{stu_id}的学生信息更新成功！')
            break
    else:
        print(f'输入错误,没有编号{stu_id}的学生信息')


def check_info():
    stu_id = int(input('请输入需要查询的学生id：'))
    for info in stu_info:
        if stu_id == info['id']:
            print(f'学生编号:{info['id']}')
            print(f'学生姓名:{info['name']}')
            print(f'学生手机号:{info['tel']}')
            break
    else:
        print(f'输入错误,没有编号{stu_id}的学生信息')


def check_all():
    for info in stu_info:
        print(f'学生编号:{info['id']}')
        print(f'学生姓名:{info['name']}')
        print(f'学生手机号:{info['tel']}')


if __name__ == '__main__':
    read_file('student_infomation.txt')
    print(stu_info)
    while True:
        update_info()
        print('-' * 32)
        input_choice = input('请输入功能编号：')
        if input_choice == '1':
            add_info()
        elif input_choice == '2':
            delete_info()
        elif input_choice == '3':
            change_info()
        elif input_choice == '4':
            check_info()
        elif input_choice == '5':
            check_all()
        elif input_choice == '6':
            write_file('student_infomation.txt')
            break
        else:
            print('输入错误,没有相关编号！')