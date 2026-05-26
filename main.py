from random import *  # Импорт модуля рандома
from time import time, sleep
from colorama import init, Fore as F, Style as S  # Импорт модуля для раскраски строчек 
init(autoreset=True)   # После каждой строки цвет сбрасывается сам

# Определим переменных цвета,чтобы код в последствии стал короче и читабельней

R = F.RED
RR = F.LIGHTRED_EX
G = F.GREEN
GG = F.LIGHTGREEN_EX
Y = F.YELLOW
YY = F.LIGHTYELLOW_EX
B = F.BLUE
BB = F.LIGHTBLUE_EX
C = F.CYAN
M = F.MAGENTA
MM = F.LIGHTMAGENTA_EX
W = F.WHITE
S = S.RESET_ALL


# Приветствие и обработка имени

def valid_name():
    global user
    name_otvet = input(
            f'\nПриветствую тебя в игре - {GG}"Угадайка слов"{S}\n'
            f'Как к тебе можно обращаться?\n\n{Y}'  
        )
    if name_otvet.isdigit():
        user["name_user"] = name_otvet
        print("\nТы число? - Ладно...\n\n")
    else:
        if name_otvet.isalpha:
            user["name_user"] = name_otvet[0].upper() + name_otvet[1:]
            print(f'\nПриятно познакомиться {Y}{user["name_user"]}{S}!\n\n')
        else:
            print(f'\nДавай-ка мы лучше введем корректное имя состоящее из {R}букв{S}!\n\n')


# Проверка ответа юзера на предложенные варианты

def valid_otvet(otvet, num):
    while True:
        if otvet.isdigit():
            if 1 <= int(otvet) <= num:
                return int(otvet)
            else:
                otvet = input(f'\nВыбери {R}вариант{S} из предложенных! От 1 до {num}\n\n{Y}') 
        else:
            otvet = input(f'\nВыбери {R}числовой вариант{S} из предложенных! От 1 до {num}\n\n{Y}')


# Все характеристики юзера в одном словаре

def player_stats():
    global user
    user = {
        "name_user": "",
        "user_damage": 0,
        "user_damage_fact": 1,
        "user_heath": 0,
        "user_heath_fact": 10,
        "user_wearon": [],
        "gold": 1000,
        "gold_bank": 0,
        "start_vklad": 0,
        "exp": 0,
        "lvl": 1,
        "hard_game_1": 1,
        "hard_game_2": 1,
        "win_game_1": 0,
        "win_game_2": 0,
        "baf_damage": 0,
        "baf_heath": 0  
    }



# Все правила которые потребуются для знакомства с игрой, каждый ряд правил для своей "локации"

def pravila(location):
    while True:
        if location == "game_1":
            print(
                f'\nПравила игры - "{RR}Угадай число{S}"\n\n'
                f'{BB}(1){S} Ты выбираешь сложность от {Y}1{S} до {Y}бесконечности{S}\n'
                f'{BB}(2){S} Сложность это какой будет интервал угадывания: от 1 до сложность * 10\n'
                f'{BB}(3){S} Компьютер загадывает число и ты должен его угадать\n'
                f'{BB}(4){S} Если ты угадал то получаешь: случайную награду из выбранно интервала\n'
                f'{BB}(5){S} Если нет то он тебе наносят урон в размере: случайное число из интервала\n\n'
            )
            return None
        elif location == "game_2":
            print(
                f'\nПравила игры - "{RR}Обмани компьютер{S}"\n\n'
                f'{BB}(1){S} Ты выбираешь сложность от {Y}1{S} до {Y}бесконечности{S}\n'
                f'{BB}(2){S} Сложность это какой будет интервал угадывания: от 1 до сложность * 10\n'
                f'{BB}(3){S} Ты пишешь число в этом интервале и компьютер должен его угадать\n'
                f'{BB}(4){S} Если он не угадал ты получаешь: случайную награду из выбранно интервала // 10\n'
                f'{BB}(5){S} Если нет то он наносит тебе урон в размере: случайное число из интервала * 10\n\n'
            )
            return None


# Во всех боях (где юзер получает EXP) проверят не готов ли юзер к новому уровню
# А так же каждые 10 угадываний(побед) дает процентный бонус ко всему урону

