y=0
y1=0
y2=0
y3=0
y4=0
y5=0
y6=0
y7=0
y8=0
y9=0
y10=0
y11=0
y12=0
y13=0
y14=0
y15=0
y16=0
y17=0
y18=0
y19=0
y20=0
def setup():
    size(800,800)
    background(28,84,131)
  
def draw():
    global y,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20
    background(28,84,131)
    ellipse(400,800,800,300)
    ellipse(400,600,100,100)
    ellipse(400,530,80,80)
    ellipse(400,470,60,60)
    strokeWeight(8)
    point(390,470)
    point(410,470)
    strokeWeight(0)
    fill(250,127,3)
    triangle(406,480,400,500,400,480)
    fill(255,255,255)
    ellipse(244,y1,10,10)
    ellipse(463,y2,10,5)
    ellipse(332,y3,4,13)
    ellipse(742,y4,4,5)
    ellipse(372,y5,2,6)
    ellipse(643,y6,8,9)
    ellipse(534,y7,5,9)
    ellipse(546,y8,2,10)
    ellipse(490,y9,10,2)
    ellipse(789,y10,12,3)
    ellipse(575,y11,8,17)
    ellipse(12,y12,8,17)
    ellipse(24,y13,8,17)
    ellipse(156,y14,8,17)
    ellipse(34,y15,8,17)
    ellipse(269,y16,8,17)
    ellipse(42,y17,8,17)
    ellipse(284,y18,8,17)
    ellipse(123,y19,8,17)
    ellipse(64,y20,8,17)
    y=y+1
    y1=y1+1.9
    y2=y2+1.6
    y3=y3+5.8
    y4=y4+1.3
    y5=y5+1.1
    y6=y6+1.2
    y7=y7+2.0
    y8=y8+2.3
    y9=y9+2.6
    y10=y10+2.2
    y11=y11+2.9
    y12=y12+4.2
    y13=y13+1.1
    y14=y14+1.0
    y15=y15+2.3
    y16=y15+3.3
    y17=y17+2.9
    y18=y18+1.4
    y19=y19+2.6
    y20=y20+3.1
    
    if y1>700:

      y1=0
    
    if y2>700:
        
      y2=0
      
    if y3>700:
        
      y3=0
    
    if y4>700:
        
      y4=0

    if y5>700:
        
      y5=0
      
    if y6>700:
        
      y6=0
    
    if y7>700:
        
      y7=0
      
    if y8>700:
        
      y8=0
 
    if y9>700:
        
      y9=0
    
    if y10>700:
        
      y10=0
      
    if y11>700:
        
      y11=0
      
    if y12>700:
        
      y12=0
   
    if y13>700:
        
      y13=0   
            
    if y14>700:
        
      y14=0
            
    if y15>700:
        
      y15=0
      
    if y16>700:
        
      y16=0
      
    if y17>700:
        
      y17=0
      
    if y18>700:
        
      y18=0
      
    if y19>700:
        
      y19=0
      
    if y20>700:
        
      y20=0  

    textSize (101)
    text(u'с новым годом!!!!',0,200)
      
