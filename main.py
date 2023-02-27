link1CurrPos = 0
link2CurrPos = 0
link3CurrPos = 0
hummingbird.start_hummingbird()
hummingbird.set_position_servo(FourPort.ONE, 0)
hummingbird.set_position_servo(FourPort.TWO, 0)
hummingbird.set_position_servo(FourPort.THREE, 0)

def on_forever():
    moveTo(0, 0, 0)
    basic.pause(1000)
basic.forever(on_forever)

def moveTo(target1, target2, target3):
    global link1CurrPos
    global link2CurrPos
    global link3CurrPos
    while(link1CurrPos != target1 or link2CurrPos != target2 or link3CurrPos != target3):
        if(link1CurrPos > target1):
            link1CurrPos -= 1
        elif(link1CurrPos < target1):
            link1CurrPos += 1
        if(link2CurrPos > target2):
            link2CurrPos -= 1
        elif(link2CurrPos < target2):
            link2CurrPos += 1
        if(link3CurrPos > target3):
            link3CurrPos -= 1
        elif(link3CurrPos < target3):
            link3CurrPos += 1
        hummingbird.set_position_servo(FourPort.ONE, link1CurrPos)
        hummingbird.set_position_servo(FourPort.TWO, link2CurrPos)
        hummingbird.set_position_servo(FourPort.THREE, link3CurrPos)
        basic.pause(10)
