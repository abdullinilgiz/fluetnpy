# Use installed library
from latex_fluentpy.latex_gen import (list_to_tex_code,
                                      image_path_to_tex_code,
                                      wrap_tex_code)

if __name__ == '__main__':
    cells = [[1, 2, 3,],
             [4, 5, 6,],
             [7, 8, 9,]]
    table = list_to_tex_code(cells)
    image = image_path_to_tex_code('monkey.jpg')
    tex_code = wrap_tex_code((table, image))
    f = open('example.tex', 'a')
    f.write(tex_code)
    f.close()
