from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True
#sense.show_message("WELCOME! Entrez votre code de déverrouillage.", text_colour=[255, 255, 255],scroll_speed=0.1,back_colour=[0, 0, 0])
#sense.show_message("Vous avez 4 options. Appuiez pour valider votre choix. ",text_colour=[255, 255, 255],scroll_speed=0.1,back_colour=[0, 0, 0])


yellow = (255, 255, 0)
white = (255,255,255)
nothing = (0,0,0)
blue= (0,0,255)
red= (255,0,0)

def display(affichage):   #Affichage des nombres et lettres
    sense.set_pixels(affichage)
    return 
    

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
    O, O, O, W, W, W, W, O,
    O, O, W, O, O, O, W, O,
    O, O, W, O, O, W, O, O,
    O, O, O, O, W, O, O, O,
    O, O, O, W, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    W, W, W, W, W, W, W, O,
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
    
    

    
    
a="Nouveau message."
b="Boite de messages."
c="Ecrire nouveau message."
d="Eteindre."

messages=[a,b,c,d]
images = [Number1,Number2,Number3,Number4]
count = 0



def displayMenu(count):
  while count <= 4:
    for event in sense.stick.get_events():
      while event.action == "pressed":
        if event.direction == "right":
          if count > 4:
            count = 0
          count+=1
          sense.set_pixels(images[count % len(images)]())
          time.sleep(0.9)
          sense.show_message(messages[count])
        elif event.direction == "left":
          if count < 0:
            count = 0
          count-=1
          sense.set_pixels(images[count % len(images)]())
          time.sleep(0.9)
          sense.show_message(messages[count])
        else:
          count=0
displayMenu(count)


