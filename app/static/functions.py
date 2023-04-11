def format_timedelta(delta):
    time_parts = [
        {'name': 'нед', 'duration': 60*60*24*7},
        {'name': 'д', 'duration': 60*60*24},
        {'name': 'ч', 'duration': 60*60},
        {'name': 'мин', 'duration': 60},
        {'name': 'сек', 'duration': 1}
    ]

    seconds = int(delta.total_seconds())

    for part in time_parts:
        count = seconds // part['duration']
        if count:
            return '{} {}'.format(count, part['name'])

    return 'только что'
