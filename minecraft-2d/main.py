from ursina import *
from ursina.audio import *
from controller import *
app=Ursina()
grass=[(0,0),(1,1),(2,-1),(3,2),(4,-2),(4,3),(5,3),(6,2)]
dirt=[(0,-1),(0,-2),(1,0),(1,-1),(1,-2),(2,-2),(3,-2),(6,0),(6,1),(4,2)]
stone=[(4,1),(5,-2),(5,2),(6,-2),(6,-1)]
coal=[(5,1)]
textures=['grass','dirt','stone','coal']
entities=[]
music=Audio('audio.mp3', loop=True, autoplay=True)#my song
coin=Entity(model="quad",texture="coin",x=20,y=10)
sky=Entity(model="quad",texture="sky minecraft",scale=(100,100,0),z=0.5)
for pos in grass:
    entity=Entity(model="quad",texture="grass",position=pos,collider='box')
    entities.append(entity)
for pos in dirt:
    entity2=Entity(model="quad",texture="dirt",position=pos,collider='box')
    entities.append(entity2)
for pos in stone:
    entity3=Entity(model="quad", texture="stone", position=pos,collider='box')
    entities.append(entity3)
for pos in coal:
    entity4=Entity(model="quad",texture="coal",position=pos,collider='box')
    entities.append(entity4)
#steve=Entity(model="quad",texture="skin",scale=(1,2,0))
#steve.y=1
player = PlatformerController2d(scale_y=2, scale_x=1, color=color.white, jump_height=1, texture='finished!',x=0,y=5, scale_z=0.0001)
camera.add_script(SmoothFollow(target=player, offset=[0, 1, -30], speed=4))
ori=1
def input(key):
    global ori
    try:
        ori=int(key)
    except:pass
    if key=="right arrow":
        for entity_ in entities:
            try:
                if entity_.position == Vec3(floor(player.x),floor(player.y),0)+(1,1,0):
                    destroy(entity_)
                    entities.remove(entity_)
            except:
                pass
    if key=="left arrow":
        for entity_ in entities:
            try:
                if entity_.position == Vec3(floor(player.x), floor(player.y), 0) + (0, 1, 0):
                    destroy(entity_)
                    entities.remove(entity_)
            except:
                pass
    if key == "up arrow":
        for entity_ in entities:
            try:
                if entity_.position == Vec3(round(player.x), round(player.y), 0) + (0, 3, 0):
                    destroy(entity_)
                    entities.remove(entity_)
            except:
                pass
    if key == "down arrow":
        for entity_ in entities:
            try:
                if entity_.position == Vec3(round(player.x), floor(player.y), 0):
                    destroy(entity_)
                    entities.remove(entity_)
            except:
                pass

    if key=="shift" and ori!=0 and ori!=5 and ori!=6 and ori!=7 and ori!=8 and ori!=9:
        ok=True
        for entity_ in entities:
            if entity_.position == Vec3(round(player.x),floor(player.y),0):
                ok=False
        if ok==True:
            entity = Entity(model="quad", texture=textures[ori-1], position=Vec3(round(player.x),floor(player.y),0), collider='box')
            entities.append(entity)

k=True
def update():
    global coin,k,music
    if player.y < -50:
        player.y = 50
        player.x = 0
        ok = True
        for entity_ in entities:
            if entity_.position == Vec3(round(player.x), 0, 0):
                ok = False
        if ok == True:
            entity = Entity(model="quad", texture=textures[ori - 1], position=Vec3(round(player.x), 0, 0),
                            collider='box')
            entities.append(entity)
    if distance(player,coin)<=0.5 and k==True:
        coin.texture="benx"
        music.stop()
        music.clip="skipidi_dop.mp3"
        music.play()
        k=False
app.run()