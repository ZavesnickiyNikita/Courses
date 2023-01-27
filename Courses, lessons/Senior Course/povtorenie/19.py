def tech_site():
    question_2 = input('Введите название продукта для нового сайта: ')
    answer = {
        'html': {
            'head': {
                'title': f'Куплю/продам {question_2} недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {question_2}',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }
    return answer

a = []
question_1 = int(input('Сколько сайтов вы хотите?'))
if question_1 == 1:
    print(tech_site())
else:
    for i in range(question_1):
        a.append(tech_site())
        print(*a, sep='\n')
