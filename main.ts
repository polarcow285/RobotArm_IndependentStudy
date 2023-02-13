let count = 0
hummingbird.startHummingbird()
hummingbird.setPositionServo(FourPort.One, 0)
hummingbird.setPositionServo(FourPort.Two, 0)
hummingbird.setPositionServo(FourPort.Three, 0)
basic.forever(function on_forever() {
    
    for (let index = 0; index < 40; index++) {
        hummingbird.setPositionServo(FourPort.One, count)
        hummingbird.setPositionServo(FourPort.Two, count)
        hummingbird.setPositionServo(FourPort.Three, count)
        basic.pause(35)
        count += 2
    }
    for (let i = 0; i < 40; i++) {
        hummingbird.setPositionServo(FourPort.One, count)
        hummingbird.setPositionServo(FourPort.Two, count)
        hummingbird.setPositionServo(FourPort.Three, count)
        basic.pause(35)
        count -= 2
    }
})
