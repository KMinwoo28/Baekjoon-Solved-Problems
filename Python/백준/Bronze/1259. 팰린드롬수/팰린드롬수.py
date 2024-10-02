while(True):
    Fel = input()
    if Fel == '0':
        break;
    else:
        if Fel[::-1] == Fel:
            print('yes')
        else:
            print('no')