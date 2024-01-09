import random

ORIGIN = {
    1: 'Случайное. Торговый пост появился в результате несчастного случая, такого как поломка каравана или неправильное направление. То, что было создано для ликвидации последствий аварии, в конечном итоге превратилось в торговый пост',
    2: 'Деловое предприятие. Торговый пост был основан богатым предпринимателем специально для того, чтобы с самого начала быть торговым постом.',
    3: 'Перекресток дорог. Торговый пост находится на пересечении более чем одного крупного торгового пути.',
    4: 'Военный аванпост. Торговый пост был построен на остатках старой крепости или сторожевой башни, строения которой давно обрушились или были переделаны местными жителями.',
    5: 'Нейтральная территория. Торговый пост был создан как нейтральное место, где противоборствующие силы могли приобретать товары, не вторгаясь на вражескую территорию',
    6: 'Местные. Торговый пост был основан кем-то из местных жителей, кто увидел потенциал в торговле с прохожими.',
    7: 'Ночлежка. Первоначально торговый пост представлял собой единый большой дом для ночлега усталых путешественников, который вскоре вырос вместе со спросом на жилье.',
    8: 'Эксперт по выживанию. Торговый пост был основан, когда траппер, охотник или проводник разбил лагерь, чтобы помочь тем, кто проходит через этот район.'
}
SPECIALITY = {
    1: 'Нестандартные способы доставки',
    2: {1:'Еда и Напитки: Этот торговый пост знаменит за свою отличную и уникальную еду',
        2:'Еда и Напитки: Этот торговый пост известен большим разнообразием первоклассных напитков'},
    3: 'Гостиничный бизнес',
    4: 'Информирование',
    5: 'Приобретение связей',
    6: {1:'Наёмники: Силачи и дебоширы',
        2:'Наёмники: Плащ и кинжал',
        3:'Наёмники: Луки и пращи',
        4:'Наёмники: Писари и канцеляристы',
        5:'Наёмники: Проводники и следопыты',
        6:'Наёмники: Караванщики и наездники',
        7:'Наёмники: Академики магии',
        8:'Наёмники: Магические наемники',
        9:'Наёмники: Священнослужители',
        10:'Наёмники: Руки Божества'}
}
AGE = {
    3: 'Недавний',
    8: 'Устоявшийся',
    13: 'Развитый',
    17: 'Старый',
    19: 'Древний',
    20: 'Не известно'
}

CONDITION = {
    2: 'Ветхое',
    6: 'Бедное',
    14: 'Облагороженное',
    18: 'Хорошее',
    20: 'Безупречное'
}

VISITOR_TRAFFIC = {
    2: 'Пустой',
    6: 'Группы',
    14: 'Толпы',
    18: 'Массы',
    20: 'Орды'
}
SIZE = {
    2: 'Очень маленький',
    6: 'Маленький',
    14: 'Средний',
    18: 'Большой',
    20: 'Очень большой'
}
ENVIRONMENT = {
    1: 'Берег',
    2: 'Лес',
    3: 'Горы',
    4: 'Равнины',
    5: 'Река',
    6: 'Болото',
    7: 'Подземье',
    8: 'Долина',
    9: 'Тундра',
    10: 'Пустыня'
}
POPULATION = {
    2: 'Почти безлюдный',
    6: 'Немногочисленное',
    14: 'Приемлемое',
    18: 'Переполненное',
    20: 'Ошеломляющее'
}
DEMOGRAPHICS = {
    5: 'Одна раса',
    10: 'Две расы',
    14: 'Нормальное распределение',
    17: 'Широкое распределение',
    19: 'Высокий и низкий уровень',
    20: 'Постоянно меняющаяся'
}
DISPOSITION = {
    2: 'Враждебность',
    6: 'Недружелюбие',
    14: 'Нейтральность',
    18: 'Дружелюбие',
    20: 'Радушие'
}
ENFORCEMENT = {
    2: 'Отсутствуют',
    6: 'Шерифф',
    14: 'Небольшой местный дозор',
    18: 'Хорошо укомплектованы',
    20: 'Ошеломляющее присутствие'
}
LEADERSHIP = {
    1: 'Нет лидера',
    4: 'Наследник',
    7: 'Монарх-торговец',
    10: 'Преступный мир или преступное предприятие',
    13: {1:'Олигархия: Торговцы (плутократия)',
        2:'Олигархия: Маги (магократия)',
        3:'Олигархия: Жрецы (теократия)',
        4:'Олигархия: Другая малая группа'},
    16: 'Местный совет',
    19: 'Единый, избранный лидер',
    20: 'Анархо-синдикалистская коммуна',
}
POPULATION_WEALTH = {
    2: 'Обездоленное',
    6: 'Обедневшее',
    14: 'Достаточное',
    17: 'Процветающее',
    19: 'Зажиточное',
    20: 'Изобильное'
}
CRIME = {
    2: 'Высокая преступность',
    6: 'Распространены',
    14: 'Обычно',
    18: 'Нечастые',
    20: 'Редкие'
}
SHOPS = {
    4: 'Пекарь',
    8: 'Мясник',
    12: 'Бондарь',
    16: 'Плотник',
    24: 'Универсальный магазин',
    28: 'Травник',
    36: 'Кузница',
    40: 'Портной',
    44: 'Кожевник/таксидермист',
    48: 'Кровельщик',
    52: 'Каретных дел мастер',
    56: 'Ткач',
    59: 'Алхимик',
    62: 'Художник',
    65: 'Банк и биржа',
    68: 'Сапожник',
    71: 'Литейное производство/плавильня',
    74: 'Мельница',
    77: 'Текстильное производство',
    80: 'Корабельщик',
    82: 'Редкие растения',
    84: 'Роскошная мебель',
    86: 'Редкие напитки и закуски',
    88: 'Редкие товары для торговли',
    90: 'Волшебный магазин: Броня',
    92: 'Волшебный магазин: Книги',
    94: 'Волшебный магазин: Одежда',
    96: 'Волшебный магазин: Ювелирный',
    98: 'Волшебный магазин: Оружие',
    100: 'Волшебный магазин: Чудесные предметы'
    }
