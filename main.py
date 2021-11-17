import math

import wrap,random
randomx=random.randint(200, 500)
randomy=random.randint(200, 500)
wrap.world.create_world(600,600,350,100)
wrap.world.set_back_color(212,219,244)

#клад и марио
marioplayer=wrap.sprite.add("mario-2-big",50,50,"walk3")
klad=wrap.sprite.add("mario-items", randomx, randomy, "vine1", False)
wrap.actions.set_angle_to_point(0, randomx, randomy)

#помощ
mathx= randomx-50
mathy= randomy-50
rastoyanie=math.sqrt(mathx**2+mathy**2)
rastoyanie=int(rastoyanie)
wrap.sprite.add_text("до клада "+str(rastoyanie)+"пикселей",200,80,"Arial")



#перемещение
mariox=input("введите сюда число по x")
marioy=input("введите сюда число по y")
mariox=int(mariox)
marioy=int(marioy)
wrap.actions.move_to(0,mariox,marioy)
wrap.actions.set_angle_to_point(0, randomx, randomy)

#1попытка
sostykovka=wrap.sprite.is_collide_sprite(0,1)

#попытка 2
if sostykovka==False:
    mariox=wrap.sprite.get_x(0)
    marioy=wrap.sprite.get_y(0)
    mathx = randomx - mariox
    mathy = randomy - marioy
    rastoyanie = math.sqrt(mathx ** 2 + mathy ** 2)
    rastoyanie=int(rastoyanie)
    wrap.sprite.add_text("до клада  " + str(rastoyanie) + "пикселей", mariox+100,marioy, "Arial")
    mariox = input("введите сюда число по x")
    marioy = input("введите сюда число по y")
    mariox = int(mariox)
    marioy = int(marioy)
    wrap.actions.move_to(0, mariox, marioy)
    wrap.actions.set_angle_to_point(0, randomx, randomy)
    sostykovka = wrap.sprite.is_collide_sprite(0, 1)
    if sostykovka == False:
        mariox = wrap.sprite.get_x(0)
        marioy = wrap.sprite.get_y(0)
        mathx = randomx - mariox
        mathy = randomy - marioy
        rastoyanie = math.sqrt(mathx ** 2 + mathy ** 2)
        rastoyanie = int(rastoyanie)
        wrap.sprite.add_text("до клада  " + str(rastoyanie) + "пикселей", mariox + 100, marioy, "Arial")
        mariox = input("введите сюда число по x")
        marioy = input("введите сюда число по y")
        mariox = int(mariox)
        marioy = int(marioy)
        wrap.actions.move_to(0, mariox, marioy)
        wrap.actions.set_angle_to_point(0, randomx, randomy)
        sostykovka = wrap.sprite.is_collide_sprite(0, 1)
        if sostykovka == False:
            mariox = wrap.sprite.get_x(0)
            marioy = wrap.sprite.get_y(0)
            mathx = randomx - mariox
            mathy = randomy - marioy
            rastoyanie = math.sqrt(mathx ** 2 + mathy ** 2)
            rastoyanie = int(rastoyanie)
            wrap.sprite.add_text("до клада  " + str(rastoyanie) + "пикселей", mariox + 100, marioy, "Arial")
            mariox = input("введите сюда число по x")
            marioy = input("введите сюда число по y")
            mariox = int(mariox)
            marioy = int(marioy)
            wrap.actions.move_to(0, mariox, marioy)
            wrap.actions.set_angle_to_point(0, randomx, randomy)
            sostykovka = wrap.sprite.is_collide_sprite(0, 1)
            wrap.sprite.show(1)