def level_up():
    global user
    while True:
        user["user_heath"] =  user["user_heath_fact"] + user["user_heath_fact"] / 100 * user["baf_heath"]
        user["user_damage"] =  user["user_damage_fact"] + user["user_damage_fact"] / 100 * user["baf_damage"]
        sled_level = (user["lvl"] * 100) + (user["lvl"] * 50)
        if user["win_game_1"] >= 10:
            user["baf_damage"] += user["win_game_1"] // 10
            print(
                f'Ты получил + {RR}{user["win_game_1"] // 10}% к урону{S}!'
                )
            user["win_game_1"] //= 10
            user["user_damage"] =  user["user_damage_fact"] + user["user_damage_fact"] / 100 * user["baf_damage"]
        if user["win_game_2"] >= 10:
            user["baf_heath"] += user["win_game_2"] // 10
            print(
                f'Ты получил + {GG}{user["win_game_2"] // 10}% к здоровью!{S}!'
                )
            user["win_game_2"] //= 10
            user["user_heath"] =  user["user_heath_fact"] + user["user_heath_fact"] / 100 * user["baf_heath"]
        if user["exp"] >= sled_level:
            user["lvl"] += 1
            user["exp"] = 0
            user["user_heath_fact"] += user["lvl"]
            user["user_heath"] =  user["user_heath_fact"] + user["user_heath_fact"] / 100 * user["baf_heath"]
            print(
                f'\nПоздравляю! Ты получил {user["lvl"]} lvl!\n'
                f'Теперь у тебя {user["user_heath"]} здоровья.\n\n'
            )

            return None
        else:
            print(
                f'\nНужно еще {sled_level - user["exp"]} опыта!\n'
                f'До следующего {user["lvl"] + 1} уровня.\n\n'
            )
            return None


# Здесь юзер переходит на другие локации и всегда возращается сюда
# Можно посмотреть характеристики 


def taverna():
    global user
    while True:
        otvet = input(
            f'\n{Y}{user["name_user"]}{S}, приветствую тебя в таверне! - {R}"Чертово число!"{S}\n'
            f'Здесь ты всегда можешь отдохнуть и восстановить свое {G}здоровье!{S}\n'
            f'Что хочешь путник?\n\n'
            f'{BB}(1){S} Посражаться с числами.\n'
            f'{BB}(2){S} Посмотреть характеристики.\n'
            f'{BB}(3){S} Зайти в магазин.\n'
            f'{BB}(4){S} Зайти в банк.\n\n'
            f'Какой вариант выберешь?\n\n{Y}'
        )
        otvet = valid_otvet(otvet, 4)
        if otvet == 1:
            otvet = input(
                f'\n{Y}{user["name_user"]}{S}, могу предложить тебе несколько игр:\n\n'
                f'{BB}(1){S} Угадай и уменьши диапазон\n'
                f'{BB}(2){S} Попробуй обмануть компьютер :)\n'
                f'Какой вариант выберете?\n\n{Y}'
            )
            print(S)
            return valid_otvet(otvet, 2)              
        elif otvet == 2:
            if not user["user_wearon"]:
                print(
                    f'\nУ тебя {GG}{user["exp"]} опыта{S}. И у тебя {G}{user["lvl"]} lvl{S}.\n'
                    f'У тебя {YY}{user["gold"]} золота{S} и {YY}{user["gold_bank"]}{S} лежит на счету!\n'
                    f'Твой {RR}урон: {user["user_damage"]}{S}. Количество {MM}здоровья: {user["user_heath"]}{S}.\n\n'
                    f'Твой бафф на {RR}урон{S} составляет: {RR}{user["baf_damage"]}%{S}!\n'
                    f'Твой бафф на {MM}здоровье{S} составляет: {MM}{user["baf_heath"]}%{S}!\n\n'
                    f'Общее количество побед над Уки: '
                    f'{YY}{user["win_game_1"] + user["baf_damage"] // 10}{S}!\n'
                    f'Общее количество побед над Заг: '
                    f'{YY}{user["win_game_2"] + user["baf_heath"] // 10}{S}!\n\n'
                    f'Снаряжения у тебя нет! Иди трудись!\n\n'
                )
            else:
                print(
                   f'\nУ тебя {GG}{user["exp"]} опыта{S}. И у тебя {G}{user["lvl"]} lvl{S}.\n'
                    f'У тебя {YY}{user["gold"]} золота{S} и {YY}{user["gold_bank"]}{S} лежит на счету!\n'
                    f'Твой {RR}урон: {user["user_damage"]}{S}. Количество {MM}здоровья: {user["user_heath"]}{S}.\n\n'
                    f'Твой бафф на {RR}урон{S} составляет: {RR}{user["baf_damage"]}%{S}!\n'
                    f'Твой бафф на {MM}здоровье{S} составляет: {MM}{user["baf_heath"]}%{S}!\n\n'
                    f'Общее количество побед над Уки: '
                    f'{YY}{user["win_game_1"] + user["baf_damage"] // 10}{S}!\n'
                    f'Общее количество побед над Заг: '
                    f'{YY}{user["win_game_2"] + user["baf_heath"] // 10}{S}!\n\n'
                    f'Твое оружие это: {user["user_wearon"][0]} - {user["user_wearon"][1]} урона!\n\n'
                )
        elif otvet == 3:
            shop()
        elif otvet == 4:
            bank()


