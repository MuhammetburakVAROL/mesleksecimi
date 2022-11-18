def Mesleksecimi():
    meslek = []

    isim = str(input('Hoşgeldiniz, lütfen isminizi yazınız : '))
    print(50*'-')
    print(f'Merhaba, {isim} \nÖnerilere Evet veya Hayır şeklinde cevap veriniz')
    print(50*'-')
    Alansa = str(input("Sayısal alanım daha iyidir :"))
    print(50*'-')
    Alans = str(input("Sözel alanım daha iyidir :"))
    print(50 * '-')
    Bilgisayar = str(input('Bilgisayar donanımı ve yazılımına ilgi duyarım :'))
    print(50 * '*')
    Yazilim = str(input('Bir şeyler kodlamayı severim :'))
    print(50 * '*')
    Elektrik = str(input('Elektrik ve Elektronik malzemelerine ilgi duyarım :'))
    print(50 * '*')
    Doktor = str(input('İnsanları iyileştirmeyi severim ve biyolojiye ilgi duyarım :'))
    print(50 * '*')
    Hoca = str(input('Çocuklar / gençlere birşeyler öğretmeyi severim :'))
    print(50 * '*')
    Mimar = str(input('Mimari eserler ile uğraşmayı severim :'))
    print(50 * '*')
    Avukat = str(input('Ezberim iyidir ve kendimi iyi ifade ederim :'))
    print(50 * '*')

    if Alansa == 'Evet':
        if Bilgisayar == 'Evet':
            meslek.append('Bilgisayar Mühendisliği')
        if Yazilim == 'Evet':
            meslek.append('Yazılım Mühendisliği')
        if Elektrik == 'Evet':
            meslek.append('Elektrik Elektronik Mühendisliği')
        if Doktor == 'Evet':
            meslek.append('Tıp')
    if Alans == 'Evet':
        if Hoca == 'Evet':
            meslek.append('Öğretmen')
        if Mimar == 'Evet':
            meslek.append('Mimar')
        if Avukat == 'Evet':
            meslek.append('Avukat')




    print(f'Yatkın olabileceğiniz meslekler : {meslek}')

Mesleksecimi()