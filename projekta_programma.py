a=int(input("Ko vēlies darīt? Ievadi 1, ja vēlies izpētīt formulu apkopojumu.\
Ievadi 2, ja vēlies izpildīt testu, lai pārbaudītu savas zināšanas."))
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
    
