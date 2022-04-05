class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde

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