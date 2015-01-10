from sys import exit

def formation_vote():
    print "Choose your formation:"
    formation_list = ['4-4-2', '4-3-3', '3-4-3', '3-5-2', '5-3-2']
    for form in formation_list:
         print form
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

##################list of players
def goalkeeper_list():
    print "Choose your goalkeeper:"
    gk_list = ['Manuel Neuer', 'Thibaut Courtois', 'Gianluigi Buffon', 'Beto']
    for gk_name in gk_list:
        print gk_name

def defender_list():
    print "Choose your defenders:"
    def_list = ['David Alaba', 'Medhi Benatia', 'Jerome Boateng', 'Daniel Carvajal', 'Ezequiel Garay', 'Diego Godin', 'Mats Hummel', 'Vincent Kompany', 'Philipp Lamn', 'Miranda', 'Sergio Ramos', 'Pablo Zabaleta']
    for def_name in def_list:
        print def_name
    
def midfielder_list():
    print "Choose your midfielders:"
    mid_list = ['Xabi Alonso', 'Arda Turan', 'Angel Di Maria', 'James Rodriguez', 'Koke', 'Toni Kroos', 'Luka Modric', 'Paul Pogba', 'Ivan Rakitic', 'Marco Reus', 'Arjen Robben', 'Yaya Toure']
    for mid_name in mid_list:
        print mid_name
    
def forward_list():
    print "Choose your forwards:"
    for_list = ['Alexis Sanchez', 'Gareth Bale', 'Karim Benzema', 'Diego Costa', 'Zlatan Ibrahimovic', 'Robert Lewandowski', 'Lionel Messi', 'Thomas Muller', 'Neymar', 'Carlos Tevez', 'Cristiano Ronaldo', 'Jonatan Soriano']
    for for_name in for_list:
        print for_name
#######################    
def formation_442():
    goalkeeper_list()
    gk_choice = raw_input("> ")
    defender_list()
    def_choice1 = raw_input("> ")
    defender_list()
    def_choice2 = raw_input("> ")
    defender_list()
    def_choice3 = raw_input("> ")
    defender_list()
    def_choice4 = raw_input("> ")
    midfielder_list()
    mid_choice1 = raw_input("> ")
    midfielder_list()
    mid_choice2 = raw_input("> ")
    midfielder_list()
    mid_choice3 = raw_input("> ")
    midfielder_list()
    mid_choice4 = raw_input("> ")
    forward_list()
    for_choice1 = raw_input("> ")
    forward_list()
    for_choice2 = raw_input("> ")
    
    print "Confirm your team? (y/n)"
    submit = raw_input("> ").lower()
    if submit == 'n':
        formation_vote()
    else:
        print "\nYour 2014 Team of the Year:"
        print "--------------------------", gk_choice, "--------------------------\n"
        print def_choice1, "-----", def_choice2, "-----", def_choice3, "-----", def_choice4, "\n"
        print "---", mid_choice1, "---", mid_choice2, "---", mid_choice3, "---", mid_choice4, "\n"
        print "----------", for_choice1, "-----", for_choice2, "----------"
    
    
        

def formation_433():
    goalkeeper_list()
    gk_choice = raw_input("> ")
    defender_list()
    def_choice1 = raw_input("> ")
    defender_list()
    def_choice2 = raw_input("> ")
    defender_list()
    def_choice3 = raw_input("> ")
    defender_list()
    def_choice4 = raw_input("> ")
    midfielder_list()
    mid_choice1 = raw_input("> ")
    midfielder_list()
    mid_choice2 = raw_input("> ")
    midfielder_list()
    mid_choice3 = raw_input("> ")
    forward_list()
    for_choice1 = raw_input("> ")
    forward_list()
    for_choice2 = raw_input("> ")
    forward_list()
    for_choice3 = raw_input("> ")
    
    print "Confirm your team? (y/n)"
    submit = raw_input("> ").lower()
    if submit == 'n':
        formation_vote()
    else:
        print "\nYour 2014 Team of the Year:"
        print "--------------------------", gk_choice, "--------------------------\n"
        print def_choice1, "-----", def_choice2, "-----", def_choice3, "-----", def_choice4, "\n"
        print "---", mid_choice1, "---", mid_choice2, "---", mid_choice3, "---""\n"
        print "--", for_choice1, "--", for_choice2, "--", for_choice3, "--"
        
