count = 0
hummingbird.start_hummingbird()
hummingbird.set_position_servo(FourPort.ONE, 0)
hummingbird.set_position_servo(FourPort.TWO, 0)
hummingbird.set_position_servo(FourPort.THREE, 0)

def on_forever():
    global count

    for index in range(40):
        hummingbird.set_position_servo(FourPort.ONE, count)
        hummingbird.set_position_servo(FourPort.TWO, count)
        hummingbird.set_position_servo(FourPort.THREE, count)
        basic.pause(35)
        count += 2
        
    for i in range(40):
        hummingbird.set_position_servo(FourPort.ONE, count)
        hummingbird.set_position_servo(FourPort.TWO, count)
        hummingbird.set_position_servo(FourPort.THREE, count)
        basic.pause(35)
        count -= 2
basic.forever(on_forever)
