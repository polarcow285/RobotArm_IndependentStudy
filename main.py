count = 0
hummingbird.start_hummingbird()
hummingbird.set_position_servo(FourPort.ONE, 0)
hummingbird.set_position_servo(FourPort.TWO, 0)
hummingbird.set_position_servo(FourPort.THREE, 0)
link1CurrPos = 0
def on_forever():
    global count
    hummingbird.set_position_servo(FourPort.ONE, link1CurrPos)
    link1CurrPos = link1CurrPos + 1
    basic.pause(35)
    '''
    while(link1CurrPos != 90):
        hummingbird.set_position_servo(FourPort.ONE, link1CurrPos)
        basic.pause(35)
        link1CurrPos = link1CurrPos + 1
    basic.pause(1000)
    while(link1CurrPos != 90):
        hummingbird.set_position_servo(FourPort.ONE, link1CurrPos)
        basic.pause(35)
        link1CurrPos = link1CurrPos - 1
    '''
basic.forever(on_forever)