SERVICES = {
    8: 'Парикмахерская',
    16: 'Баня',
    24: 'Врач/аптекарь',
    32: 'Дом отдыха',
    44: 'Постоялый двор',
    52: 'Клуб',
    60: 'Прорицатель',
    68: 'Конюшня',
    80: 'Таверна',
    82: 'Наемные работники: Силачи и дебоширы',
    84: 'Наемные работники: Плащ и кинжал',
    86: 'Наемные работники: Луки и пращи',
    88: 'Наемные работники: Писари и клерки',
    90: 'Наемные работники: Проводники и следопыты',
    92: 'Наемные работники: Караванщики и наездники',
    94: 'Наемные работники: Академики магии',
    96: 'Наемные работники: Магические наемники',
    98: 'Наемные работники: Священнослужители',
    100: 'Наемные работники: Руки Бога'
    }
QUALITY = {
    4: 'Плохое качество',
    10: 'Хорошее качество',
    12: 'Отличное качество'
    }
HIRED_HELP = {
    6: 'Одиночка',
    10: 'Команда',
    12: 'Гильдия'
    }
WORSHIP = {
    1: 'Место поклонения: Тайное место',
    8: 'Место поклонения: Алтарь ',
    14: 'Место поклонения: Ораторий',
    17: 'Место поклонения: Святилище',
    19: 'Место поклонения: Храм',
    20: 'Место поклонения: Большой Храм'
    }
WORSHIP_FERVENCY = {
    1: 'Незаметное почитание местных жителей',
    5: 'Молчаливое почитание местных жителей',
    10: 'Сдержанное почитание местных жителей',
    16: 'Умеренное почитание местных жителей',
    19: 'Пылкое почитание местных жителей',
    20: 'Ревностное почитание местных жителей'
}
WORSHIP_ALIGNMENT = {
    1: 'Злое мировоззрение',
    5: 'Нейтральное мировоззрение',
    10: 'Доброе мировоззрение'
}
HISTORY = {
    1: 'Захваченная власть после доброжелательного лидера',
    2: 'В процессе строительства',
    3: 'Бывший криминальный центр',
    4: 'Нейтралитет',
    5: 'Популярный производитель',
    6: 'Разорванные войной'
}
POLITICS = {
    1: 'На грани войны',
    2: 'Беззаконный район',
    3: 'В боевой готовности',
    4: 'Революция',
    5: 'Мир',
    6: 'Новое управление'
}
EVENTS = {
    1: 'Посетитель высшего класса',
    2: 'Нарушители спокойствия',
    3: 'Фестиваль дураков',
    4: 'Поймали с поличным',
    5: 'Чужеземцы',
    6: 'Общественная чрезвычайная ситуация'
}
OPPORTUNITIES = {
    1: 'Политическая интрига',
    2: 'Пропал человек',
    3: 'Расправиться с монстром',
    4: 'Помощь караульной службе',
    5: 'Помощь с транспортировкой',
    6: 'Спрятанный артефакт'
}
WEATHER = {
    2: 'Хорошая',
    6: 'Мягкая',
    14: 'Обычная',
    18: 'Суровая',
    20: 'Плохая'
}
DANGER_LEVEL = {
    2: 'Постоянный',
    6: 'Частый',
    14: 'Обычный',
    18: 'Иногда случается',
    20: 'Редко случается'
}
DANGER_TYPE = {
    2: 'Подозрительные местные жители',
    6: 'Набеги',
    14: 'Монстр',
    18: 'Погодные опасности',
    20: 'Культисты'
}

