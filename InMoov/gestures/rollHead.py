# -- coding: utf-8 --

def rollHead():
  i01.setHeadSpeed(0.75, 0.75)
  i01.moveHead(90,90,20)
  sleep(0.5)
  i01.moveHead(90,90,170)
  sleep(1)
  i01.moveHead(90,90,20)
  sleep(1)
  i01.moveHead(90,90,170)
  sleep(1)
  i01.moveHead(90,90,90)
  sleep(1)
  i01.mouth.speakBlocking("thanks a lot, it feels great. doctor")
  #i01.mouth.speakBlocking(u"Большое спасибо, он чувствует себя прекрасно. Доктор")
