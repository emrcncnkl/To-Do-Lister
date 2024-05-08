print('''
 _       _________ _______ _________ _______  _        _______          _________ _______ _________
( \      \__   __/(  ____ \\__   __/(  ____ \( \      (  ____ \|\     /|\__   __/(  ____ \\__   __/
| (         ) (   | (    \/   ) (   | (    \/| (      | (    \/( \   / )   ) (   | (    \/   ) (   
| |         | |   | (_____    | |   | (__    | |      | (__     \ (_) /    | |   | |         | |   
| |         | |   (_____  )   | |   |  __)   | |      |  __)     \   /     | |   | |         | |   
| |         | |         ) |   | |   | (      | |      | (         ) (      | |   | |         | |   
| (____/\___) (___/\____) |   | |   | (____/\| (____/\| (____/\   | |   ___) (___| (____/\___) (___
(_______/\_______/\_______)   )_(   (_______/(_______/(_______/   \_/   \_______/(_______/\_______/
                                                                                                   
''')

yapilacaklar_listesi = []
devam_listesi = 'e'
while devam_listesi == 'e':
    eylem = input("Bir görev eklemek için 'e' girin ve bir görevi silmek için 's' girin:")
    gorev = 0
    if eylem == "e":
        gorev = input("Eklemek istediğiniz görevi girin:")
        yapilacaklar_listesi.append(gorev)
    elif eylem == "s":
        gorev = input("Silmek istediğiniz görevi girin:")
        if gorev in yapilacaklar_listesi:
            yapilacaklar_listesi.remove(gorev)
    print(yapilacaklar_listesi)
    devam_listesi = input("Listeye başka bir öğe eklemek ister misiniz? (e/h)")
