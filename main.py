def on_forever():
basic.show_icon(IconNames.DIAMOND)
basic.clear_screen()
basic.pause(500)
basic.show_icon(IconNames.SMALL_DIAMOND)
basic.clear_screen()
basic.pause(500)
basic.forever(on_forever)