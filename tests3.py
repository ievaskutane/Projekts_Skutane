class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde

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
