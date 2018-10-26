def setup():
    size(640,480) #size
def draw():
    background(36,30,71) #background
    noStroke()
   
    fill(220,204,234)
    ellipse(600,60,300,300) #moon
    
    #ground
    fill(75, 63, 31)
    ellipse(400, 480,980,300) 
    
    #house 1
    fill(50)
    rect(350, 250, 150, 150)
    triangle(350,250,500,250,425,100)
    fill(225,225,0)
    rect(365,250,50,50)
    rect(435,250,50,50)
    fill(0)
    rect(387.5,250,5,50)
    rect(457.5,250,5,50)
    rect(365,272.5,50,5)
    rect(435,272.5,50,5)
    
    #house 2
    fill(50)
    rect(150, 250, 150, 150)
    triangle(150,250,300,250,225,100)
    fill(225,225,0)
    rect(165,250,50,50)
    rect(235,250,50,50)
    fill(0)
    rect(187.5,250,5,50)
    rect(257.5,250,5,50)
    rect(165,272.5,50,5)
    rect(235,272.5,50,5)
    
    #pumpkin
    fill(255, 140, 0)
    ellipse(400,400,50,50)
    ellipse(300,400,50,50)
    ellipse(100,400,50,50)
    
    
