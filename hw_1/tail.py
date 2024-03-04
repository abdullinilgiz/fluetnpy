import collections


def tail(file_path, num_lines=10):
    with open(file_path, 'r') as file:
        lines = collections.deque()
        for line in file:
            lines.append(line)
            if len(lines) > num_lines:
                lines.popleft()
        return lines


if __name__ == '__main__':
    import sys
    import os

    args = sys.argv
    if len(args) > 1:
        current_dir = os.getcwd()
        path_to_files = args[1:]
        first = True
        for file_path in path_to_files:
            if len(path_to_files) > 1:
                if not first:
                    print()
                print(f'==> {file_path} <==')
            file_path = os.path.join(current_dir, file_path)
            for line in tail(file_path):
                print(line, end='')
            first = False
    else:
        lines = collections.deque()
        for line in sys.stdin:
            lines.append(line)
            if len(lines) > 10:
                lines.popleft()
        for line in lines:
            print(line, end='')