#обычный ролл (цезарь-ролл от Макдональдс)
def roll(d): 
    roll_result = random.randint(1, d)
    return roll_result

#новая функция, которая выводит значение из таблицы, проверяя выпавший ролл и есть ли вложенные списки внутри списков
def label(roll_result, table):
    for i in table.keys():
        if roll_result <= i:
            if type(table[i]) == dict:
                additional_roll = roll(len(table[i]))
                return table[i][additional_roll], list(table).index(i)+1
            return table[i], list(table).index(i)+1
    return list(table.values())[-1], len(table)

#высчитывает модификаторы по таблицам
def dice_modifier(start, roll_result, step, table):
    modifier = start + step * (label(roll_result, table)[1] - 1)
    return modifier

#ШАГ ПЕРВЫЙ
origin_roll = roll(8)
speciality_roll = roll(6)
age_roll = roll(20)
age_to_traffic_modifier = dice_modifier(-1, age_roll, 1, AGE)
condition_roll = roll(20)
condition_to_wealth_modifier = dice_modifier(-6, condition_roll, 3, CONDITION)
traffic_roll = roll(20) + age_to_traffic_modifier
traffic_to_size_modifier = dice_modifier(0, traffic_roll, 1, VISITOR_TRAFFIC)
traffic_to_crime_modifier = dice_modifier(2, traffic_roll, -1, VISITOR_TRAFFIC)
size_roll = roll(20)
size_to_shops_modifier = dice_modifier(2, size_roll, 2, SIZE)
size_to_services_modifier = dice_modifier(-1, size_roll, 2, SIZE)
if size_to_services_modifier==-1:
    size_to_services_modifier=0
environment_roll = roll(10)

print('\nБАЗОВАЯ ИНФОРМАЦИЯ')
print(f'Происхождение: {label(origin_roll, ORIGIN)[0]} ({origin_roll})')
print(f'Специализация: {label(speciality_roll, SPECIALITY)[0]} ({speciality_roll})')
print(f'Возраст: {label(age_roll, AGE)[0]} ({age_roll}) (мод. возраст-трафик [{age_to_traffic_modifier}])')
print(f'Состояние: {label(condition_roll, CONDITION)[0]} ({condition_roll}) (мод. состояние-благосостояние [{condition_to_wealth_modifier}])')
print(f'Трафик: {label(traffic_roll, VISITOR_TRAFFIC)[0]} ({traffic_roll-age_to_traffic_modifier})+[{age_to_traffic_modifier}] (мод. трафик-размер [{traffic_to_size_modifier}]) (мод. трафик-преступление [{traffic_to_crime_modifier}])')
print(f'Размер: {label(size_roll, SIZE)[0]} ({size_roll})')
print(f'Окружение: {label(environment_roll, ENVIRONMENT)[0]} ({environment_roll})')

#ШАГ ВТОРОЙ
population_roll = roll(20)
population_to_crime_modifier = dice_modifier(2, population_roll, -1, POPULATION)
demographics_roll = roll(20)
disposition_roll = roll(20)
enforcement_roll = roll(20)
enforcement_to_crime_modifier = dice_modifier(-8, enforcement_roll, 4, ENFORCEMENT)
leadership_roll = roll(20)
population_wealth_roll = roll(20) + condition_to_wealth_modifier
population_wealth_to_crime_modifier = dice_modifier(-4, population_wealth_roll, 2, POPULATION_WEALTH)
population_wealth_to_quality_modifier = dice_modifier(-2, population_wealth_roll, 1, POPULATION_WEALTH)
crime_roll = roll(20) + population_to_crime_modifier + traffic_to_crime_modifier + enforcement_to_crime_modifier + population_wealth_to_crime_modifier
crime_to_encounter_modifier = dice_modifier(4, crime_roll, -1, CRIME)

