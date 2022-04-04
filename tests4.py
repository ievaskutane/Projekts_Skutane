class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde
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