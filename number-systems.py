dict = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F',
}


def with_hex_format(value, ns_to):
    if ns_to == 16 and value > 9 and value < 16:
        return dict[str(value)]
    return str(value)


def without_hex_format(value, ns_from):
    if ns_from == 16 and not value.isdigit():
        return int({v: k for k, v in dict.items()}[value])
    return int(value)


def number_systems(value, ns_from, ns_to):
    split = value.split('.')

    if len(split) == 1:
        return number_systems_int(value, ns_from, ns_to)

    if len(split) == 2:
        return f'{number_systems_int(split[0], ns_from, ns_to)}.{number_systems_float(
            split[1], ns_from, ns_to
        )}'


def number_systems_float(value, ns_from, ns_to, count=5):
    if ns_from == ns_to:
        return value
    if ns_from == 10:
        current_count = 0
        result = ''
        while current_count < count:
            result += with_hex_format(
                int(float(f'0.{value}') * ns_to), ns_to
            )
            value = str(float(f'0.{value}') * ns_to).split('.')[1]
            current_count += 1
        return result
    if ns_to == 10:
        value_by_ns_to = 0
        for i, char in enumerate(value):
            value_by_ns_to += without_hex_format(
                char, ns_from
            ) * ns_from ** (-i - 1)
        return str(value_by_ns_to).split('.')[1]


def number_systems_int(value, ns_from, ns_to):
    if ns_from == ns_to:
        return value
    if ns_from == 10:
        value = int(value)
        value_by_ns_to = ''
        while value // ns_to > 0:
            value_by_ns_to = with_hex_format(
                value % ns_to, ns_to
            ) + value_by_ns_to
            value //= ns_to
        value_by_ns_to = str(value) + value_by_ns_to
        return value_by_ns_to
    if ns_to == 10:
        value_by_ns_to = 0
        for i, char in enumerate(str(value)):
            value_by_ns_to += without_hex_format(
                char, ns_from
            ) * ns_from ** (len(str(value)) - i - 1)
        return value_by_ns_to


while input('Продолжить переводить числа?: ').lower() != 'нет':
    num = input('Введите число: ')
    ns_from = int(input('Введите исходную систему счисления: '))
    ns_to = int(input('Введите систему счисления, в которую перевести: '))
    print(number_systems(num, ns_from, ns_to))
