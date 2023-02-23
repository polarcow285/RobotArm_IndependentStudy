let count = 0
hummingbird.startHummingbird()
hummingbird.setPositionServo(FourPort.One, 0)
hummingbird.setPositionServo(FourPort.Two, 0)
hummingbird.setPositionServo(FourPort.Three, 0)
let link1CurrPos = 0
basic.forever(function on_forever() {
    let link1CurrPos: number;
    
    hummingbird.setPositionServo(FourPort.One, link1CurrPos)
    link1CurrPos = link1CurrPos + 1
    basic.pause(35)
    /** 
    while(link1CurrPos != 90):
        hummingbird.set_position_servo(FourPort.ONE, link1CurrPos)
        basic.pause(35)
        link1CurrPos = link1CurrPos + 1
    basic.pause(1000)
    while(link1CurrPos != 90):
        hummingbird.set_position_servo(FourPort.ONE, link1CurrPos)
        basic.pause(35)
        link1CurrPos = link1CurrPos - 1
    
 */
})
