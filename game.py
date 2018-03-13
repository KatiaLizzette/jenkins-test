def game(p1, p2):
    """
    enter values that represent the player choice
    Return p1 if player 1 wins otherway p2
    """

    l=['R','S','P','r','s','p']
    if ((p1 in l) and (p2 in l)):
        if (p1 == p2):
            return 'Empate'
        elif ((p1=="" and p2=="")or(p1=="" and p2=='R') or (p1=='R' and p2=="")or(p1=="" and p2=='P') or (p1=='P' and p2=="") or (p1=="" and p2=='S') or (p1=='S' and p2=="")):
            return 'p'
        elif( (p1 == 'R' and p2 =='S') or (p1 == 'P' and p2 =='R') or (p1 == 'S' and p2 =='P') or (p1 == 'r' and p2 =='s') or (p1 == 'p' and p2 =='r') or (p1 == 's' and p2 =='p')):
            return 'p1'
        else:
            return 'p2'
    else:
        return 'False'
    

"game('R','S')"




