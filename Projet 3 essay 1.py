from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True
#sense.show_message("WELCOME!   Entrez votre code de deverrouillage.", text_colour=[255, 255, 255],scroll_speed=0.1,back_colour=[0, 0, 0])
#time.sleep(0.9)
#sense.show_message("Vous avez 4 options. Appuiez pour valider votre choix. ",text_colour=[255, 255, 255],scroll_speed=0.1,back_colour=[0, 0, 0])


yellow = (255, 255, 0)
white = (255,255,255)
nothing = (0,0,0)
blue= (0,0,255)
red= (255,0,0)

 
    

def Number1():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, W, O, W, O, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, W, W, W, O, O,
    ]
    
    return logo
    
    
def Number2():
    W = white
    O = nothing
    logo = [
    O, O, W, W, W, W, W, O,
    O, W, O, O, O, O, W, O,
    O, O, W, O, O, W, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, W, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    ]
    
    return logo
    
    
def Number3 ():
    W = white
    O = nothing
    logo = [
    O, O, W, W, W, W, W, O,
    O, O, O, O, O, W, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, W, O, O, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, O, W, O, O,
    O, O, O, O, O, O, W, O,
    O, O, W, W, W, W, W, O,
    ]
    
    return logo
    
    
def Number4 ():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, W, O, W, O, O, O,
    O, W, O, O, W, O, O, O,
    W, W, W, W, W, W, W, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, W, O, O, O,
    ]
    
    return logo
    
   

message="Je m'appelle Hirwa-Mihigo Olyvia Abigail Raissa Heri"
delete="ou    2.supprimer"
keep="1.sauvergarder"
    
    
a="Nouveau message."
b="Boite à messagerie."
c="Ecrire nouveau message."
d="Eteindre."

messages=[a,b,c,d]
images = [Number1,Number2,Number3,Number4]
count = 0

while True:
  
  for event in sense.stick.get_events():
    if event.action == "pressed" : #and event.action == "released":
      if event.direction == "right":
        count+=1
        sense.set_pixels(images[count % len(images)]())
      elif event.direction == "middle":
        sense.show_message(messages[count])
        if count==0:
          sense.show_message("Vous avez un nouveau message  :",text_colour=[255, 255, 255],scroll_speed=0.1,back_colour=[0, 0, 0])
          time.sleep(1)
          sense.show_message(message,text_colour=[255, 255, 255],scroll_speed=0.1,back_colour=[0, 0, 0])
          time.sleep(1)
          sense.show_message(keep,text_colour=[255, 255, 255],scroll_speed=0.1,back_colour=[0, 0, 0])
          sense.show_message(delete,text_colour=[255, 255, 255],scroll_speed=0.1,back_colour=[0, 0, 0])
          
          
      if event.direction == "left":
        count-=1
        sense.set_pixels(images[count % len(images)]())
      if event.direction == "middle":
          sense.show_message(messages[count])
             