def formation_343():
    goalkeeper_list()
    gk_choice = raw_input("> ")
    defender_list()
    def_choice1 = raw_input("> ")
    defender_list()
    def_choice2 = raw_input("> ")
    defender_list()
    def_choice3 = raw_input("> ")
    midfielder_list()
    mid_choice1 = raw_input("> ")
    midfielder_list()
    mid_choice2 = raw_input("> ")
    midfielder_list()
    mid_choice3 = raw_input("> ")
    midfielder_list()
    mid_choice4 = raw_input("> ")
    forward_list()
    for_choice1 = raw_input("> ")
    forward_list()
    for_choice2 = raw_input("> ")
    forward_list()
    for_choice3 = raw_input("> ")
    
    print "Confirm your team? (y/n)"
    submit = raw_input("> ").lower()
    if submit == 'n':
        formation_vote()
    else:
        print "\nYour 2014 Team of the Year:"
        print "--------------------------", gk_choice, "--------------------------\n"
        print "-----", def_choice1, "-----", def_choice2, "-----", def_choice3, "-----", "\n"
        print mid_choice1, "---", mid_choice2, "---", mid_choice3, "---", mid_choice4, "\n"
        print "--", for_choice1, "--", for_choice2, "--", for_choice3, "--"
    
def formation_352():
    goalkeeper_list()
    gk_choice = raw_input("> ")
    defender_list()
    def_choice1 = raw_input("> ")
    defender_list()
    def_choice2 = raw_input("> ")
    defender_list()
    def_choice3 = raw_input("> ")
    midfielder_list()
    mid_choice1 = raw_input("> ")
    midfielder_list()
    mid_choice2 = raw_input("> ")
    midfielder_list()
    mid_choice3 = raw_input("> ")
    midfielder_list()
    mid_choice4 = raw_input("> ")
    midfielder_list()
    mid_choice5 = raw_input("> ")
    forward_list()
    for_choice1 = raw_input("> ")
    forward_list()
    for_choice2 = raw_input("> ")
    
    print "Confirm your team? (y/n)"
    submit = raw_input("> ").lower()
    if submit == 'n':
        formation_vote()
    else:
        print "\nYour 2014 Team of the Year:"
        print "--------------------------", gk_choice, "--------------------------\n"
        print "-----", def_choice1, "-----", def_choice2, "-----", def_choice3, "-----", "\n"
        print mid_choice1, "---", mid_choice2, "---", mid_choice3, "---", mid_choice4, "\n"
        print "--------------------------", mid_choice5, "--------------------------\n"
        print "----------", for_choice1, "-----", for_choice2, "----------"
    
def formation_532():
    goalkeeper_list()
    gk_choice = raw_input("> ")
    defender_list()
    def_choice1 = raw_input("> ")
    defender_list()
    def_choice2 = raw_input("> ")
    defender_list()
    def_choice3 = raw_input("> ")
    defender_list()
    def_choice4 = raw_input("> ")
    defender_list()
    def_choice5 = raw_input("> ")
    midfielder_list()
    mid_choice1 = raw_input("> ")
    midfielder_list()
    mid_choice2 = raw_input("> ")
    midfielder_list()
    mid_choice3 = raw_input("> ")
    forward_list()
    for_choice1 = raw_input("> ")
    forward_list()
    for_choice2 = raw_input("> ")
    
    print "Confirm your team? (y/n)"
    submit = raw_input("> ").lower()
    if submit == 'n':
        formation_vote()
    else:
        print "\nYour 2014 Team of the Year:"
        print "--------------------------", gk_choice, "--------------------------\n"
        print "--------------------------", def_choice5, "--------------------------\n"
        print def_choice1, "-----", def_choice2, "-----", def_choice3, "-----", def_choice4, "\n"
        print "---", mid_choice1, "---", mid_choice2, "---", mid_choice3, "---""\n"
        print "----------", for_choice1, "-----", for_choice2, "----------"
    
    
def dead(why):
    print why, "Bye!"
    exit(0)

def start():
    formation_vote()
    
start()


