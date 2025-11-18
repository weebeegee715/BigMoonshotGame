# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def val_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("val.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def mira_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("mira.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
            
define v = Character("Val", callback=val_beep, color="#de9c01")
define m = Character("Mira", callback=mira_beep, color="#329b15")

define typography(what):

    replacements = [
            (".",".{w=.2}")
            
    ]

# The game starts here.

label start:
    play music 'audio/wallpaper.mp3' fadein 0.3


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "val and mira are about to talk. Wow."

    v "Hi I'm Val, who are you?"

    m "I'm mira let's talk, I just got my voice so I want to talk a lot to see how my voicebeep sounds."

    v "This game's taking a {bt=5}lonnggg timee{/bt} to make, no? "
    
    m "Ikr, its kinda ridiculous"

    v "But that's ok!! We'll be complete in no time"
    
    m "{sc}But we don't even have sprites yet...{/sc}"

    v "That's okayy, theyre just in the sketchbook rn."

    v " I'm {swap=Victoria@Valencia@0.3}name{/swap} ! - IM {swap=VALENCIA@VICTORIA@0.1}{sc}NAME{/sc}{/swap} !"

    v "{sc}I don't know...{/sc}"

    m "lol that'd be cool if the game actually got made..."

    v "ikr so much loree"

    menu:
        "I hate you val ur a burger.":

            m "Not gonna lie, you seem like a burger."
            v "thats not very nice bro."

            jump mad_val
    
        "Yo val you are lowkey fire. I like ur voicebeep":

            m "Your voicebeep is amazing!"
            v "Awhh thank you!"

            jump happy_val

label happy_val:
    v "I've never felt so appreiciated in my life before. You're a lovely person."

    $ topics = ["Love", "Life", "The political and economical state of the world"]
label goodval_chat:
    menu:
        "Love" if "Love" in topics:
            $ topics.remove("Love")

            m "What is love?"
            v "Love is really an odd thing!"
            jump goodval_chat

        "Life" if "Life" in topics:
            $ topics.remove("Life")

            m "What is your take on life?"
            v "Life is everything, no?"
            jump goodval_chat
        
        "The political and economical state of the world" if "The political and economical state of the world" in topics:
            $ topics.remove("The political and economical state of the world")
             
            m "Opinions on politicoeconomics?"
            v "I mean, its pretty bad."
            $ topics.append("really")
            jump goodval_chat

        "Thats all you have to say??" if "really" in topics:
            $ topics.remove("really")
            m "That's all you have to say?"
            v "Well yeah. I don't care very much..."
            jump goodval_chat

    v "that was a nice talk."
    m "yeah!"

    jump the_end

label mad_val:
    v "I've never felt so disrespected in my life before. You're an awful person."

    $ topics = ["Hate", "Death", "The political and economical state of the world"]
label badval_chat:

    menu:
        "Death" if "Death" in topics:
            $ topics.remove("Death")
            m "What's your take on death?"
            v "It comes for us all... especially you because you called me a burger"
            jump badval_chat

        "Hate" if "Hate" in topics:
            $ topics.remove("Hate")

            m "what is hate, truly?"
            v "What I feel for you. Meanie."
            jump badval_chat
        
        "The political and economical state of the world" if "The political and economical state of the world" in topics:
            $ topics.remove("The political and economical state of the world")
            
            m "how do you feel about politicoeconomics?"
            v "I mean, its pretty bad."
            $ topics.append("really")
            jump badval_chat

        "Thats all you have to say??" if "really" in topics:
            $ topics.remove("really")
            m "Wasn't that a bit of a shallow answer, genius?"
            v "Well yeah. I don't care very much..."
            jump badval_chat
        
    v "I didn't enjoy chatting with you today."
    m "Oh, well."

    jump the_end

label the_end:
v ".   .   ."
v "Well bye now."

return