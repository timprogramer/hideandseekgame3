import wrap,random
random=random.randint(200, 500)
#a=random.randint(200, 500)
wrap.world.create_world(600,600,350,100)
wrap.world.set_back_color(212,219,244)

#клад и марио
wrap.sprite.add("mario-2-big",50,50,"walk3")
wrap.sprite.add("mario-items", random, random, "vine1", False)
wrap.actions.set_angle_to_point(0, random, random)

#помощ
mathx= random - 50
mathy= random - 50
wrap.sprite.add_text("до клада по x "+str(mathx)+"пикселей",100,50,"Arial")
wrap.sprite.add_text("до клада по y "+str(mathy)+"пикселей",100,80,"Arial")


#перемещение
mariox=input("введите сюда число по x")
marioy=input("введите сюда число по y")
mariox=int(mariox)
marioy=int(marioy)
wrap.actions.move_to(0,mariox,marioy)

#1попытка
sostykovka=wrap.sprite.is_collide_sprite(0,1)
print(sostykovka)
#wrap.sprite.show(1)