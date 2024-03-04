if __name__ == '__main__':
    import sys
    import os

    args = sys.argv
    cnt = 0
    if len(args) > 1:
        current_dir = os.getcwd()
        path_to_file = args[1]
        path_to_file = os.path.join(current_dir, path_to_file)
        file = open(path_to_file)
        for row in file:
            cnt += 1
            row_num = str(cnt)
            row_num = ' ' * max(0, 6 - len(row_num)) + row_num
            print(row_num + '	' + row.rstrip('\n'))
    else:
        for stdin in sys.stdin:
            cnt += 1
            row_num = str(cnt)
            row_num = ' ' * max(0, 6 - len(row_num)) + row_num
            print(row_num + '	' + stdin, end='')
