# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("val.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("mid_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("high_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


define v = Character("Val", callback=low_beep)

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

    "val is about to talk. Wow."

    v "Oh, to speak with a voice, this text is on and on and on and on lalalala."

    menu:
        "I hate you val ur a burger.":

            v "thats not very nice bro."

            jump mad_val
    
        "Yo val you are lowkey fire. I like ur voicebeep":

            v "Awhh thank you!"

            jump happy_val

label happy_val:
    v "I've never felt so appreiciated in my life before. You're a lovely person."

    $ topics = ["Love", "Life", "The political and economical state of the world"]
label goodval_chat:
    menu:
        "Love" if "Love" in topics:
            $ topics.remove("Love")

            v "Love is really an odd thing!"
            jump goodval_chat

        "Life" if "Life" in topics:
            $ topics.remove("Life")

            v "Life is everything, no?"
            jump goodval_chat
        
        "The political and economical state of the world" if "The political and economical state of the world" in topics:
            $ topics.remove("The political and economical state of the world")
             
            v "I mean, its pretty bad."
            $ topics.append("really")
            jump goodval_chat

        "Thats all you have to say??" if "really" in topics:
            $ topics.remove("really")
            v "Well yeah. I don't care very much..."
            jump goodval_chat

    v "that was a nice talk."

    
    # This ends the game.

    return

label mad_val:
    v "I've never felt so disrespected in my life before. You're an awful person."

    $ topics = ["Hate", "Death", "The political and economical state of the world"]
label badval_chat:

    menu:
        "Death" if "Death" in topics:
            $ topics.remove("Death")

            v "It comes for us all... especially you because you called me a burger"
            jump badval_chat

        "Hate" if "Hate" in topics:
            $ topics.remove("Hate")

            v "What I feel for you. Meanie."
            jump badval_chat
        
        "The political and economical state of the world" if "The political and economical state of the world" in topics:
            $ topics.remove("The political and economical state of the world")
             
            v "I mean, its pretty bad."
            $ topics.append("really")
            jump badval_chat

        "Thats all you have to say??" if "really" in topics:
            $ topics.remove("really")
            v "Well yeah. I don't care very much..."
            jump badval_chat
        
    v "I didn't enjoy chattiing with you today."

    return