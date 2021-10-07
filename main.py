def on_forever():
    pass

def stiskbtnA():
    basic.show_icon(IconNames.HEART)
def stiskbtnB():
    basic.show_icon(IconNames.DIAMOND)
def stiskbtnC():
    basic.show_icon(IconNames.YES)

basic.forever(on_forever)
input.on_button_pressed(Button.A, stiskbtnA)
input.on_button_pressed(Button.AB, stiskbtnC)
input.on_button_pressed(Button.B, stiskbtnB)