# Словари со всеми качествами и снаряжением 
# А так же списочное выражение которое выдает словарь с рандомным снаряжением и его качестом!

def quality(location, total=1):
    global all_quality, all_wearon
    all_quality = {
    "Обычный": 1,
    "Необычный": 1.2,
    "Редкий": 1.5,
    "Эпический": 2,
    "Легендарный": 3,
    "Мифический": 5,
    "Божественный": 8,
    "Космический": 12,
    "Астральный": 16,
    "Трансцендентный": 20,
}
    all_wearon = {
    "Деревянный меч": 1,
    "Каменный меч": 2,
    "Медный меч": 4,
    "Бронзовый меч": 5,
    "Железный меч": 8,
    "Стальной меч": 10,
    "Чугунный меч": 12,
    "Серебряный меч": 14,
    "Золотой меч": 16,
    "Титановый меч": 20,
    "Мифриловый меч": 25,
    "Адамантовый меч": 35,
    "Оркалиевый меч": 50,
    "Карбидный меч": 60,
    "Вольфрамовый меч": 70,
    "Платиновый меч": 80,
    "Рубиновый меч": 90,
    "Сапфировый меч": 100,
    "Алмазный меч": 120,
    "Неферитовый меч": 150,
    "Ониксовый меч": 170,
    "Эндер-меч": 180,
    "Драконий стальной меч": 200,
    "Вибранцевый меч": 210,
    "Уруковый меч": 250,
    "Хрустальный меч": 300,
    "Меч из звёздной пыли": 400,
    "Меч бога войны": 500,
    "Космический метеоритный меч": 700,
    "Меч из чистой энергии": 1000,
}   
    if location == "shop":
        wearon_random = sample(list(all_wearon),total)
        quality_random = sample(list(all_quality),total)
        wearon_shop = {}
        for i,j in zip(wearon_random, quality_random):
            wearon_shop[f"({j}) {i}"] = all_wearon[i] * all_quality[j]

        return wearon_shop
          

# Здесь юзер можеть потратить золото и купить себе снаряжение 
# Снаряжение пока что дает только урон
# Каждый раз при просмотре ассортимента он разный как и цена его

def shop():
    global user
    wearon_random = quality("shop", total=5)
    wearon_shop = {}
    while True:       
        otvet = input(
            f'\n{Y}{user["name_user"]}{S}! Приветствую тебя у себя в магазине!\n'
            f'Что ты хочешь посмотреть?\n\n'
            f'{BB}(1){S} Оружие\n' 
            f'{BB}(2){S} Артефакты\n'
            f'{BB}(3){S} Вернуться в таверну\n\n{Y}'
        )
        print()
        otvet = valid_otvet(otvet, 3)
        print(S)
        if otvet == 1:
            for i, j in zip(range(1, len(wearon_random) + 1), wearon_random.keys()):
                wearon_shop[i] = [wearon_random[j] * randint(50, 100), j, wearon_random[j]]
                print(
                    f'{BB}({i}){S} {j}: {RR}Урон - {int(wearon_random[j])}{S}'
                    f' Цена - {YY}{int(wearon_shop[i][0])} золота{Y}!'
                )
                if i == len(wearon_random):
                    print(S)
            else:
                otvet = input(
                    f'\nКакой хочешь купить?\n'
                    f'Или вернемся в таверну? - тогда напиши {G}"назад"{Y}!\n\n{Y}'
                )
                
                if otvet.isalpha() and otvet.lower() == "назад":
                    return None
                otvet = valid_otvet(otvet, len(wearon_shop))
                if wearon_shop[otvet][0] > user["gold"]:
                    print(
                        f'\nВначале заработай эти деньги, {R}умник{S}!\n'
                        f'У тебя всего {YY}{user["gold"]} золота{S}!\n\n'
                    )
                else:
                    if not user["user_wearon"]:
                        user["gold"] -= wearon_shop[otvet][0]
                        user["user_wearon"] = [wearon_shop[otvet][1],wearon_shop[otvet][2],wearon_shop[otvet][0]]
                        user["user_damage_fact"] += wearon_shop[otvet][1]
                        level_up()
                        print(
                            f'\nТы приобрел {Y}{wearon_shop[otvet][0]}{S}!\n'
                            f'У него {RR}{wearon_shop[otvet][1]} урона{S}!\n\n'
                        )
                    else:
                        user["gold"] += user["user_wearon"][2]
                        user["gold"] -= wearon_shop[otvet][0]
                        print(
                            f'\n{S}Свой старый меч ты продал за {Y}{user["user_wearon"][2]} золота!{S}\n'
                        )
                        user["user_damage_fact"] -= user["user_wearon"][1]
                        user["user_wearon"] = [wearon_shop[otvet][1],wearon_shop[otvet][2],wearon_shop[otvet][0]]
                        user["user_damage_fact"] += user["user_wearon"][1]
                        print(
                            f'\n{S}Ты приобрел {Y}{wearon_shop[otvet][0]}{S}!\n'
                            f'У него {RR}{wearon_shop[otvet][1]} урона{S}!\n\n'
                        )


        elif otvet == 2:
            pass
        elif otvet == 3:
            break
  

