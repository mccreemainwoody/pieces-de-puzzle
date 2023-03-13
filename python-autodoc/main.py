import docxtpl
import re
import os


def main():
    chemin = "C:\\Users\\metzc\\Perso\\Cours\\Stages - Alternance\\Alternance 1 - x\\"
    nom_dossier_sauvegarde = "lettres"

    doc = docxtpl.DocxTemplate(os.path.join(chemin, "lettre-de-motivation-1.docx"))
    with open(os.path.join(chemin, "entr-cand-spont-classement-par-zones.txt"), "r", encoding='utf-8') as f:
        entreprises = [entreprise.replace("\n", "").split(" - ", 1)
                       for entreprise in f.readlines() if re.match(r"^\D+ - ", entreprise)]

    if not os.path.exists(os.path.join(chemin, nom_dossier_sauvegarde)):
        os.mkdir(os.path.join(chemin, nom_dossier_sauvegarde))
    chemin = os.path.join(chemin, nom_dossier_sauvegarde)
    for entreprise in [k for k in entreprises if len(k) > 1]:
        doc.render({
            'nom_entreprise': entreprise[0].upper(),
            'adresse': entreprise[1],
        })
        doc.save(os.path.join(f"{chemin}", f"lettre-de-motivation-{entreprise[0].replace(' ', '-').lower()}.docx"))


if __name__ == '__main__':
    main()
