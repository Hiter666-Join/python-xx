content = int(input('输入1-3的数字\n'))
match content:
    case 1:
        print('这个是 1')
    case 2:
        print('这个是 2')
    case 3:
        print('这个是 3')
    case _:
        print('这个不是 1-3')