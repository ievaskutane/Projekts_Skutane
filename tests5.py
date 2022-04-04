class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde
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