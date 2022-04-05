a=int(input("Ko vēlies darīt?\nIevadi 1, ja vēlies izpētīt formulu apkopojumu.\nIevadi 2, ja vēlies izpildīt testu, lai pārbaudītu savas zināšanas.\n"))
if a==1:
    print("Vidusskolas tēmu formulu apkopojums ķīmijā.")
    list = ['W=m(v)/m(šķ)', 'C=n/V', 'ρ=m/V', 'n=m/M ', 'α=n(dis)/n(kop)',]
    list2 = ['v=±Δc/Δt', 'v=k*c(A)*c(B)', 'vt1/vt2=k**(t2-t1/10)', 'k(līdzsvara)=k(t)/k(p)', 'k(līdzsvara)=c(ab)/(c(a)*c(b))'] 
    
    fmt = '{:<8}{:<20}{}'
    
    print(fmt.format('', 'Dispersās sistēmas', 'Ķīmisko reakciju norise'))
    for i, (disp, reakc)  in enumerate(zip(list, list2)):
        print(fmt.format(i, disp, reakc))
    
    apzimejumi = ['W – izšķīdinātās vielas masas daļa, %', 'm – vielas masa, g', 'C – vielas molārā koncentrācija, mol/l', 'n – vielas daudzums, mol ', 'V – šķīduma tilpums, ml', 'ρ – šķīduma blīvums, g/ml', 'M – vielas molmasa, g/mol (atrodama ķīmisko elementu periodiskajā tabulā)', 'α – disociācijas pakāpe, %', 'n(kop) – izšķīdušās vielas kopējais daudzums, mol', 'v – reakcijas ātrums, mol/l*s', 'k – proporcionalitātes koeficents', 'c(A), c(B) – reaģējošo vielu koncentrācija', 'Δt – laika intervāls, s', 't1 – sākotnējā temperatūra', 't2 – paaugstinātā temperatūra']
        
    print("Apzīmējumu skaidrojumi: ")
    for apzimejumi in apzimejumi:
        print(apzimejumi)
