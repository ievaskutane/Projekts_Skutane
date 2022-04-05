class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde
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
     
    

    

