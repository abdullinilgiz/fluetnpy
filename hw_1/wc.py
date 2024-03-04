def get_num_with_indent(num: int, indent=2):
    num = str(num)
    num = ' ' * max(0, indent - len(num)) + num
    return num


def get_stats_for_file(file_path):
    file = open(file_path)
    num_bytes = 0
    num_words = 0
    num_lines = 0
    for line in file:
        num_bytes += len(line.encode('utf-8'))
        num_words += len(line.split())
        num_lines += line.count('\n')
    return {
        'num_bytes': num_bytes,
        'num_words': num_words,
        'num_lines': num_lines,
        }


if __name__ == '__main__':
    import sys
    import os

    args = sys.argv
    num_bytes = 0
    num_words = 0
    num_lines = 0

    stats_list = []
    max_indent = 1
    if len(args) > 1:
        current_dir = os.getcwd()
        path_to_files = args[1:]
        for file_path in path_to_files:
            full_file_path = os.path.join(current_dir, file_path)
            stats = get_stats_for_file(full_file_path)
            stats['file_path'] = file_path
            stats_list.append(stats)

            num_bytes += stats['num_bytes']
            num_words += stats['num_words']
            num_lines += stats['num_lines']
            max_indent = max(num_bytes, num_lines, num_words)

        if len(path_to_files) > 1:
            stats = {
                'num_bytes': num_bytes,
                'num_words': num_words,
                'num_lines': num_lines,
                'file_path': 'total',
            }
            stats_list.append(stats)

        max_indent = len(str(max_indent))
        for stats in stats_list:
            print(
                get_num_with_indent(stats['num_lines'], indent=max_indent),
                get_num_with_indent(stats['num_words'], indent=max_indent),
                get_num_with_indent(stats['num_bytes'], indent=max_indent),
                stats['file_path'],
            )

    else:
        for stdin in sys.stdin:
            num_bytes += len(stdin.encode('utf-8'))
            num_words += len(stdin.split())
            num_lines += stdin.count('\n')

        print(
            get_num_with_indent(num_lines, indent=7),
            get_num_with_indent(num_words, indent=7),
            get_num_with_indent(num_bytes, indent=7)
        )
