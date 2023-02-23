# # dodaj komentarz
#
# def dodaj(a: int, b: int) -> int:
#     """
#     :param a:
#     :param b:
#     :return:
#     """
#
#
#
#
dictionary = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'}
new_dict = {k: v for (k, v) in zip(dictionary.keys(), dictionary.values())}
print(new_dict)
# #
# # klucz = dictionary.keys()
# # wartosc = dictionary.values()
# #
for k, v in dictionary.items():
    print(k, v)
#
#
extensions = ['test.mp3', 'test2.flac', 'test3.jpg.zip']
results = []

for n in extensions:
    a = (n.split('.'))
    if 'zip' in a:
        a.remove('zip')
    print('a: ', a[-1])

route = [(3, 'w'), (2, 'e'), (3, 'n'), (2, 's')]
print(type(route))
for n in route:
    print(n[0])

seconds = 5

def oblicz_czas(route, seconds):
    final = []
    droga = 0
    for n in route:
        result = n[0]*seconds
        final.append(result)
        print(result)
    print(final)
    for n in final:
        droga += n
    print(droga)

oblicz_czas(route, seconds=seconds)





