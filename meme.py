import time, random


meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            'РОФЛ': 'шутка',
            
            
            }

while True:
    command = input('Введите комманду (спросить, добавить):')
    if command == 'спросить':
        word = input("Введите непонятное слово (большими буквами!): ")
        if word in meme_dict.keys():
            # Что делать, если слово нашлось?
            print(meme_dict[word])
        else:
            # Что делать, если слово не нашлось?
            print('Мы о таком не слышали...')
    elif command == 'добавить':
        k1 = input('Напишите слово большими буквами:')
        k2 = input('Напишите значение слова:')
        meme_dict[k1] = k2
        print ('Мы добавили ваше слово')
