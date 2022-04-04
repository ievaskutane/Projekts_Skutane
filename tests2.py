class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde

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
