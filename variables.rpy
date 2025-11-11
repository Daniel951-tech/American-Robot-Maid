# esse script vai ser para declarar personagens e variaveis
label characterdefines:
    define mc = Character("Voce", color="#010391ff", who_outlines=[(0.5,"#ffffff")])
    define pai = Character("Pai", color="#5c5300ff", who_outlines=[(0.5, "#ffffff")])
    define mae = Character("Mãe", color="#6d006d", who_outlines=[(0.5,"#faf5f5ff")])

label other:
    define slowdissolve = Dissolve(1.0)
    define fastishdissolve = Dissolve(0.3)
    define fastdissolve = Dissolve(0.1)
    
label splashscreen:
    scene bg_intro with dissolve
    pause 4.5
    scene thiswork with dissolve
    pause 4
    scene black with dissolve
    pause 2    
    return