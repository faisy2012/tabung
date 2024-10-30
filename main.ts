input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(music.volume())
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.soundLevel())
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    if (true) {
        basic.showIcon(IconNames.Happy)
        music.setVolume(255)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Nyan), music.PlaybackMode.InBackground)
        servos.P2.setAngle(180)
        basic.pause(2000)
        servos.P2.setAngle(90)
        basic.clearScreen()
        music.stopMelody(MelodyStopOptions.All)
    }
})
basic.showLeds(`
    . # # # #
    # . # . .
    . # # # .
    . . # . #
    # # # # .
    `)
