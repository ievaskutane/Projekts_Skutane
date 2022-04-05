class Jautajums:
     def __init__(self, jaut, atbilde):
          self.jaut = jaut
          self.atbilde = atbilde

question_prompts = [
     "Kas ir aminoskābes?\na) Organiskie savienojumi, kuru molekulās ogļūdeņraža atlikumā viens vai vairāki ūdeņraža atomi ir aizvietoti ar aminogrupu.\nb) Ogļūdeņražu atvasinājumi, kuru molekulās ogļūdeņraža atlikums ir saistīts ar funkcionālo grupu – karboksilgrupu.\nc) Organiskas vielas, kas rodas skābju un spirtu reakcijās.\n",
     "Kas ir ogļūdeņražu karboksilatvasinājumi? \na) Organiskie savienojumi, kuru molekulās ogļūdeņraža atlikumā viens vai vairāki ūdeņraža atomi ir aizvietoti ar aminogrupu.\nb) Ogļūdeņražu atvasinājumi, kuru molekulās ogļūdeņraža atlikums ir saistīts ar funkcionālo grupu – karboksilgrupu.\nc) Ķīmiskā reakcija, kurā skābe reaģē ar spirtu.\n ",
     "Kā iedalās aizvietotās karbonskābes?\na) Halogēnkarbonskābes, hidroksikarbonskābes un aminoskābes.\nb) Hidroksikarbonskābes, aminoskābes un esteri.\nc) Esteri, halogēnkarbonskābes un hidroksikarbonskābes.\n",
]

jautajumi = [
     Jautajums(question_prompts[0], "a"),
     Jautajums(question_prompts[1], "b"),
     Jautajums(question_prompts[2], "a"),
     
]

def veikt_testu(jautajumi):
     rezultats = 0
     for jautajums in jautajumi:
          atbilde = input(jautajums.jaut)
          if atbilde == jautajums.atbilde:
               rezultats += 1
     print("Tu pareizi atbildēji uz", rezultats, "no", len(jautajumi), "jautājumiem. Pareizās atbildes bija a, b, a.")

veikt_testu(jautajumi)