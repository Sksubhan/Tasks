def results(eng,hin,phy):
    average=int((eng+hin+phy)/3)
    if eng>=30 and hin>=30 and phy>=30 and 0<average<=100:
        if 30<=average<40:
            return 'you got E grade'

        elif 40<=average<55:
            return 'you got D grade'

        elif 55<=average<70:
            return 'you got C grade'

        elif 70<=average<85:
            return 'you got B grade'

        elif 85<=average<92:
            return 'You got A grade'

        elif 92<=average<=100:
            return 'You got A+ grade'
        return 'Passed :'+str(average)
    else:
        return f'You are failed :{average}'


