#create a list of play options
t = ["Batu", "Kertas", "Gunting"]

#assign a random play to yhe computer
computer = t[randint (0,2)]

#set player to false
player = false

while palyer == false;
#set player to true
    player = input ["Batu, gunting, kertas?"]
    if player == computer:
        print("Seri!")
    elif player == "Batu":
        if computer == "Kertas":
            print ("Anda Kalah!", computer, "menutup", player)
        else:
            print ("Anda Menang!", player, "memukul", computer)
    elif player == "Kertas":
        if computer == "Gunting":
            print ("Anda Kalah!", computer, "memotong", player)
        else:
            print ("Anda Menang!", player, "menutup", computer)
    elif player == "Gunting":
        if computer == "Batu":
            print ("Anda Kalah....", computer, "memukul", player)
        else:
            print ("Anda Menang!", player, "memotong", computer)
        else:
            print ("input tidak valid. perhatikan penulisan anda!")
        #player was set to  true, but we want it to be false so the loop continues
        player = false
        computer = t[randint(0,2)]