print('\nОБЩЕСТВО')
print(f'Численность населения: {label(population_roll, POPULATION)[0]} ({population_roll}) (мод. численность-преступление [{population_to_crime_modifier}])')
print(f'Демография: {label(demographics_roll, DEMOGRAPHICS)[0]} ({demographics_roll})')
print(f'Отношение к путникам: {label(disposition_roll, DISPOSITION)[0]} ({disposition_roll})')
print(f'Правоохранительные органы: {label(enforcement_roll, ENFORCEMENT)[0]} ({enforcement_roll}) (мод. охраны-преступление [{enforcement_to_crime_modifier}])')
print(f'Руководство: {label(leadership_roll, LEADERSHIP)[0]} ({leadership_roll})')
print(f'Благосостояние: {label(population_wealth_roll, POPULATION_WEALTH)[0]} ({population_wealth_roll-condition_to_wealth_modifier})+[{condition_to_wealth_modifier}] (мод. благосостояние-преступление [{population_wealth_to_crime_modifier}]) (мод. благосостояние-качество [{population_wealth_to_quality_modifier}])')
print(f'Преступность: {label(crime_roll, CRIME)[0]} ({crime_roll-population_to_crime_modifier-traffic_to_crime_modifier-enforcement_to_crime_modifier-population_wealth_to_crime_modifier})+[{population_to_crime_modifier}]+[{traffic_to_crime_modifier}]+[{enforcement_to_crime_modifier}]+[{population_wealth_to_crime_modifier}]={crime_roll} (мод. преступность-городские встречи [{crime_to_encounter_modifier}])')

#ШАГ ТРЕТИЙ
print('\nТОЧКИ ИНТЕРЕСА')
shops = roll(8) + size_to_shops_modifier
print(f'Магазины ({shops-size_to_shops_modifier}+[{size_to_shops_modifier}]):')
shop_list = {}
shop_list[0] = ['Универсальный магазин']
unishop_quality_roll = roll(12) + population_wealth_to_quality_modifier
shop_list[0].append(label(unishop_quality_roll, QUALITY)[0])
unishop_help_roll = roll(12)
shop_list[0].append(label(unishop_help_roll, HIRED_HELP)[0])
print(f'0. {shop_list[0]}')
for i in range(shops):
    x = roll(100)
    shop_list[x] = [label(x, SHOPS)[0]]
    y = roll(12) + population_wealth_to_quality_modifier
    shop_list[x].append(label(y, QUALITY)[0])
    z = roll(12)
    shop_list[x].append(label(z, HIRED_HELP)[0])
    print(f'{i+1}. ({x}): {shop_list[x]}')

services = roll(6) + size_to_services_modifier
print(f'Услуги ({services-size_to_services_modifier}+[{size_to_services_modifier}]):')
service_list = {}
service_list[0] = ['Постоялый двор']
service_quality_roll = roll(12) + population_wealth_to_quality_modifier
service_list[0].append(label(service_quality_roll, QUALITY)[0])
service_help_roll = roll(12)
service_list[0].append(label(service_help_roll, HIRED_HELP)[0])
print(f'0. {service_list[0]}')
for i in range(services):
    x = roll(100)
    service_list[x] = [label(x, SERVICES)[0]]
    y = roll(12) + population_wealth_to_quality_modifier
    service_list[x].append(label(y, QUALITY)[0])
    z = roll(12)
    service_list[x].append(label(z, HIRED_HELP)[0])
    print(f'{i+1}. ({x}): {service_list[x]}')
print('Места поклонения:')
if roll(2) == 1:
    print('Отсутствуют')
else:
    worship_size_roll = roll(20)
    worship_fervency_roll = roll(20)
    worship_alignment_roll = roll(10)
    print(f'({worship_size_roll}) {label(worship_size_roll, WORSHIP)[0]} - {label(worship_fervency_roll, WORSHIP_FERVENCY)[0]} - {label(worship_alignment_roll, WORSHIP_ALIGNMENT)[0]}')

#дополнительная интрига
history_roll = roll(6)
politics_roll = roll(6)
events_roll = roll(6)
opportunities_roll = roll(6)
weather_roll = roll(20)
danger_level_roll = roll(20)
danger_type_roll = roll(10)

print('\nДополнительная интрига:')
print(f'Недавняя история: {label(history_roll, HISTORY)[0]} ({history_roll})')
print(f'Политическая ситуация: {label(politics_roll, POLITICS)[0]} ({politics_roll})')
print(f'Текущие события: {label(events_roll, EVENTS)[0]} ({events_roll})')
print(f'Возможности: {label(opportunities_roll, OPPORTUNITIES)[0]} ({opportunities_roll})')
print(f'Погода по прибытию: {label(weather_roll, WEATHER)[0]} ({weather_roll})')
print(f'Уровень опасности: {label(danger_level_roll, DANGER_LEVEL)[0]} ({danger_level_roll})')
print(f'Тип опасности: {label(danger_type_roll, DANGER_TYPE)[0]} ({danger_type_roll})')