elif a==2:
    class Jautajums:
        def __init__(self, jaut, atbilde):
            self.jaut = jaut
            self.atbilde = atbilde
    while True:
                
        temas = ['1 - dispersās sistēmas', '2 - atoma un vielas uzbūve', '3 - elektrolītiskā disociācija', '4 - oksidēšanās-reducēšanās procesi', '5 - ķīmisko procesu norise', '6 - ogļūdeņraži', '7 - spirti un aldehīdi', '8 - karbonskābes', '9 - dabasvielas', '10 - ķīmijas un vides tehnoloģijas sabiedrības ilgtspējīgā attīstībā']
        for temas in temas:
            print(temas)
        b=input("Par kuru no tēmām vēlies pārbaudīt zināšanas? Ievadi skaitli!")
        if b=="1":
            print("Tests par tēmu dispersās sistēmas.")
            
            question_prompts = [
                 "Šķīduma masa ir 500 g, MgCl masa šķīdumā ir 25 g. Aprēķini MgCl masas daļu šķīdumā!\na) 20%\nb) 50%\nc) 14%\nd) 5%\n",
                 "Kas ir migla?\na) Suspensija\nb) Aerosols\nc) Emulsija\nd) Kolodiāls šķīdums\n ",
                 "Kas ir piens?\na) Emulsija\nb) Kolodiāls šķīdums\nc) Suspensija\nd) Aerosols\n",
                 "Izšķīdušās vielas masas daļu NEizsaka ...?\na) promilēs\nb) molos\nc) procentos\nd) miljondaļās\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "d"),
                 Jautajums(question_prompts[1], "b"),
                 Jautajums(question_prompts[2], "a"),
                 Jautajums(question_prompts[3], "b"),
                 
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija d, b, a, c.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
            
        elif b=="2":
            
            print("Tests par tēmu atoma un vielas uzbūve.")
            
            question_prompts = [
                 "Cik protonu ir ķīmiskajam elementam vanādijam?\na) 22\nb) 23\nc) 11\nd) 285\n",
                 "Nepolāra kovalenta saite: \na) Veidojas starp elementu atomiem, kuru relatīvās elektronegativitātes krasi neatšķiras.\nb) Veidojas starp elementu atomiem, kuru relatīvās elektronegativitātes krasi atšķiras.\nc) Veidojas starp viena un tā paša ķīmiskā elementa atomiem.\nd) Visi iepriekš minētie.\n ",
                 "Cik elektronu ir ķīmiskajam elementam, kas atrodas 2. perioda IV A grupā?\na) 6\nb) 9\nc) 46\nd) 90\n",
                 "Cik elektronu ārējā enerģijas līmenī ir ķīmiskajam elementam, kas atrodas grupā VIII A?\na) 8\nb) 78\nc) 22\nd) 4\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "c"),
                 Jautajums(question_prompts[1], "c"),
                 Jautajums(question_prompts[2], "a"),
                 Jautajums(question_prompts[3], "a"),
                 
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija c, c, a, a.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
        
        elif b=="3":
            print("Tests par tēmu elektrolītiskā disociācija.")
            
            question_prompts = [
                 "Šķīdumā ir 1,9 mol Ba(NO3)2. Aprēķini, cik liels daudzums jonu ir šķīdumā, ja Ba(NO3)2 disociācijas pakāpe ir 0,76!\na) 4,32\nb) 2,51\nc) 2,53\nd) 4,92\n",
                 "Šķīduma pH ir 4,8. Kāda ir H+ un OH− jonu koncentrācija šķīdumā? \na) [H+]=10−4.8mol/l ; [OH−]=10−9.2mol/l\nb) b.	[H+]=10−4mol/l ; [OH−]=10−2mol/l\nc) c.	[H+]=10−7.3mol/l ; [OH−]=10−0.3mol/l\n ",
                 "Kāds ir kafijas aptuvenais pH\na) 2\nb) 16\nc) 5\nd) 9\n",
                 "Kura elektrolītiskās disociācijas definīcija ir pareizā?\na) Par elektrolītisko disociāciju sauc procesu, kurā sāļi ūdens šķīdumā sadalās pretēji lādētos jonos ar strāvas palīdzību.\nb) Par elektrolītisko disociāciju sauc procesu, kurā elektrolīti ūdens šķīdumā sadalās vienādi lādētos jonos.\nc) Par elektrolītisko disociāciju sauc procesu, kurā elektrolīti ūdens šķīdumā sadalās un veido jaunus savienojumos.\nd) Par elektrolītisko disociāciju sauc procesu, kurā elektrolīti ūdens šķīdumā sadalās pretēji lādētos jonos.\n",
                 "Kurš no doto savienojumu ūdens šķīdumiem vada elektrisko strāvu?\na) saharozes (cukura) 10% šķīdums\nb) nātrija hlorīda (vārāmā sāls) 5% šķīdums\nc) etilspirta 45% šķīdums\nd) etiķskābes 2% šķīdums (etiķis)\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "a"),
                 Jautajums(question_prompts[1], "a"),
                 Jautajums(question_prompts[2], "c"),
                 Jautajums(question_prompts[3], "d"),
                 Jautajums(question_prompts[4], "b"),
                 
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija a, a, c, d, b.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
            
        elif b=="4":
            print("Tests par tēmu oksidēšanās - reducēšanās procesi")
            question_prompts = [
                 "Ko parāda oksidēšanās pakāpe?\na) Tas ir vienkārši cipariņš, lai padarītu ķīmiju sarežģītāku.\nb) Oksidēšanās pakāpe parāda tikai to, cik elektronu ir pieņēmis vai zaudējis konkrētais elements.\nc) Cik molekulas jāņem no katras vielas.\n",
                 "Oksidētājs ir: \na) viela, kuras atomi oksidēšanās-reducēšanās reakcijas laikā pievieno sev elektronus.\nb) viela, kuras atomi oksidēšanās-reducēšanās reakcijas laikā nemaina savu elektronu skaitu.\nc) viela, kuras atomi oksidēšanās-reducēšanās reakcijas laikā atdod savus elektronus.\n ",
                 "Kurš no šiem pieder pie ātras oksidēšanās?\na) Rūsēšana\nb) Apsūbēšana\nc) Pūšana\nd) Degšana\n",
                 "Oksidēšanās-reducēšanās reakcija norisinās, ja:\na) reaģējošajām vielām mainās oksidēšanās pakāpes.\nb) reaģējošajām vielām nemainās oksidēšanās pakāpes.\nc) mainās reaģējošās vielas.\nd) mainās vielu koncentrācijas.\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "b"),
                 Jautajums(question_prompts[1], "a"),
                 Jautajums(question_prompts[2], "d"),
                 Jautajums(question_prompts[3], "a"),
                 
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija b, a, d, a.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
            
        elif b=="5":
            print("Tests par tēmu ķīmisko procesu norise")
            question_prompts = [
                 "Aprēķini ķīmiskās reakcijas ātrumu, ja izejvielas sākotnējā koncentrācija ir 8.6 mol/l, bet pēc 40 sekundēm tā ir 4.2 mol/l.\na) 0,15\nb) 0,11\nc) 1,10\nd) 0,41\n",
                 "Kāds likums nosaka reakcijas ātruma atkarību no reaģējošo vielu koncentrācijas?\na) Pirmais Ņūtona likums\nb) Oma likums. \nc) darbīgo (aktīvo) masu likums\nd) visi iepriekš minētie\n ",
                 "Aprēķini, cik reižu ir jāpalielina spiediens, lai reakcijā  2H2+O2⇄2H2O tiešās reakcijas ātrums palielinātos 125 reizes!\na) 5\nb) 125\nc) 4\nd) 78\n",
                 "Kas paātrina ķīmiskās reakcijas norisi?\na) Inhibitors.\nb) Lešateljē princips.\nc) Katalizators.\nd) Termoķīmiskie reakciju vienādojumi.\n",
                 "Aprēķini, cik reižu palielināsies ķīmiskās reakcijas ātrums, ja temperatūra paaugstināsies no 20°C līdz 90°C un reakcijas ātruma temperatūras koeficients ir 3!\na) 2021\nb) 2187\nc) 11\nd)14\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "b"),
                 Jautajums(question_prompts[1], "c"),
                 Jautajums(question_prompts[2], "a"),
                 Jautajums(question_prompts[3], "c"),
                 Jautajums(question_prompts[4], "b"),
                 
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija b, c, a, c, b.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
            
        elif b=="6":
            print("Tests par tēmu ogļūdeņraži.")
            question_prompts = [
                      "Kas ir alkāni?\na) Piesātinātie ogļūdeņraži, kuru molekulās ir tikai vienkāršās saites un kuru homologu rindas vispārīgā formula ir Cn H2n+2.\nb) Nepiesātinātie ogļūdeņraži, kuru molekulās ir viena divkāršā saite un kuru homologu rindas vispārīgā formula ir Cn H2n.\nc) Nepiesātinātie ogļūdeņraži, kuru molekulās ir viena trīskāršā saite un kuru homologu rindas vispārīgā formula ir Cn H2n–2.\n",
                      "Kas ir alkēni?\na) Piesātinātie ogļūdeņraži, kuru molekulās ir tikai vienkāršās saites un kuru homologu rindas vispārīgā formula ir Cn H2n+2.\nb) Nepiesātinātie ogļūdeņraži, kuru molekulās ir viena trīskāršā saite un kuru homologu rindas vispārīgā formula ir Cn H2n–2.\nc) Nepiesātinātie ogļūdeņraži, kuru molekulās ir viena trīskāršā saite un kuru homologu rindas vispārīgā formula ir Cn H2n.\n ",
                      "Kas ir arēni?\na) Ogļūdeņraži, kuru molekulās ir viens vai vairāki benzola gredzeni.\nb) Ķīmiskie savienojumi, kuru sastāvs ir vienāds, bet uzbūve un īpašības atšķiras.\nc) Alkāna atlikums, ko iegūst, no tā molekulformulas atņemot vienu ūdeņraža atomu.\n",
                      "Kāda ir butāna formula?\na) C5H12\nb) C4H10\nc) C6H14\n",
                 ]
            
            jautajumi = [
                      Jautajums(question_prompts[0], "a"),
                      Jautajums(question_prompts[1], "c"),
                      Jautajums(question_prompts[2], "a"),
                      Jautajums(question_prompts[3], "b"),     
                      
                 ]
                 
            def veikt_testu(jautajumi):
                    rezultats = 0
                    for jautajums in jautajumi:
                        atbilde = input(jautajums.jaut)
                        if atbilde == jautajums.atbilde:
                                rezultats += 1
                    print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija a, c, a, b.")
            veikt_testu(jautajumi) 
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
            
        elif b=="7":
            print("Tests par tēmu spirti un aldehīdi.")
            question_prompts = [
                 "Kas ir aldehīdi?\na) Noteikta atomu grupa, kas kopīga visai ķīmisko savienojumu klasei un nosaka šīs klases savienojumu raksturīgās īpašības.\nb) Organiskie savienojumi, kuru molekulās ir funkcionālā grupa –CHO.\nc) Mijiedarbības spēki, kuru rezultātā ar stipri elektronegatīva elementa atomu saistīts ūdeņraža atoms pievelkas ar citas vai tās pašas molekulas F, O vai N atomu.\n",
                 "Kas ir spirti? \na) Ogļūdeņražu atvasinājumi, kuros viens vai vairāki ūdeņraža atomi ir aizvietoti ar hidroksilgrupu (−OH).\nb) Ķīmiskie savienojumi, kas sastāv no metāliskiem elementiem un skābju atlikumiem. \nc) Organiskie savienojumi, kuru molekulās ir funkcionālā grupa –CHO.\n ",
                 "Kas ir funkcionālā grupa?\na) Noteikta atomu grupa, kas kopīga visai ķīmisko savienojumu klasei un nosaka šīs klases savienojumu raksturīgās īpašības.\nb) Organiskie savienojumi, kuros viens vai vairāki ūdeņraža atomi aizvietoti ar hidroksilgrupām.\nc) Mijiedarbības spēki, kuru rezultātā ar stipri elektronegatīva elementa atomu saistīts ūdeņraža atoms pievelkas ar citas vai tās pašas molekulas F, O vai N atomu.\n",
                 "Kas ir ūdeņraža saite? \na) Noteikta atomu grupa, kas kopīga visai ķīmisko savienojumu klasei un nosaka šīs klases savienojumu raksturīgās īpašības.\nb) Saite starp metālu un nemetālu atomiem.\nc) Mijiedarbības spēki, kuru rezultātā ar stipri elektronegatīva elementa atomu saistīts ūdeņraža atoms pievelkas ar citas vai tās pašas molekulas F, O vai N atomu.\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "b"),
                 Jautajums(question_prompts[1], "a"),
                 Jautajums(question_prompts[2], "a"),
                 Jautajums(question_prompts[3], "c"),
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija b, a, a, c.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
            
        elif b=="8":
            print("Tests par tēmu karbonskābes un to atvasinājumi.")
            question_prompts = [
                 "Kas ir aminoskābes?\na) Organiskie savienojumi, kuru molekulās ogļūdeņraža atlikumā viens vai vairāki ūdeņraža atomi ir aizvietoti ar aminogrupu.\nb) Ogļūdeņražu atvasinājumi, kuru molekulās ogļūdeņraža atlikums ir saistīts ar funkcionālo grupu – karboksilgrupu.\nc) Organiskas vielas, kas rodas skābju un spirtu reakcijās.\n",
                 "Kas ir ogļūdeņražu karboksilatvasinājumi? \na) Organiskie savienojumi, kuru molekulās ogļūdeņraža atlikumā viens vai vairāki ūdeņraža atomi ir aizvietoti ar aminogrupu.\nb) Ogļūdeņražu atvasinājumi, kuru molekulās ogļūdeņraža atlikums ir saistīts ar funkcionālo grupu – karboksilgrupu.\nc) Ķīmiskā reakcija, kurā skābe reaģē ar spirtu.\n ",
                 "Kā iedalās aizvietotās karbonskābes?\na) Halogēnkarbonskābes, hidroksikarbonskābes un aminoskābes.\nb) Hidroksikarbonskābes, aminoskābes un esteri.\nc) Esteri, halogēnkarbonskābes un hidroksikarbonskābes.\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "a"),
                 Jautajums(question_prompts[1], "b"),
                 Jautajums(question_prompts[2], "a"),
                 
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija a, b, a.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
            
        elif b=="9":
            print("Tests par tēmu dabasvielas.")
            question_prompts = [
                 "Kas ir ogļhidrāti?\na) Dabiskie lielmolekulārie savienojumi – polimēri, kuru monomēri ir aminoskābes.\nb) Glicerīna (trīsvērtīgā spirta) un augstāko karbonskābju jeb taukskābju esteri (triglicerīdi).\nc) Organiski savienojumi, kurus veido ogleklis, ūdeņradis un skābeklis. Tie var būt gan monosaharīdi (monomēri), gan disaharīdi, gan polisaharīdi (polimēri).\n",
                 "Kas ir olbaltumvielas? \na) Dabiskie lielmolekulārie savienojumi – polimēri, kuru monomēri ir aminoskābes.\nb) Glicerīna (trīsvērtīgā spirta) un augstāko karbonskābju jeb taukskābju esteri (triglicerīdi).\nc) Organiski savienojumi, kurus veido ogleklis, ūdeņradis un skābeklis. Tie var būt gan monosaharīdi (monomēri), gan disaharīdi, gan polisaharīdi (polimēri).\n ",
                 "Kas ir enzīmi?\na) Dabiski katalizatori. Olbaltumvielas, kuras paātrina vielmaiņas reakcijas.\nb) Karbonskābes, kuras ietilpst tauku sastāvā.\nc) Dabiskie polimēri, kuru monomēri ir nukleotīdi.\n",
                 "Kas ir dabasvielu hidrolīze? \na) Ķīmiskā saite, kas saista aminoskābju atlikumus olbaltumvielās.\nb) Dabasvielu reakcija ar ūdeni noteiktos apstākļos, kuras rezultātā rodas katram dabiskajam polimēram raksturīgie monomēri.\nc) Olbaltumvielu telpiskās struktūras izmaiņas ārējo apstākļu ietekmē, kā rezultātā tās zaudē bioloģisko aktivitāti.\n",
                 "Kas ir nukleotīds? \na) Viela, kuras molekulas sastāv no diviem vai vairākiem aminoskābju atlikumiem, kuri savā starpā saistīti ar peptīdsaitēm. \nb) Nukleīnskābes monomērs, kas sastāv no savstarpēji kovalenti saistītas slāpekļa bāzes (adenīna, guanīna, citozīna vai timīna/uracila), ogļhidrāta (dezoksiribozes/ ribozes) un ortofosforskābes atlikuma. \nc) Organiski savienojumi, kurus veido ogleklis, ūdeņradis un skābeklis. Tie var būt gan monosaharīdi (monomēri), gan disaharīdi, gan polisaharīdi (polimēri).\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "c"),
                 Jautajums(question_prompts[1], "a"),
                 Jautajums(question_prompts[2], "a"),
                 Jautajums(question_prompts[3], "b"),
                 Jautajums(question_prompts[4], "b"),     
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija c, a, a, b, b.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break            
            
        elif b=="10":
            print("Tests par tēmu ķīmijas un vides tehnoloģijas sabiedrības ilgtspējīgā attīstībā.")
            question_prompts = [
                 "Kas ir biorafinēšana? \na) Efektīva biomasas izmantošana, ar daudzveidīgām tehnoloģijām pārvēršot to vērtīgos savienojumos, lai maksimāli aizstātu naftas pārstrādes produktus ar tādiem pašiem produktiem, iegūtiem no biomasas.\nb) Vides, ekonomiskā, sociālā attīstība, kas nodrošinašodienas vajadzību apmierināšanu, neradot draudus nākamo paaudžu vajadzību apmierināšanai.\nc) Zinātnes un tehnikas nozare, kas pētī iespējas, kā bioloģiskos procesus izmantot rūpnieciskos nolūkos,lai iegūtu cilvēkiem nepieciešamus produktus.\n",
                 "Kas nodrošina skābekļa atjaunošanos gaisā un ogļskābās gāzes saistīšanu?\na) Erozija\nb) Fotosintēze\nc) Transpirācija\n ",
                 "Kurš no šiem apgalvojumiem ir patiess?:\na) Melnajā konteinerā met bīstamos atkritumus.\nb) Zilajā konteinerā met papīru.\nc) Zaļajā konteinerā met papīru.\n",
                 "Nafta ir:\na) dažādas neorganiskās skābes.\nb) melnās silikātsmiltis.\nc) dažādu ogļūdeņražu maisījums.\n",
            ]
            
            jautajumi = [
                 Jautajums(question_prompts[0], "a"),
                 Jautajums(question_prompts[1], "b"),
                 Jautajums(question_prompts[2], "b"),
                 Jautajums(question_prompts[3], "c"),
                 
            ]
            
            def veikt_testu(jautajumi):
                rezultats = 0
                for jautajums in jautajumi:
                    atbilde = input(jautajums.jaut)
                    if atbilde == jautajums.atbilde:
                        rezultats += 1
                print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija a, b, b, c.")
            
            veikt_testu(jautajumi)
            atpakal=input("Ja vēlies mēģināt vēlreiz, ievadi 1, ja vēlies atgriezties pie tēmu saraksta ievadi 2.\n")
            if atpakal=="2":
                continue
            else:
                break  
