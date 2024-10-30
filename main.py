input.onButtonPressed(Button.A, function () {
    record.playAudio(record.BlockingState.Blocking)
    record.playAudio(record.BlockingState.Blocking)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(input.lightLevel())
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (input.soundLevel()))
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    record.startRecording(record.BlockingState.Nonblocking)
    record.startRecording(record.BlockingState.Nonblocking)
    if (true) {
        basic.showIcon(IconNames.Happy)
        music.setVolume(255)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Chase), music.PlaybackMode.InBackground)
        servos.P2.setAngle(180)
        basic.pause(2000)
        servos.P2.setAngle(90)
        basic.clearScreen()
        record.startRecording(record.BlockingState.Nonblocking)
        record.startRecording(record.BlockingState.Nonblocking)
    }
})
basic.showLeds(`
    . # # # #
    # . # . .
    . # # # .
    . . # . #
    # # # # .
    `)
