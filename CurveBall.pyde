'''Collision Exploration
See if we can collide with a curved surface
July 8, 2017'''

ball_list = []

grav = PVector(0,5)

def f(x):
    #return -0.001*(x-300)**2 + 550
    return 400+120.0*(sin(x/50.0)+cos(x/40.0))

def deriv(f,x):
    '''returns the derivative of f at x'''
    run = 1/1000.0
    rise = f(x+run) - f(x)
    return rise/run

point_list = [[x,f(x)] for x in range(600)]

class Particle:
    def __init__(self,x = random(600),y = random(100)):
        self.pos = PVector(x,y)
        #self.pos = PVector(400,50)
        self.vel = PVector(0,0)#random(-10,10),
                           #random(3))
        self.col = color(random(255),
                         random(255),
                         random(255))
        self.sz = 10
    
    def update(self):
        #update velocity by gravity
        self.vel += grav
        #decay the velocity
        self.vel.mult(0.99)
        #update position by velocity
        self.pos += self.vel
        #check for bounce
        self.bounce()
        noStroke()
        fill(self.col)
        ellipse(self.pos.x,self.pos.y,
                self.sz*2, self.sz*2)
        
    def bounce(self):
        if self.pos.y > f(self.pos.x) - self.sz:
            self.pos.y = f(self.pos.x) - self.sz
            #use the derivative to find the slope on the curve
            slope = deriv(f,self.pos.x)
            #convert the slope to an angle
            angle = atan(slope)
            #println(degrees(angle))
            #find the particle's angle of incidence
            self.particle_angle = self.vel.heading()
            #println(self.pos.x)
            #println(slope)
            self.vel.rotate(-2*(self.particle_angle-angle))
            self.vel.mult(0.80)

def setup():
    global ball
    size(600,600)
    for i in range(10):
        ball_list.append(Particle())
    
    
def draw():
    global ball
    background(0)
    
    #draw the curve
    strokeWeight(2)
    stroke(0,255,0) #green
    for i,point in enumerate(point_list):
        if i < len(point_list) - 1:
            line(point[0],point[1],
                 point_list[i+1][0],
                 point_list[i+1][1])
    for ball in ball_list:
        ball.update()
            
def mousePressed():
    ball_list.append(Particle(mouseX,mouseY))