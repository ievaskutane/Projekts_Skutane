class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde

question_prompts = [
     "Kas ir ogļhidrāti?\na) Dabiskie lielmolekulārie savienojumi – polimēri, kuru monomēri ir aminoskābes.\nb) Glicerīna (trīsvērtīgā spirta) un augstāko karbonskābju jeb taukskābju esteri (triglicerīdi).\nc) Organiski savienojumi, kurus veido ogleklis, ūdeņradis un skābeklis. Tie var būt gan monosaharīdi (monomēri), gan disaharīdi, gan polisaharīdi (polimēri).\n",
     "Kas ir olbaltumvielas? \na) Dabiskie lielmolekulārie savienojumi – polimēri, kuru monomēri ir aminoskābes.\nb) Glicerīna (trīsvērtīgā spirta) un augstāko karbonskābju jeb taukskābju esteri (triglicerīdi).\nc) Organiski savienojumi, kurus veido ogleklis, ūdeņradis un skābeklis. Tie var būt gan monosaharīdi (monomēri), gan disaharīdi, gan polisaharīdi (polimēri).\n ",
     "Kas ir enzīmi?\na) Dabiski katalizatori. Olbaltumvielas, kuras paātrina vielmaiņas reakcijas.\nb) Karbonskābes, kuras ietilpst tauku sastāvā.\nc) Dabiskie polimēri, kuru monomēri ir nukleotīdi.\n",
     "Kas ir dabasvielu hidrolīze? \na) Ķīmiskā saite, kas saista aminoskābju atlikumus olbaltumvielās.\nb) Dabasvielu reakcija ar ūdeni noteiktos apstākļos, kuras rezultātā rodas katram dabiskajam polimēram raksturīgie monomēri.\nc) Olbaltumvielu telpiskās struktūras izmaiņas ārējo apstākļu ietekmē, kā rezultātā tās zaudē bioloģisko aktivitāti.\n",
     "Kas ir nukleotīds? \na) Viela, kuras molekulas sastāv no diviem vai vairākiem aminoskābju atlikumiem, kuri savā starpā saistīti ar peptīdsaitēm. \nb) Nukleīnskābes monomērs, kas sastāv no savstarpēji kovalenti saistītas slāpekļa bāzes (adenīna, guanīna, citozīna vai timīna/uracila), ogļhidrāta (dezoksiribozes/ ribozes) un ortofosforskābes atlikuma. \nc) Organiski savienojumi, kurus veido ogleklis, ūdeņradis un skābeklis. Tie var būt gan monosaharīdi (monomēri), gan disaharīdi, gan polisaharīdi (polimēri).\n",
]

jautajumi = [
     Jautajums(question_prompts[0], "c"),
     Jautajums(question_prompts[1], "a"),
     Jautajums(question_prompts[2], "a"),
     Jautajums(question_prompts[3], "b"),
     Jautajums(question_prompts[4], "b"),     
]

def veikt_testu(jautajumi):
     rezultats = 0
     for jautajums in jautajumi:
          atbilde = input(jautajums.jaut)
          if atbilde == jautajums.atbilde:
               rezultats += 1
     print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija c, a, a, b, b.")

veikt_testu(jautajumi)