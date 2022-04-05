class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde

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