# Здесь юзер может положить и забрать деньги со счета
# На этом можно заработать а так же не потерять деньги при смерти

def bank():
    global user
    while True:

        # Приветствуем юзера и предлагаем выбрать вариант действий,записывая ответ в otvet
        print()
        otvet = input(
            f'{S}Приветствую вас в банке {GG}бесконечного города{S}!\n'
            f'Могу предложить вам несколько услуг:\n\n'
            f'{BB}(1){S} Положить деньги на счет.\n'
            f'{BB}(2){S} Забрать деньги со счета.\n'
            f'{BB}(3){S} Вернуться в таверну.\n\n'
            f'Что вам нужно?\n\n{Y}'            
        )
        otvet = valid_otvet(otvet, 3)
        print(S)
        if otvet == 1:
            if user["gold_bank"] > 0:
                end_vklad = time()
                itog_vklad = int(user["gold_bank"] / 10000  * (end_vklad - user["start_vklad"]))
                user["gold_bank"] += itog_vklad
                otvet = input(
                    f'\nНапиши сколько вы хотите положить на счет!\n'
                    f'Каждую секунду вам будет начисляться {YY}0.01%{S} от вашей суммы на счету!\n'
                    f'Сейчас у вас {YY}{user["gold"]} золота{S} на руках.\n\n{Y}{S}'    
                )
                if otvet.isdigit() and int(otvet) <= user["gold"]:
                    user["gold_bank"] += int(otvet)
                    user["gold"] -= int(otvet)
                    user["start_vklad"] = time()
                    print(
                        f'\nТеперь у вас на счету {YY}{user["gold_bank"]} золота{S}.\n'
                        f'\nА на руках у вас {YY}{user["gold"]} золота{S}.\n'
                        f'Мы всегда рады вашим денюжкам!\n\n'                      
                    )
                else:
                    if otvet.isdigit() and otvet == 0:
                        print(
                            f'\nХм,ну ноль так ноль, только если это что то {Y}изменит{S}...\n\n'                           
                        )
                    print(
                        f'\nПрошу вас,напишите столько сколько вы можете положить!\n\n'
                    )
            else:
                print(S)
                otvet = input(
                    f'\nНапиши сколько вы хотите положить на счет!\n'
                    f'Каждую секунду вам будет начисляться {YY}0.01%{S} от вашей суммы на счету!\n'
                    f'Сейчас у вас {YY}{user["gold"]} золота{S} на руках.\n\n{Y}'    
                )
                if otvet.isdigit() and int(otvet) <= user["gold"]:
                    user["gold_bank"] += int(otvet)
                    user["gold"] -= int(otvet)
                    user["start_vklad"] = time()
                    print(
                        f'\nТеперь у вас на счету {YY}{user["gold_bank"]} золота{S}.\n'
                        f'\nА на руках у вас {YY}{user["gold"]} золота{S}.\n'
                        f'Мы всегда рады вашим денюжкам!\n\n'                      
                    )
                else:
                    print(
                        f'\nПрошу вас,напишите столько сколько вы можете положить!\n\n'
                    )

        elif otvet == 2:
            if user["gold_bank"] > 0:
                end_vklad = time()
                itog_vklad = int(user["gold_bank"] / 10000 * (end_vklad - user["start_vklad"]))
                user["gold_bank"] += itog_vklad
                otvet = input(
                    f'\nНапиши сколько вы хотите снять со счета!\n'
                    f'Благодаря вашему вкладу вы заработали за это время {YY}{itog_vklad} золота!{S}\n'
                    f'Сейчас у вас лежит {YY}{user["gold_bank"]} золота{S}.\n\n{Y}'    
                )
                if otvet.isdigit() and int(otvet) <= user["gold_bank"]:
                    user["gold_bank"] -= int(otvet)
                    user["gold"] += int(otvet)
                    user["start_vklad"] = time()
                    print(
                        f'\nТеперь у вас на счету {YY}{user["gold_bank"]} золота{S}.\n'
                        f'\nА на руках у вас {YY}{user["gold"]} золота{S}.\n'
                        f'Мы будет ждать ваших следующих вложенний!\n\n'                      
                    )
            else:
                print(
                    f'\nУ вас сейчас на счету нету {YY}золота!{S}\n'
                    f'Сделайте вклад! И приходите.. \n\n'
                )
        elif otvet == 3:
            return None



