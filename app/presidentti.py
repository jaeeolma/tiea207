#-*- coding: utf8 -*-

def hae_presidentti(year):
    presidentin_kuva = ''
    if (1919 <= int(year) <= 1924 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/d/d0/Kaarlo_Juho_St%C3%A5hlberg.jpg'
    if (1925 <= int(year) <= 1930 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/8/86/Lauri_Kristian_Relander.jpg'
    if (1931 <= int(year) <= 1936 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/a/a1/P._E._Svinhufvud.png'
    if (1937 <= int(year) <= 1939 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Ky%C3%B6sti_Kallio.png'
    if (1940 <= int(year) <= 1943 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Risto_Ryti.jpg'
    if (1944 <= int(year) <= 1945 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Carl_Gustaf_Emil_Mannerheim.png'
    if (1946 <= int(year) <= 1955 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Juho_Kusti_Paasikivi.jpg'
    if (1956 <= int(year) <= 1981 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/f/f5/Urho_Kaleva_Kekkonen.jpg'
    if (1982 <= int(year) <= 1993 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/d/da/Mauno_Koivisto.png'
    if (1994 <= int(year) <= 1999 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/4/4f/Martti_Ahtisaari%2C_tidigare_president_Finland_och_mottagare_av_Nobels_fredrspris_%282%29.jpg'
    if (2000 <= int(year) <= 2011 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Tarja_Halonen_1c389_8827-2.jpg'
    if (2012 <= int(year) <= 2016 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/a/a8/Sauli_Niinist%C3%B6_%28cropped%29.jpg'
    return presidentin_kuva

def hae_presidentin_nimi(year):
    presidentin_nimi = ''
    if (1919 <= int(year) <= 1924 ):
        presidentin_nimi = u'Kaarlo Juho Ståhlberg'
    if (1925 <= int(year) <= 1930 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/8/86/Lauri_Kristian_Relander.jpg'
    if (1931 <= int(year) <= 1936 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/a/a1/P._E._Svinhufvud.png'
    if (1937 <= int(year) <= 1939 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Ky%C3%B6sti_Kallio.png'
    if (1940 <= int(year) <= 1943 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Risto_Ryti.jpg'
    if (1944 <= int(year) <= 1945 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Carl_Gustaf_Emil_Mannerheim.png'
    if (1946 <= int(year) <= 1955 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Juho_Kusti_Paasikivi.jpg'
    if (1956 <= int(year) <= 1981 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/f/f5/Urho_Kaleva_Kekkonen.jpg'
    if (1982 <= int(year) <= 1993 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/d/da/Mauno_Koivisto.png'
    if (1994 <= int(year) <= 1999 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/4/4f/Martti_Ahtisaari%2C_tidigare_president_Finland_och_mottagare_av_Nobels_fredrspris_%282%29.jpg'
    if (2000 <= int(year) <= 2011 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Tarja_Halonen_1c389_8827-2.jpg'
    if (2012 <= int(year) <= 2016 ):
        presidentin_kuva = 'https://upload.wikimedia.org/wikipedia/commons/a/a8/Sauli_Niinist%C3%B6_%28cropped%29.jpg'
    return presidentin_nimi