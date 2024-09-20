import random
def play_cuefa():
        print('Незнаешь что скрывает твой друг?')


        name = input('А я знаю, напиши имя своего друга которого подозреваешь:')
        fake_news = [
                f" {name. title()} дрался в школе",
                f" {name. title( )} воровал конфенты в магазине",
                f" {name. title( )} бегал по цветам",
                f" {name. title( )} Кидался песком",
                f" {name. title()} взрывал педарды",
                f" {name. title()} был гангстером",
                ]
        gg = random.choice(fake_news)
        print(gg)
