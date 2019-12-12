def web_page():  
  html = """<html>
  <head>
    <title>FPV Bot Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:, ">
    <style>
      html{
        font-family:Helvetica;
        display: inline-block;
        margin: 0px auto;
        text-align: center;
        }
      h1{
        color: #0033cc;
        padding: 2vh;
      }
      p{
        font-size: 1.5rem;
      }
      .button{
        display: inline-block;
        background-color: #3366ff;
        border: none;
        border-radius: 4px;
        color: white;
        padding: 16px 40px;
        text-decoration: none;
        font-size: 30px;
        margin: 2px;
        cursor: pointer;
      }
      .button2{
        background-color: #4286f4;
      }
    </style>
  </head>
  <body>
    <h1>FPV-bot Control Panel</h1>
    <p><a href="/?turbo=on"><button class="button">Turbo</button></a></p>
    <p><a href="/?forward=on"><button class="button">Forward</button></a></p>
    <p><a href="/?turnLeft"><button class="button">Turn Left</button></a>
    <a href="/?turnRight"><button class="button">Turn Right</button></a></p>
    <p><a href="/?turnOff"><button class="button">Break</button></a></p>
    <p><a href="/?reverse=on"><button class="button">Return</button></a></p>
    <p>
      <a href="/?servo=left"><button class="button">Pivot Cam Left</button></a>
      <a href="/?servo=middle"><button class="button">Pivot Cam Middle</button></a>
      <a href="/?servo=right"><button class="button">Pivot Cam Right</button></a>
    </p>
  </body>
  </html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
s.settimeout(9999)
while True:
  try:
    conn, addr = s.accept()
  except OSError:
    s.bind(('', 80))
    s.listen(5)
    s.settimeout(999)
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)

  forward_on = request.find('/?forward=on')

  left_on = request.find('/?left=on')
  left_off = request.find('/?left=off')

  right_on = request.find('/?right=on')
  right_off = request.find('/?right=off')

  reverse_on = request.find('/?return=on')
  reverse_off = request.find('/?return=off')

  turnLeft = request.find('/?turnLeft')
  turnRight = request.find('/?turnRight')
  
  turnOff = request.find('/?turnOff')
  
  turbo_drive = request.find('/?turbo=on')

  servo_left = request.find('/?servo=left')
  servo_middle = request.find('/?servo=middle')
  servo_right = request.find('/?servo=right')
#

  speed = 524

#

  if forward_on == 6:
    print('Forward ON')
    dir_a.value(0)
    dir_b.value(0)
    pwm_a.duty(speed)
    pwm_b.duty(speed)

#
  if left_on == 6:
    print('LEFT ON')
    dir_a.value(0)
    pwm_a.duty(speed)
    
#
  if left_off == 6:
    print('LEFT OFF')
    dir_a.value(0)
    pwm_a.duty(0)
#
  if right_on == 6:
    print('RIGHT ON')
    dir_b.value(0)
    pwm_b.duty(speed)
#
  if right_off == 6:
    print('RIGHT OFF')
    dir_b.value(0)
    pwm_b.duty(0)
#
  if reverse_on == 6:
    print('REVERSE ON')
    dir_a.value(1)
    dir_b.value(1)
    pwm_a.duty(speed)
    pwm_b.duty(speed)
#
  if reverse_off == 6:
    print('REVERSE OFF')
    dir_a.value(0)
    dir_b.value(0)
    
   
#
  if turnLeft == 6:
    print('TURN LEFT ON')
    dir_a.value(1)
    pwm_a.duty(speed)
    dir_b.value(0)
    pwm_b.duty(speed)
#
  if turnRight == 6:
    print('TURN RIGHT ON')
    dir_a.value(0)
    pwm_a.duty(speed)
    dir_b.value(1)
    pwm_b.duty(speed)
#
  if turnOff == 6:
    print('OFF')
    dir_a.value(0)
    pwm_a.duty(0)
    dir_b.value(0)
    pwm_b.duty(0)
#

  if turbo_drive == 6:
    print('TURBO ON')
    dir_a.value(0)
    pwm_a.duty(1024)
    dir_b.value(0)
    pwm_b.duty(1024)

#

  if servo_left == 6:
    print('SERVO POSITION LEFT')
    servo.duty(30)
#
  if servo_middle == 6:
    print('SERVO POSITION MIDDLE')
    servo.duty(50)
#
  if servo_right == 6:
    print('SERVO POSITION RIGHT')
    servo.duty(80)




  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
