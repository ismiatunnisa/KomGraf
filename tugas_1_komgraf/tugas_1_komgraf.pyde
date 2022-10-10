mov = 1


def setup():
    size(500, 500)
    background(95, 73, 0, 0)
    
def draw ():
    global mov
    mov = mov +1
    if mov >= 2600:
        mov = 1
    #langit
    fill(100 + mov/6, 180 - mov/7, 210 - mov/6)
    rect(0, 0, 500, 250)
    
    #malam
    fill(0, 0, 0, mov/5-100)
    rect(0, 0, 500, 500)

    #bulan
    fill(255,255,255,-50+mov/6) 
    ellipse (150,60, 60, 60)
    fill(100 + mov/6, 180 - mov/7, 210 - mov/6) 
    ellipse (170,60, 60, 50)
    fill(0, 0, 0,mov/5-100)
    ellipse (170,60, 60.6, 50.6)
    
    #matahari
    noStroke()
    fill(255, 255 - mov/8, 0)
    ellipse (250,60 + mov/5, 120, 120)

    laut()
    Kapal1()
    Kapal()
    Awan()
    bintang()
    
def laut():
    fill(0, 65, 130)
    rect(0, 250, 500, 5)
    
    fill(0, 50, 100)
    rect(0, 255, 500, 10)
    
    fill(0, 40, 80)
    rect(0, 265, 500, 20)
    
    fill(0, 30, 60)
    rect(0, 285, 500, 35)
    
    fill(0, 22, 45)
    rect(0, 320, 500, 70)
    
    fill(0, 15, 30)
    rect(0, 390, 500, 110)
    
def Kapal():
    fill(255)
    triangle(30+ mov/4, 241 +70, 50+ mov/4 , 240+70, 28+ mov/4, 205+70)
    triangle(27 + mov/4, 241+70, 10+ mov/4+ mouseX/40, 242- mouseX/400+70, 25+ mov/4, 210+70)
    fill(120, 90, 70)
    quad (4+ mov/4, 250+70, 50+ mov/4, 250+70, 58+ mov/4, 242+70, 0+ mov/4, 245+70)
    # reflection kapal
    fill(120, 90, 70, 60)
    quad (4+ mov/4, 250+70, 50+ mov/4, 250+70, 58+ mov/4, 258+70, + mov/4, 255+70)
    fill(255, 50)
    triangle (30+ mov/4, 259+70, 50+ mov/4, 260+70, 28+ mov/4, 295+70)
    triangle (27 + mov/4, 259+70, 10+ mov/4+ mouseX/40, 258 + mouseX/400+70, 25+ mov/4, 290+70)
    
def Kapal1():
    # strokeWeight(5)
    noStroke()

# atas kapal 1
    fill(230, 212, 204)
    quad (8+ mov/6, 221, 32+ mov/6, 220, 30+ mov/6, 190, 6+ mov/6, 192)   
    
    fill(173, 169, 169)
    quad (49+ mov/6, 221, 89+ mov/6, 220, 88+ mov/6, 198, 48+ mov/6, 200)
    
    fill(251, 223, 208)
    quad (30+ mov/6, 221, 68+ mov/6, 220, 66+ mov/6, 183, 28+ mov/6, 185)
    
    fill(197, 78, 13)
    quad (8+ mov/6, 250, 80+ mov/6, 250, 100+ mov/6, 220, 0+ mov/6, 222)

# bawah kapal 2
    noStroke()

    fill(150, 78, 13, 50)
    quad (8+ mov/6, 250, 80+ mov/6, 250, 100+ mov/6, 280, + mov/6, 278)
    
    fill(105, 104, 104, 50)
    quad (69+ mov/6, 278, 89+ mov/6, 279, 88+ mov/6, 302, 67+ mov/6, 300)
    
    fill(180, 180, 180, 50)
    quad (8+ mov/6, 278, 32+ mov/6, 279, 30+ mov/6, 310, 6+ mov/6, 308)
    
    fill(200, 200, 200, 20)
    quad (30+ mov/6, 278, 68+ mov/6, 279, 66+ mov/6, 315, 28+ mov/6, 313)

def Awan ():
    fill(255-mov/11)
    ellipse (340+125-mov/10, 100, 40, 40)    
    ellipse (450+125-mov/10, 90, 60, 60)    
    ellipse (390+125-mov/10, 80, 80, 80)    
    rect (340+125-mov/10, 100, 110, 20)
    ellipse (110+125-mov/10, 110, 80, 80)
    ellipse (50+125-mov/10, 120, 60, 60)
    ellipse (160+125-mov/10, 130, 40, 40)    
    rect(46+125-mov/10, 130, 110, 20)
    
def bintang():
    pass
