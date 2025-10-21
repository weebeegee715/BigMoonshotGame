# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:

    #Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')

    #Character callback that generates the sound.
    def e(event, **kwargs):
        if event == "show": #When the text is shown
            build_sentence(_last_say_what, "bing")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end": #When the text is finished displaying or you open a menu.
            renpy.sound.stop(channel="beeps")

    #Example of an alternate character callback
    def e2(event, **kwargs):
        if event == "show": #When the text is shown
            build_sentence(_last_say_what, "bing")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end": #When the text is finished displaying or you open a menu.
            renpy.sound.stop(channel="beeps")

define e = Character("Eileen", callback=e)
define e2 = Character("Eileen", callback=e2)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "I just wish my voice function worked!"

    e2 "Me too..."

    # This ends the game.

    return
