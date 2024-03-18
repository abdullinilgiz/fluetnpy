def list_to_tex_code(table: list):
    tex_code = '\\begin{tabular}{ ' + 'c '*len(table[0]) + '}\n'
    tex_table_rows = []
    for row in table:
        tex_table_rows.append(' & '.join(map(str, row)))

    tex_code += ' \\\\\n'.join(tex_table_rows) + '\n'
    tex_code += '\\end{tabular}\n'
    return tex_code


def image_path_to_tex_code(image_path):
    tex_code = '\\begin{figure}[htp]\n'
    tex_code += '\\includegraphics[width=4cm]{' + image_path + '}\n'
    tex_code += '\\end{figure}\n'
    return tex_code


def wrap_tex_code(items):
    tex_code = ('\\documentclass{article}\n'
                '\\usepackage{graphicx}\n'
                '\\begin{document}\n')
    for item in items:
        tex_code += item
    return tex_code + '\\end{document}\n'
