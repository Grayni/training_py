from math import ceil


def jarriquez_encryption(text, key, a='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    letters = ''.join(filter(lambda x: x in a, text.upper()))
    key_str = (f'{key}' * ceil(len(text) / len(str(key))))[:len(text)]
    new_str = ''
    for i, key in enumerate(letters):
        new_str += a[(a.index(key) + (-1)**reverse * int(key_str[i])) % len(a)]

    return new_str


letter_author = 'ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС'

for i in range(1001, 1000000):
    key = i
    print(i)
    value = jarriquez_encryption(letter_author, key, a='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', reverse=True)
    if ('Дакоста'.upper() in value and 'алмаз'.upper() in value):
        print(value)
        break