# Первая игра в которой надо угадывать числа в выбранном промежутке
# Промежуток определяется сложностью 
# Чтобы поднять сложность надо победить босса

def game_1():
    global user
    while True:
        otvet = input(
            f'\nПредлагаю тебе выбрать сложность самому! Или вернуться в таверну написав - {G}"назад"{S}\n'
            f'Если хочешь посмотреть правила этой игры напиши - "{Y}правила{S}"\n\n'
            f'Какую сложность хочешь? Ты можешь выбрать от {M}1 до {user["hard_game_1"]}{S}\n'
            f'Чтобы повысить сложность сразись с {RR}Угадайкой ({user["hard_game_1"] + 1}lvl){S}\n'
            f'Написав - "{RR}босс{S}"!\n\n'
            f'Сложность это игра от {RR}1 до (10 * сложность){S}\n\n' 
            f'Просто напиши одно {G}число{S}:\n\n{Y}'
            )
        print(S)  
        if otvet.isalpha():
            if otvet.lower() == "назад":
                break
            elif otvet.lower() == "правила":
                pravila("game_2")
            elif otvet.lower() == "босс":
                heath_fight = user["user_heath"]
                total_win = 0
                print(
                    f'\nКакой смелый! Тогда попробуй угадать {Y}5 раз{S} в интервале\n'
                    f'От 1 до {(user["hard_game_1"] + 1) * 10} и остаться в {RR}живых{S}!\n\n'                    
                )
                while True:
                    complexity = (user["hard_game_1"] + 1) * 10
                    prav = randint(1, complexity)
                    otvet = input(
                            f"\nВведи число от {R}{1} и до {complexity}{S}\n"
                            f'Или вернись в таверну написав - {G}"назад"{S}{Y}\n\n'
                        )
                    if otvet.isdigit():
                        if total_win == 5:
                            user["hard_game_1"] += 1
                            print(
                                f'\nПоздравляю ты победил {RR}Угадайку {user["hard_game_1"] + 1} lvl{S}!\n'
                                f'Теперь ты можешь пользоваться {R}сложностью {user["hard_game_1"] + 1}{S}!\n\n'
                            )
                            break
                        if user["user_damage"] >= 1:
                            polovina_damage_1, polovina_damage_2 = user["user_damage"] / 2, user["user_damage"] / 2
                            polovina_damage_2 = int(polovina_damage_2 + float("0" + str(polovina_damage_1)[1:]))
                            polovina_damage_1 = int(polovina_damage_1)
                            otvet = [i for i in range(int(otvet) - polovina_damage_1, int(otvet) + polovina_damage_2 + 1)]
                        else:
                            otvet = [int(otvet)]    
                        if prav in otvet:
                            total_win += 1
                            print(
                                f'\nПоздравляю, ты {GG}угадал{S}!\n'
                                f'Было число {prav} в твоей области: от {min(otvet)} до {max(otvet)}\n\n'
                                f'Тебе осталось угадать {Y}{5 - total_win}{S} раз и ты убьешь его!\n\n'
                            )
                        else:
                            lose = randint(1, complexity)
                            
                            # Проверяем не погиб ли юзер, если нет просто вычитаем его здоровье.
                            user_los = int(user["gold"] / 100 * 33)
                            user["gold"] = int(user["gold"] / 100 * 67)
                            
                            if heath_fight - lose <= 0:               
                                print(
                                    f'\nТы погиб от удара {R}Угадайки ({complexity // 10} lvl){S}!..\n'
                                    f'Возращайся в таверну и отдавай за возраждение:\n\n'
                                    f'{RR}{user_los} золота{S}!\n\n'
                                    f'У тебя осталось {YY}{user["gold"]} золота{S}.\n\n'
                                )
                                return None
                            else:

                                #  Пишем юзеру о том сколько у него осталось здоровья

                                heath_fight -= lose
                                print(
                                    f'\n{RR}Неправильно{S}! - Попробуй еще раз!\n'
                                    f'Верное число {prav} не попало в твою область: от {min(otvet)} до {max(otvet)}!\n\n'
                                    f'Тебе нанесли {RR}{lose} урона!{S}\n'
                                    f'Осталось {MM}{heath_fight} здоровья!{S}\n\n'
                                )   
                    else:
                        if otvet.isalpha() and otvet == "назад":
                            return None
                        else:
                            print(
                                f'Просто введи число от {YY}1 до {complexity}{S}'
                                f'Или напиши вернись в таверну написав - "{YY}назад{S}"'
                            )                                           
        elif not otvet.isdigit():
            print(
                f'Просто введи одно число! Начиная с {R}1! до {user["hard_game_1"]}{S}\n\n'
            )
        else:
            if int(otvet) <= user["hard_game_1"]:
                complexity = int(otvet) * 10
                print(f'\nХорошо начнем!\n\n')
                heath_fight = user["user_heath"]  
                while True:
                    prav = randint(1, complexity)
                    otvet = input(
                            f"\nВведи число от {R}{1} и до {complexity}{S}\n"
                            f'Или вернись в таверну написав - {G}"назад"{S}{Y}\n\n'
                        )
                    if otvet.isdigit():                       
                        if user["user_damage"] >= 1:
                            polovina_damage_1, polovina_damage_2 = user["user_damage"] / 2, user["user_damage"] / 2
                            polovina_damage_2 = int(polovina_damage_2 + float("0" + str(polovina_damage_1)[1:]))
                            polovina_damage_1 = int(polovina_damage_1)
                            otvet = [i for i in range(int(otvet) - polovina_damage_1, int(otvet) + polovina_damage_2 + 1)]
                        else:
                            otvet = [int(otvet)]    
                        if prav in otvet:
                            win1, win2 = randint(1, complexity), randint(1, complexity)
                            user["exp"] += win1
                            user["gold"] += win2
                            user["win_game_1"] += 1
                            print(
                                f'\nПоздравляю, ты {GG}угадал{S}!\n'
                                f'Было число {prav} в твоей области: от {min(otvet)} до {max(otvet)}\n\n'
                                f'Ты получил {GG}{win1} EXP{S}! И {YY}{win2} GOLD{S}!\n\n'
                                f'Теперь у тебя {GG}{user["exp"]} EXP{S}.\nИ {YY}{user["gold"]} GOLD{S}.\n\n'
                            )
                            level_up()
                        else:
                            lose = randint(1, complexity)
                            
                            # Проверяем не погиб ли юзер, если нет просто вычитаем его здоровье.

                            if heath_fight - lose <= 0:               
                                user_los = int(user["gold"] / 100 * 33)
                                user["gold"] = int(user["gold"] / 100 * 67)
                                print(
                                    f'\nТы погиб от удара {R}Уки ({complexity // 10} lvl){S}!..\n'
                                    f'Возращайся в таверну и отдавай за возраждение:\n\n'
                                    f'{RR}{user_los} золота{S}!\n\n'
                                    f'У тебя осталось {YY}{user["gold"]} золота{S}.\n\n'
                                )
                                return None
                            else:

                                #  Пишем юзеру о том сколько у него осталось здоровья

                                heath_fight -= lose
                                print(
                                    f'\n{RR}Неправильно{S}! - Попробуй еще раз!\n'
                                    f'Верное число {prav} не попало в твою область: от {min(otvet)} до {max(otvet)}!\n\n'
                                    f'Тебе нанесли {RR}{lose} урона!{S}\n'
                                    f'Осталось {MM}{heath_fight} здоровья!{S}\n\n'
                                )                                              
                    else:
                        if otvet.lower() == "назад":
                            return None
                        elif otvet.lower() == "правила":
                            pravila("game_1")
                        else:
                            print(
                                f'\nВведи число или вернись в таверну написав - {G}"назад"{S}!\n\n'
                            )
            else:
                print(
                    f'\nВведи доступную тебе сложность!\n'
                    f'Или победи {RR}босса{S}!\n\n'
                )


