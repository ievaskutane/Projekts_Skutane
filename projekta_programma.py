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