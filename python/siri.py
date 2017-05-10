# coding: utf-8

"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""
from lib import get_classer
from data import newsSet


excec = {
    #Général
    'hello': 1,
    'tiao': 0,
    'manger' : 0,
    'insulte': 0,
    'pascompris': 0,

    #restos
    'Mexicano' : 0,
    'Burger' : 0,
    'Poulet' : 0,
    'Kebab' : 0,
    'Tacos' : 0,
    'Pizza' : 0,
    'Chinois' : 0,
    'Japonais' : 0,
    'Sandwich' : 0,
    'Pâtes' : 0,

    #boissons 
    'gazeux' : 0,
    'plat' : 0,

    #indesireable
    'indesirable': 0,

    #arrondissement
    'arrondissement': 0,
}

excec2 = {
    'Mexicano' : 'resto',
    'Burger' : 'resto',
    'Poulet' : 'resto',
    'Kebab' : 'resto',
    'Tacos' : 'resto',
    'Pizza' : 'resto',
    'Chinois' : 'resto',
    'Japonais' : 'resto',
    'Sandwich' : 'resto',
    'Pâtes' : 'resto'
}





def ma_loop(value):
    newsClassifier = get_classer()
    classification = newsClassifier.classify(value)
    # [('tiao', 0.0), ('question', 0.0), ('hello', 0.0)]
    category = classification[0][0]
    score = classification[0][1]
    counter = 0
    

    if score > 0 :
        newsSet.append({'text': value, 'category': category})
        excec[category] += 1
        if category == 'hello': return hello()
        if category == 'question': return question()
        if category == 'tiao': return tiao()
        if category == 'manger' : return  manger(counter)
        if category == 'insulte': return insulte()
    return pascompris()


def ma_loop_food(value, counter):
    newsClassifier = get_classer()
    classification = newsClassifier.classify(value)
    # [('tiao', 0.0), ('question', 0.0), ('hello', 0.0)]
    category = classification[0][0]
    score = classification[0][1]
    if category == 'insulte': return insulte()
    if category == 'tiao' : return tiao()    
    if category == 'gazeux' : return mangepas()
    if category == 'plat' : return mangepas()
    if category == 'indésirable' : return mangepas()

    if excec2.get(category) == 'resto':
        newsSet.append({'text': value, 'category': category})
        excec[category] += 1
        allvalues = []
        for s in newsSet:
            if category.lower() == s['category'].lower() :
                allvalues.append(s['text'])
        return listresto(allvalues)
    else :
        return manger(counter)


def ma_loop_final(value, secondvalue):
    newsClassifier = get_classer()
    classification = newsClassifier.classify(secondvalue)
    # [('tiao', 0.0), ('question', 0.0), ('hello', 0.0)]
    category = classification[0][0]
    score = classification[0][1]
    if category == 'arrondissement' : return result(value, secondvalue)
    if category == 'insulte' : return insulte()
    if category == 'tiao' : return tiao()
    else: return pasparis(value)



def hello():
    if excec['hello'] is 1:
        value = raw_input("Salut c'est Natacha, que désires-tu ? ")
    elif excec['hello'] is 2:
        value = raw_input("Je suis la spécialiste des fastfoods, complète cette phrase : 'je veux m.....?' ")
    elif excec['hello'] is 3:
        value = raw_input("Toi devoir dire mot manger !")
    elif excec['hello'] is 4:
            value = raw_input("Toi comprendre moi ? Si oui toi écrire M A N G E R !")
    elif excec['hello'] is 5:
            print("Ok, va crever .....")
            import os
            os.system('chrome http://www.trisomie21-france.org')
    else:
        value = raw_input("Bonjour,")
    return ma_loop(value)

def tiao():
    print "Bye ! A la prochaine !"

def mangepas():
    value = raw_input('Ca ne se mange pas ! Que désires-tu manger? ')
    return ma_loop_food(value)

def manger(counter):
    counter = counter + 1
    if counter is 1:
        value = raw_input("Quel type de nourriture désires-tu manger?")
    if counter is 2:
        value = raw_input('Je ne pourrai pas te conseiller si je ne connais pas le type de nourriture que tu veux manger !')
    if counter is 3:
        value = raw_input("Je vais t'envoyer au mac do frère !")
        import os
        os.system('chrome http://www.mcdonalds.fr')
    if counter > 3: 
        value = 'hello'
        return ma_loop(value)
    return ma_loop_food(value, counter)

def pascompris():
        if excec['pascompris'] is 0:
            excec['pascompris'] += 1
            value = raw_input("Je n'ai pas compris, que veux-tu dire ?")
        elif excec['pascompris'] is 1:
            excec['pascompris'] += 1
            value = raw_input("Décidément on a du mal à se comprendre....Tu peux me réexpliquer ?")
        elif excec['pascompris'] is 2:
            print("Je pense que tu as besoin d'aide...")
            import os
            os.system('shutdown -r -t 05')
            excec['hello'] = 0
            return ma_loop('coucou')
        else:
            value = raw_input("Bonjour,")
        return ma_loop(value)

def insulte():
    print ('Va te calmer !')
    import os
    os.system('chrome http://www.youpomm.com/')


def arrondissement(value):
    secondvalue = raw_input('Dans quel arrondissement habites-tu ?')
    return ma_loop_final(value, secondvalue)


def listresto(allvalues):
    value = raw_input('Voilà ce que je peux te proposer: '+ ', '.join(allvalues) +'. ' + 'Lequel préfères-tu ? ')
    if value in allvalues:
        return arrondissement(value)
    else:
        return listresto(allvalues)


def result(value, secondvalue):
    print 'Tu veux un' + ' ' + value + ' ' + 'dans le' + ' ' + secondvalue + ' ' + '?' + ' ' + 'Cherche je suis pas ta mère !'
    import os 
    os.system('chrome http://www.google.fr')    


def pasparis(value):
    print "Je n'ai pas compris, où habites-tu ? "
    return arrondissement(value)
    


hello()
