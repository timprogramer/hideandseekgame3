import wrap,random
random=random.randint(200,500)
wrap.world.create_world(600,600,350,100)
wrap.world.set_back_color(212,219,244)

#клад и марио
wrap.sprite.add("mario-2-big",50,50,"walk3")
wrap.sprite.add("mario-items",random,random,"vine1",False)
wrap.actions.set_angle_to_point(0,random,random)

#помощ
mathx=random-50
mathy=random-50
print(mathx)
print(mathy)
