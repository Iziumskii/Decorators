import datetime


def logger(old_function):

    def new_function(*args, **kwargs):
        start_time = datetime.datetime.utcnow()
        result = old_function(*args, **kwargs)
        with open("logs.txt", "w", encoding='utf-8') as file:
            file.write(f'{start_time}: {"Вызов функции"}\n{old_function}: {"Имя функции"}\n'
                       f'{*args, *kwargs}: {"Аргументы"}\n{result}: {"Возвращаемое значение"}')
        return result

    return new_function


@logger
def test_func(n, m):
    return n + m + 1


test_func(1, 2)

