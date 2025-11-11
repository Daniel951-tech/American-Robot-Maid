# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define persistent.dialogueBoxOpacity = 0.1
image bg_intro = "boygames_intro"
image thiswork = "work_of_fiction"

image render1 = "render-mouth-open1"
image render2 = "render-mouth-open2"
image render5 = "render-mouth-close5"
image render6 = "render-surprise6"
image render4 = "render-mouth-open4"
image render7 = "render-sad7"
image render8 = "render-mouth-open8"
image render9 = "render-mouth-open9"
image render10 = "render-pick-towels10"
image render11 = "render-pick-towels11"
image render12 = "render-pick-towels12"
image render13 = "render-pick-towels13"
image render14 = "render-pick-towels14"
image render15 = "render-pick-towels15"
image render16 = "render-pick-towels16"
image render17 = "pants_clothes"
image render18 = "shirt_clothes"
image render19 = "television_talk1"
image render20 = "television_talk2"
image render21 = "tv_news1"
image render22 = "tv_news2"

# The game starts here.

label start:
    $ toalhas = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black with dissolve
    mc "Tchau"
    pause 0.5
    window hide
    #
    scene render1 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 30.0 xalign 1.0
    mc "Tchau mãe"
    mc "Tchau pai"
    mc "Boas-ferias"
    mc "Divirtão-se"
    window hide
    #
    scene render2 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 30.0 xalign 1.0
    mae "Garoto !!!"
    mae "E não esqueça de colocar pra lavar suas toalhas"
    mae "Não esquece de colocar uma calças, antes de ir para faculdade"
    window hide
    #
    scene render6 with dissolve
    mc "!!!"
    mc "Ahh droga" 
    mc "Alguem na rua pode me ver assim"
    window hide
    #
    scene render5 with dissolve
    pai "Filho se comporte"
    pai "Deixe a casa arrumada"
    pai "Tem uma encomenda para chegar"
    pai "Não esqueça de colocar para dentro da casa"
    window hide
    #
    scene render4 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 30.0 xalign 1.0
    mc "Certo pai"
    mc "Até mais"
    mc "Boa-Viagem"
    window hide
    play audio "audio/car-slow-driving-sound-effect1.wav" fadein 0.5 volume 0.2
    #
    scene render7 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0
    mc "Droga"
    mc "Não pude ir com eles"
    mc "Tenho algumas provas finais da universidade"
    window hide
    #
    scene render8 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0
    mc "..."    
    mc "O que eu faço"
    mc "Tenho que colocar aquelas toalhas no cesto pra lavar"
    mc "Mas vou me atrasar"
    window hide
    #
    scene render9 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0    
    menu:
        # escolhas 1
        "Colocar toalhas no cesto?":
            jump toalhas
        "Vou me vestir estou com presa":
            jump vestir
label toalhas:
    $ renpy.notify("Voce não esqueceu das toalhas")
    mc "..."
    mc "Acho que vou deixar as toalhas no cesto"
    mc "Antes de me vistir"
    scene render10 with dissolve
    pause 1.0
    scene render11 with dissolve
    pause 1.0
    scene render12 with fastishdissolve
    pause 1.0
    scene render13 with fastishdissolve      
    pause 1.0
    scene render14 with fastishdissolve
    pause 1.0
    scene render15 with fastishdissolve
    pause 1.0
    scene render16 with fastishdissolve
    mc "Certo agora vou me arrumar"
    window hide
    scene render17 with dissolve
    mc "Droga"
    mc "Essas calças são um pouco apertadas"
    mc "Vou colocar uma outra camiseta"
    window hide
    scene render18 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0
    mc "Certo estou pronto"
    jump apos_vestir
    
return

    #scene render10
label vestir:
    mc "Acho que vou me vestir"
    scene render17 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0
    mc "Droga"
    mc "Essas calças são um pouco apertadas"
    mc "Vou colocar uma outra camiseta"
    window hide
    scene render18 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0
    mc "Certo estou pronto"
    jump apos_vestir

label apos_vestir:
    show black
    play audio "audio/efeito_jornal_tv.wav" fadein 0.5 volume 0.1
    scene render19 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0
    mc "Que barulho é esse" 
    mc "Merda foi essa"
    window hide
    scene render20 with fastishdissolve
    mc "Não acredito que a TV ligou sozinha de novo"
    scene render21 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0
    pause 5   
    scene render22 with dissolve:
        subpixel True
        xalign 0.1 yalign 0.5
        zoom 1.1
        ease 25.0 xalign 1.0
  



    


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show render1

    # show mc


    # These display lines of dialogue.

    # "You've created a new Ren'Py game."

    # "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
