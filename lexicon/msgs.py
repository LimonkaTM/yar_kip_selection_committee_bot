msgs = {
    '1': {
        'name': 'фыва',
        'content': '1',
    },
    '1.1': {
        'name': 'фывафва',
        'content': '1.1',
    },
    '1.1.1': {
        'name': 'sadf',
        'content': '1.1.1',
    },
}

btns = {
    'back': {
        'content': 'Назад',
        'fn': 'open_msg',
    },
    'open_profs': {
        'content': 'Открыть 1.1.1',
        'fn': 'open_msg',
    },
    'main': {
        'content': 'Открыть 1',
        'fn': 'open_url',
    },
    'btn_1.1': {
        'content': 'Открыть 1.1',
        'fn': 'open_msg',
    }
}

btns_msgs = {
    # '1': ['back'],
    # '1.1': ['open_profs', 'back']
    '1': {
        'btn_1.1': '1.1'
    },
    '1.1': {
        'open_profs': '1.1.1',
        'back': '1'
    },
    '1.1.1': {
        'main': 'https://yar-kip.edu.yar.ru/studentam/raspisanie.html',
        'back': '1.1'
    }
}
