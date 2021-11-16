CRAFT_ROTATE_RATIO = 0.65
LINE_THRESHOLD = 0.0375

TIME_OUT = 15

PDF_FILE_FORMAT = ('.pdf', '.PDF')
IMG_FILE_FORMAT = ('.png', '.jpeg', '.jpg', '.PNG', '.JPEG', '.JPG')

A4_WIDTH = 4182
A4_HEIGHT = 5750

A3_WIDTH = 8270
A3_HEIGHT = 5792

OLD_TEMPLATE_CONFIG = {
    'HDMTK': [
        {
            'page': 0,
            'coord_A4': [(283 / A4_WIDTH, 3567 / A4_HEIGHT, 1215 / A4_WIDTH, 4475 / A4_HEIGHT),
                         (1056 / A4_WIDTH, 3566 / A4_HEIGHT, 2008 / A4_WIDTH, 4478 / A4_HEIGHT),
                         (2043 / A4_WIDTH, 3492 / A4_HEIGHT, 3936 / A4_WIDTH, 4713 / A4_HEIGHT)],
            'coord_A3': [(4372 / A3_WIDTH, 3952 / A3_HEIGHT, 5349 / A3_WIDTH, 4711 / A3_HEIGHT),
                         (5251 / A3_WIDTH, 3946 / A3_HEIGHT, 6179 / A3_WIDTH, 4715 / A3_HEIGHT),
                         (6296 / A3_WIDTH, 3738 / A3_HEIGHT, 8120 / A3_WIDTH, 4754 / A3_HEIGHT)],
            'main_sign_index': -1
        }
    ],
    'TDTT': [
        {
            'page': 0,
            'coord_A4': [(395 / A4_WIDTH, 3100 / A4_HEIGHT, 1576 / A4_WIDTH, 3850 / A4_HEIGHT),
                         (1576 / A4_WIDTH, 3100 / A4_HEIGHT, 2694 / A4_WIDTH, 3850 / A4_HEIGHT),
                         (2697 / A4_WIDTH, 3100 / A4_HEIGHT, 3826 / A4_WIDTH, 3850 / A4_HEIGHT)],
            'coord_A4_backup': [(2763 / A4_WIDTH, 3990 / A4_HEIGHT, 3963 / A4_WIDTH, 4771 / A4_HEIGHT)],
            'main_sign_index': -1
        },
        {
            'page': 1,
            'coord_A4': [(2771 / A4_WIDTH, 3517 / A4_HEIGHT, 4028 / A4_WIDTH, 4978 / A4_HEIGHT)]
        }
    ],
    'DKQLTK': [
        {
            'page': 0,
            'coord_A4': [(2708 / A4_WIDTH, 3685 / A4_HEIGHT, 3845 / A4_WIDTH, 4429 / A4_HEIGHT)],
            'coord_A4_backup': [(2604 / A4_WIDTH, 4755 / A4_HEIGHT, 4016 / A4_WIDTH, 5755 / A4_HEIGHT)],
            'main_sign_index': 0
        },
        {
            'page': 1,
            'coord_A4': [(2572 / A4_WIDTH, 3269 / A4_HEIGHT, 3572 / A4_WIDTH, 4217 / A4_HEIGHT)]
        }
    ],
    'DKQLTK_old': [
        {
            'page': 0,
            'coord_A4': [(565 / A4_WIDTH, 4964 / A4_HEIGHT, 1727 / A4_WIDTH, 5833 / A4_HEIGHT)],
            'main_sign_index': 0
        },
    ]
}