# Вторая игра в которой уже компьютер должен угадывать числа в выбранном промежутке
# Промежуток определяется сложностью 
# Чтобы поднять сложность надо победить босса

def game_2():
    while True:
        otvet = input(
            f'\nПредлагаю тебе выбрать сложность самому! Или вернуться в таверну написав - {G}"назад"{S}\n'
            f'Какую сложность хочешь? ты можешь выбрать от {M}1 до {user["hard_game_2"]}{S}\n'
            f'Если хочешь посмотреть {Y}правила{S} этой игры напиши - "{Y}правила{S}"\n\n'
            f'Чтобы повысить сложность сразись с боссом {RR}Загадайкой ({user["hard_game_2"] + 1}lvl){S}\n'
            f'Написав - "{RR}босс{S}"!\n\n'
            f'Сложность это игра от {RR}1 до (10 * сложность){S}\n\n' 
            f'Просто напиши одно {G}число{S}:\n\n{Y}'
            )
        print(S)
        if otvet.isalpha():
            if otvet.lower() == "назад":
                break
            elif otvet.lower() == "правила":
                pravila("game_2")
            elif otvet.lower() == "босс":
                heath_fight = user["user_heath"]
                heath_boss = user["hard_game_2"] * 100
                complexity_boss = (user["hard_game_2"] + 1) * 10
                print(
                    f'\nКакой смелый! Тогда попробуй победить босса {RR}Загадайка ({user["hard_game_2"] + 1}lvl)!\n'
                    f'У которого {MM}{heath_boss} здоровья!{S}\n'
                    f'Он будет угадывать сразу {RR}{user["hard_game_2"] + 1} числами{S}!\n\n'                    
                )
                while True:
                    prav = []
                    for i in range(complexity_boss // 10):
                        prav.append(randint(1, complexity_boss))
                    otvet = input(
                            f"\nЗагадай число от {R}{1} и до {complexity_boss}{S}\n"
                            f'Или вернись в таверну написав - {G}"назад"{S}\n\n{Y}'
                        )
                    if otvet.isdigit() and 1 <= int(otvet) <= complexity_boss:
                        otvet = int(otvet)

                        if not otvet in prav:
                            if heath_boss - user["user_damage"] > 0:
                                heath_boss -= user["user_damage"]
                                print(
                                    f'\n{R}Загадайка({user["hard_game_2"] + 1}lvl){S} не угадал твое число!\n'
                                    f'Он сказал {len(prav)} чисел и не попал!\n'
                                    f'Ты нанес ему {RR}{user["user_damage"]} урона{S}!\n'
                                    f'У него осталось {M}{heath_boss} здоровья{S}\n\n'
                                )
                            elif heath_boss - user["user_damage"] <= 0:
                                user["hard_game_2"] += 1
                                print(
                                    f'\nПоздравляю ты победил {RR}Загадайку {user["hard_game_2"]} lvl{S}!\n'
                                    f'Теперь ты можешь пользоваться {R}сложностью {user["hard_game_2"]}{S}!\n\n'
                                )
                                break      
                        else:
                            lose = randint(1, complexity_boss)
                            
                            # Проверяем не погиб ли юзер, если нет просто вычитаем его здоровье.                           
                            
                            if heath_fight - lose <= 0:
                                user_los = int(user["gold"] / 100 * 67)
                                user["gold"] = int(user["gold"] / 100 * 67)                                      
                                print(
                                    f'\nТы погиб от удара {R}Загадайки({complexity_boss // 10} lvl){S}!..\n'
                                    f'Возращайся в таверну и отдавай за возраждение:\n\n'
                                    f'{RR}{user_los} золота{S}!\n\n'
                                    f'У тебя осталось {YY}{user["gold"]} золота{S}.\n\n'
                                )
                                return None
                            else:
                                #  Пишем юзеру о том сколько у него осталось здоровья

                                heath_fight -= lose
                                print(
                                    f'\n{RR}Загадайка{complexity_boss}lvl{S} написал {len(prav)} чисел!\n'
                                    f'И угадал твое число!\n'
                                    f'Тебе нанесли {RR}{lose} урона!{S}\n'
                                    f'Осталось {MM}{heath_fight} здоровья!{S}\n\n'
                                )
                    else:
                        if otvet == 'назад':
                            return None
                        else:
                            print(
                                f'\nЗагадай {GG}число{S} в диапозоне: от {YY}1 до {complexity_boss}{S}!\n\n'
                            )

        elif not otvet.isdigit():
            print("\nПросто введи одно число! Начиная с {R}1!{S}\n\n")
        else:
            if int(otvet) <= user["hard_game_2"]:
                complexity_mob = int(otvet) * 10
                print(f'\nХорошо начнем!\n\n')
                heath_fight = user["user_heath"]  
                heath_mob = complexity_mob
                while True:
                    prav = []
                    for i in range(complexity_mob // 10):
                        prav.append(randint(1, complexity_mob))
                    otvet = input(
                            f"\nЗагадай число от {R}{1} и до {complexity_mob}{S}\n"
                            f'Или вернись в таверну написав - {G}"назад"{S}{Y}\n\n'
                        )
                    if otvet.isdigit() and 1 <= int(otvet) <= complexity_mob:                       
                        if not otvet in prav:
                            if heath_mob - user["user_damage"] > 0:
                                heath_mob -= user["user_damage"]
                                print(
                                    f'\n{G}Поздравляю{S}, {R}Заг({user["hard_game_2"]}lvl){S} не угадал твое число!\n'
                                    f'Он сказал {Y}{len(prav)} чисел{S} и не попал!\n\n'
                                    f'Ты нанес ему {RR}{user["user_damage"]} урона{S}!\n'
                                    f'У него осталось {M}{heath_mob} здоровья{S}\n\n'
                                )
                            else:
                                win1, win2 = randint(1, complexity_mob) // 10, randint(1, complexity_mob) // 10
                                user["exp"] += win1
                                user["gold"] += win2
                                user["win_game_2"] += 1
                                heath_mob = complexity_mob
                                print(
                                    f'\n{G}Поздравляю{S}, {R}Заг({user["hard_game_2"]}lvl){S} погиб!\n'
                                    f'Ты получил {GG}{win1} EXP{S}! И {YY}{win2} GOLD{S}!\n\n'
                                    f'Теперь у тебя {GG}{user["exp"]} EXP{S}.\n'
                                    f'И {YY}{user["gold"]} GOLD{S}.\n\n'
                                )
                            level_up()    
                        else:
                            lose = randint(1, complexity_mob)

                            # Проверяем не погиб ли юзер, если нет просто вычитаем его здоровье.

                            if heath_fight - lose <= 0:               
                                user_los = int(user["gold"] / 100 * 67)
                                user["gold"] = int(user["gold"] / 100 * 67)
                                print(
                                    f'\nТы погиб от удара {R}Заг ({complexity_mob // 10} lvl){S}!..\n'
                                    f'Возращайся в таверну и отдавай за возраждение:\n\n'
                                    f'{RR}{user_los} золота{S}!\n\n'
                                    f'У тебя осталось {YY}{user["gold"]} золота{S}.\n\n'
                                )
                                return None
                            else:

                                #  Пишем юзеру о том сколько у него осталось здоровья

                                heath_fight -= lose
                                print(
                                    f'\n{RR}Угадайка{user["hard_game_2"]}lvl{S} написала {len(prav)} чисел!\n'
                                    f'И {RR}узнала{S} твое число! - {prav}\n'
                                    f'Тебе нанесли {RR}{lose} урона!{S}\n'
                                    f'Осталось {MM}{heath_fight} здоровья!{S}\n\n'
                                )                           
                    else:
                        print(S)
                        if otvet.lower() == "назад":
                            return None
                        else:
                            print(
                                f'\nВведи число в диапозоне: от {YY}1 до {complexity_mob}{S}\n' 
                                f'Или вернись в таверну написав - {G}"назад"{S}!\n\n'
                            )
            else:
                print(
                    f'\nВведи доступную тебе сложность!\n'
                    f'Или победи {RR}босса{S}!\n\n'
                )


# Основная функция которая управляет всем игровым процессом 

def game():
    player_stats()
    valid_name()
    level_up()
    while True:
        x = taverna()
        if x == 1:
            game_1()
        elif x == 2:
            game_2()
 
                
game()