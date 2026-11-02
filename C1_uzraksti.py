# ----------------------------------------------------------------------
# C1. Python — rīks ar servisa nosaukumu
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram servisa nosaukumu padod kā argumentu komandrindā. Skripts izvada, cik šim servisam žurnālā ir ERROR rindu, un parāda pirmās divas no tām. Ja arguments nav padots, skripts izvada pamācību un neavarē.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Mainīgo, kurā glabā atrastās rindas, nosauc ar vārdu rezultati.
import sys
serviss = sys.argv[1]
rezultati=[]
with open("sistema.log") as fails:
    for rinda in fails:
        if serviss in rinda and "ERROR" in rinda:
            rezultati.append(rinda)
print("ERROR rindu skaits:", len(rezultati))
for space in rezultati[:2]:
    print(space)

     
