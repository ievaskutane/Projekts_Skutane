

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Šķīduma masa ir 500 g, MgCl masa šķīdumā ir 25 g. Aprēķini MgCl masas daļu šķīdumā!\na) 20%\nb) 50%\nc) 14%\nd) 5%\n",
     "Kas ir migla?\na) Suspensija\nb) Aerosols\nc) Emulsija\nd) Kolodiāls šķīdums\n ",
     "Kas ir piens?\na) Emulsija\nb) Kolodiāls šķīdums\nc) Suspensija\nd) Aerosols\n",
     "Izšķīdušās vielas masas daļu NEizsaka ...?\na) Promilēs\nb) Molos\nc) Procentos\nd) Miljondaļās\n",
]

jautajumi = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "a"),
     Question(question_prompts[3], "b"),
     
]

def veikt_testu(jautajumi):
     rezultats = 0
     for question in jautajumi:
          atbilde = input(question.prompt)
          if atbilde == question.answer:
               rezultats += 1
     print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem.")

veikt_testu(jautajumi)


