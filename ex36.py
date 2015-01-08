from sys import exit

def formation_vote():
    print "Choose your formation:"
    formation_list = ['4-4-2', '4-3-3', '3-4-3', '3-5-2', '5-3-2']
    print formation_list
    choice = raw_input("> ")
    if choice == '4-4-2':
        formation_442()
    elif choice == '4-3-3':
        formation_433()
    elif choice == '3-4-3':
        formation_343()
    elif choice == '3-5-2':
        formation_352()
    elif choice == '5-3-2':
        formation_532()
    else:
        dead("You have to choose a formation!")

def goalkeeper_list():
    print "Choose your goalkeeper:"
    gk_list = ['Manuel Neuer', 'Thibaut Courtois', 'Gianluigi Buffon', 'Beto']
    print gk_list

def defender_list():
    print "Choose your defenders:"
    def_list = ['David Alaba', 'Medhi Benatia', 'Jerome Boateng', 'Daniel Carvajal', 'Ezequiel Garay', 'Diego Godin', 'Mats Hummel', 'Vincent Kompany', 'Philipp Lamn', 'Miranda', 'Sergio Ramos', 'Pablo Zabaleta']
    print def_list
    
def midfielder_list():
    print "Choose your midfielders:"
    mid_list = ['Xabi Alonso', 'Arda Turan', 'Angel Di Maria', 'James Rodriguez', 'Koke', 'Toni Kroos', 'Luka Modric', 'Paul Pogba', 'Ivan Rakitic', 'Marco Reus', 'Arjen Robben', 'Yaya Toure']
    print mid_list
    
def forward_list():
    print "Choose your forwards:"
    for_list = ['Alexis Sanchez', 'Gareth Bale', 'Karim Benzema', 'Diego Costa', 'Zlatan Ibrahimovic', 'Robert Lewandowski', 'Lionel Messi', 'Thomas Muller', 'Neymar', 'Carlos Tevez', 'Cristiano Ronaldo', 'Jonatan Soriano']
    print for_list
    
def formation_442():
    goalkeeper_list()
    gk_choice = raw_input("> ")
    defender_list()
    def_choice = raw_input("> ")
    midfielder_list()
    mid_choice = raw_input("> ")
    forward_list()
    for_choice = raw_input("> ")
    
    print "Your 2014 Team of the Year:"
    print "----------", gk_choice, "----------"
    print def_choice
    print mid_choice
    print for_choice
    
        
def dead(why):
    print why, "Bye!"
    exit(0)



formation_vote()


