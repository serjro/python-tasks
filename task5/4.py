# 4  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def to_rle(data):  # функция кодирования
    res, last, cnt = '', '', 1
    for char in data:
        if char != last:  # условие на повторение символа
            res += str(
                cnt) + last if last else ''  # добавляем число вхождений и сам символ, пропускаем если это первый символ
            cnt = 1
            last = char  # счетчик вхождений
        else:
            cnt += 1
    res += str(cnt) + last
    return res


def from_rle(data):  # функция декодирования
    res, cnt = '', ''
    for char in data:  # перебор строки
        if char.isdigit():  # проверка на цифру
            cnt += char  # устанавливаем счетчик в цифру
        else:
            res += char * int(cnt)  # размножаем символ по счетчику
            cnt = ''
    return res


f = open('files\\task_5-4_f1.txt', 'r', encoding="utf-8")  # считываем кодируемую строку
s = f.readline()
f.close()

enc = to_rle(s)  # кодируем

f = open('files\\task_5-4_f_encode.txt', 'w', encoding="utf-8")  # записываем результат кодирования
f.write(enc)
f.close()

dec = from_rle(enc)  # декодируем

f = open('files\\task_5-4_f_decode.txt', 'w', encoding="utf-8")  # записываем результат декодирования
f.write(dec)
f.close()

print('Кодируемая строка:', s)
print('Результат кодирования:', enc)
print('Результат декодирования:', dec)