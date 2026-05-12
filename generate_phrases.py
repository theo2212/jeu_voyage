import json
import re

soft_tribunal = [
    "L'ananas sur la pizza est le sommet de la gastronomie.",
    "Shrek 2 est meilleur que Le Parrain.",
    "Les notes vocales de plus d'une minute sont une insulte au respect humain.",
    "Mettre des chaussettes avec des sandales est un choix stylistique audacieux et valable.",
    "L'eau gazeuse a le goût de l'eau qui a été électrocutée, c'est dégueulasse.",
    "Dire 'je dis ça, je dis rien' mérite la prison ferme.",
    "Les bébés sont tous moches à la naissance, sans exception.",
    "Astérix Mission Cléopâtre est le seul bon film comique français.",
    "Les influenceurs ne sont que des panneaux publicitaires ambulants.",
    "Le vin rouge, c'est du jus de raisin qui a mal tourné.",
    "Le fromage bleu, c'est littéralement de la moisissure, arrêtez de faire genre c'est bon.",
    "Mettre un point à la fin d'un SMS est une agression passive."
]

hard_tribunal = [
    "La taille compte, et ceux qui disent le contraire se mentent à eux-mêmes.",
    "Tromper son/sa partenaire une seule fois en soirée, c'est pas si grave si personne ne l'apprend.",
    "Faire l'amour dans le noir complet, c'est pour les coincés.",
    "Les plans à 3 finissent toujours par détruire la relation.",
    "Simuler au lit est parfois nécessaire pour sauver l'ego de l'autre.",
    "Avoir des fantasmes sur le/la partenaire d'un ami est totalement normal.",
    "Coucher le premier soir est la meilleure façon de savoir si ça vaut le coup de continuer.",
    "Payer pour du contenu sur OnlyFans est pathétique.",
    "Le porno déforme complètement la réalité et ruine la sexualité.",
    "Fouiller dans le téléphone de son partenaire, c'est légitime si on a un doute."
]

soft_draft = [
    "Pire phrase à dire lors d'un enterrement.",
    "Pire chose à trouver dans son hamburger.",
    "Pire super-pouvoir à avoir au quotidien.",
    "Pire endroit pour avoir une crise de diarrhée.",
    "Pire costume d'Halloween pour aller au bureau.",
    "Pire nom pour un chien de garde.",
    "Pire chose à dire juste après un baiser.",
    "Pire objet à utiliser comme arme de poing dans la rue.",
    "Pire talent inutile à montrer à Incroyable Talent.",
    "Pire excuse pour annuler un rencard à la dernière minute."
]

hard_draft = [
    "Pire phrase à dire juste avant de jouir.",
    "Pire endroit du corps où retrouver un poil inconnu.",
    "Pire objet à utiliser comme sex-toy improvisé.",
    "Pire prénom à hurler par erreur au lit.",
    "Pire chose à découvrir dans l'historique internet de son/sa partenaire.",
    "Pire endroit public pour essayer de faire l'amour discrètement.",
    "Pire chose à dire à ses beaux-parents en parlant de leur fille/fils.",
    "Pire excuse pour justifier une panne au lit.",
    "Pire message envoyé par erreur au mauvais groupe (famille/travail).",
    "Pire fétiche inavouable à découvrir chez quelqu'un d'autre."
]

soft_prefere = [
    "Tu préfères transpirer de la mayonnaise OU pleurer des larmes en sauce piquante ?",
    "Tu préfères avoir des bras à la place des jambes OU des jambes à la place des bras ?",
    "Tu préfères parler toutes les langues du monde mais bégayer constamment OU parler seulement ta langue mais avec une voix de robot ?",
    "Tu préfères avoir un nez en forme de pénis OU des oreilles en forme de vagin ?",
    "Tu préfères éternuer des confettis OU tousser des paillettes ?",
    "Tu préfères devoir manger un cafard vivant par jour OU manger une poignée de cheveux à chaque repas ?",
    "Tu préfères ne plus jamais utiliser de papier toilette OU ne plus jamais utiliser de brosse à dents ?",
    "Tu préfères avoir toujours la sensation qu'un insecte rampe sur toi OU toujours entendre un bourdonnement dans ton oreille ?",
    "Tu préfères être constamment humide OU être constamment collant ?",
    "Tu préfères revivre la pire journée de ta vie tous les lundis OU ne plus jamais ressentir de joie le week-end ?"
]

hard_prefere = [
    "Tu préfères surprendre tes parents en train de faire l'amour OU qu'ils te surprennent en train de faire l'amour ?",
    "Tu préfères coucher une fois avec ton/ta cousin(e) pour 100 000€ OU ne jamais le faire mais tout le monde croit que tu l'as fait ?",
    "Tu préfères ne plus jamais ressentir d'orgasme de ta vie OU ne plus jamais pouvoir te masturber ?",
    "Tu préfères avoir une sex-tape qui fuite au travail OU devant toute ta famille ?",
    "Tu préfères que ton historique internet soit lu à ton enterrement OU devoir le lire à voix haute devant tes parents demain ?",
    "Tu préfères coucher avec la personne la plus moche du monde mais tout le monde pense que c'était le/la plus beau/belle, OU l'inverse ?",
    "Tu préfères crier le nom de ton/ta pire ex au lit à chaque fois, OU que ton partenaire crie le nom de son ex ?",
    "Tu préfères n'avoir que des rapports qui durent 1 minute maximum OU des rapports qui durent minimum 3 heures sans pouvoir t'arrêter ?",
    "Tu préfères devoir toujours filmer tes ébats OU devoir toujours avoir un spectateur muet dans la pièce ?",
    "Tu préfères sucer un orteil sale OU te faire lécher l'aisselle quand tu as transpiré ?"
]

soft_daube = [
    "Un homme découvre que son chat est la réincarnation de sa belle-mère.",
    "Une application de rencontre où tu ne matches qu'avec des gens qui ont les mêmes maladies que toi.",
    "Un télé-crochet pour trouver le pire cuisinier du monde, le gagnant doit manger son plat.",
    "Un film d'horreur où le tueur attaque avec une cuillère, mais très lentement.",
    "Un super-héros dont le seul pouvoir est de rendre les gens légèrement inconfortables.",
    "Une télé-réalité où des politiciens doivent survivre au SMIC pendant 1 an.",
    "Un documentaire animalier sur les pigeons de Paris narré par un dépressif.",
    "Une série policière où l'inspecteur résout les crimes en goûtant la scène de crime.",
    "Un parc d'attractions sur le thème de la bureaucratie et de l'administration française.",
    "Un film d'action où le héros est asthmatique et oublie toujours sa ventoline."
]

hard_daube = [
    "Un documentaire en caméra cachée sur les fétiches les plus dégoûtants des gens normaux.",
    "Une télé-réalité où 10 célibataires doivent deviner qui parmi eux a la plus petite taille.",
    "Un thriller érotique où l'arme du crime est toujours un sex-toy insolite.",
    "Une comédie romantique où les deux protagonistes ont le syndrome de la Tourette, mais seulement pour des insultes sexuelles.",
    "Un film d'horreur où un esprit maléfique te force à envoyer des nudes à ta mère si tu t'endors.",
    "Une série dramatique sur le quotidien du modérateur qui doit vérifier tout le porno illégal du net.",
    "Un jeu télévisé où tu gagnes de l'argent seulement si tu arrives à simuler un orgasme convaincant devant tes beaux-parents.",
    "Une application de rencontre qui ne matche que les gens ayant le même MST.",
    "Un biopic sur l'inventeur de la première poupée gonflable réaliste.",
    "Un film post-apocalyptique où la monnaie d'échange n'est plus l'eau, mais les faveurs sexuelles."
]

soft_redflag = [
    "C'est un 10, mais il/elle tape avec deux doigts sur son clavier.",
    "C'est un 10, mais il/elle claque des lèvres en mangeant.",
    "C'est un 10, mais il/elle est incapable de lire l'heure sur une horloge à aiguilles.",
    "C'est un 10, mais il/elle porte des lunettes de soleil en boîte de nuit.",
    "C'est un 10, mais il/elle met du ketchup dans ses pâtes.",
    "C'est un 10, mais il/elle renifle tout le temps au lieu de se moucher.",
    "C'est un 10, mais il/elle ne sait pas nager.",
    "C'est un 10, mais il/elle a 30 ans et utilise encore le mot 'swag'.",
    "C'est un 10, mais il/elle croit dur comme fer que la Terre est plate.",
    "C'est un 10, mais il/elle fait des fautes d'orthographe à chaque phrase ('sa va')."
]

hard_redflag = [
    "C'est un 10, mais au lit, il/elle veut toujours que tu l'appelles 'papa' ou 'maman'.",
    "C'est un 10, mais il/elle refuse de te toucher si tu n'as pas pris 2 douches juste avant.",
    "C'est un 10, mais il/elle ne fait aucun bruit ni mouvement pendant l'acte, comme un cadavre.",
    "C'est un 10, mais il/elle a un album photo caché avec des photos de ses exs nus.",
    "C'est un 10, mais il/elle veut absolument filmer la première fois sans te demander.",
    "C'est un 10, mais il/elle refuse tout préliminaire, c'est directement l'action.",
    "C'est un 10, mais il/elle demande toujours de noter sa performance sur 10 juste après.",
    "C'est un 10, mais il/elle a un fétiche inavouable avec les pieds sales.",
    "C'est un 10, mais il/elle pleure systématiquement à la fin du rapport.",
    "C'est un 10, mais il/elle veut que tu portes un masque de politicien célèbre pendant."
]

soft_susceptible = [
    "Qui est le plus susceptible de survivre à une apocalypse zombie ?",
    "Qui est le plus susceptible de rater son propre mariage ?",
    "Qui est le plus susceptible de devenir fou en premier sur une île déserte ?",
    "Qui est le plus susceptible de se faire arnaquer sur Internet ?",
    "Qui est le plus susceptible de manger la nourriture d'un collègue dans le frigo ?",
    "Qui est le plus susceptible de s'endormir ivre dans les toilettes d'un bar ?",
    "Qui est le plus susceptible d'oublier l'anniversaire de son partenaire ?",
    "Qui est le plus susceptible de péter en public et d'accuser quelqu'un d'autre ?",
    "Qui est le plus susceptible de mourir bêtement en prenant un selfie ?",
    "Qui est le plus susceptible de mentir sur son CV et de se faire griller ?"
]

hard_susceptible = [
    "Qui est le plus susceptible de tromper son/sa partenaire sans aucun scrupule ?",
    "Qui est le plus susceptible d'envoyer des nudes à la mauvaise personne ?",
    "Qui est le plus susceptible de coucher avec l'ex d'un ami présent dans la pièce ?",
    "Qui est le plus susceptible d'avoir un compte caché sur un site X ?",
    "Qui est le plus susceptible de proposer un plan à 3 et d'être jaloux pendant ?",
    "Qui est le plus susceptible de coucher pour une promotion au travail ?",
    "Qui est le plus susceptible de fétichiser quelque chose de très bizarre ?",
    "Qui est le plus susceptible de contracter une MST lors de ces vacances ?",
    "Qui est le plus susceptible de simuler au lit régulièrement ?",
    "Qui est le plus susceptible de faire une sextape et de la 'perdre' volontairement ?"
]

soft_jamais = [
    "Je n'ai jamais fouillé le téléphone de mon partenaire.",
    "Je n'ai jamais menti pour éviter une soirée.",
    "Je n'ai jamais volé un petit objet dans un magasin.",
    "Je n'ai jamais vomi en public.",
    "Je n'ai jamais stalké un ex avec un faux compte.",
    "Je n'ai jamais fait pipi dans une piscine municipale.",
    "Je n'ai jamais utilisé la brosse à dents de quelqu'un d'autre sans lui dire.",
    "Je n'ai jamais renvoyé un plat au restaurant juste pour embêter le serveur.",
    "Je n'ai jamais pleuré pour manipuler une situation.",
    "Je n'ai jamais fait semblant d'être au téléphone pour ignorer quelqu'un."
]

hard_jamais = [
    "Je n'ai jamais fantasmé sur quelqu'un dans cette pièce.",
    "Je n'ai jamais eu de rapport sexuel dans un lieu public risqué.",
    "Je n'ai jamais simulé un orgasme pour que ça se termine plus vite.",
    "Je n'ai jamais eu envie d'essayer le bondage ou le BDSM.",
    "Je n'ai jamais couché le premier soir avec un inconnu total.",
    "Je n'ai jamais regretté amèrement la personne avec qui je me suis réveillé(e).",
    "Je n'ai jamais utilisé d'objet insolite (non prévu pour) comme sex-toy.",
    "Je n'ai jamais envoyé une photo de moi nu(e).",
    "Je n'ai jamais pensé à un(e) ex pendant que je faisais l'amour avec quelqu'un d'autre.",
    "Je n'ai jamais fait l'amour dans la chambre de mes parents."
]

soft_action = [
    "Action : Laisse le groupe regarder tes 5 dernières recherches Google, ou bois 3 gorgées.",
    "Action : Mime un singe enragé pendant 10 secondes, ou bois 2 gorgées.",
    "Action : Laisse un joueur envoyer un message au hasard à ton dernier contact, ou bois cul sec.",
    "Action : Fais un compliment gênant à ton voisin de droite, ou bois 2 gorgées.",
    "Action : Raconte la pire honte de ta vie, ou bois 4 gorgées.",
    "Action : Parle avec un accent québécois jusqu'à ton prochain tour, ou bois 3 gorgées.",
    "Action : Laisse le groupe choisir ta prochaine photo de profil pour 24h, ou bois cul sec.",
    "Action : Mange un bout de papier, ou bois 2 gorgées.",
    "Action : Fais 10 pompes, ou bois 3 gorgées.",
    "Action : Ne cligne pas des yeux pendant 30 secondes. Si tu perds, bois 2 gorgées."
]

hard_action = [
    "Action : Embrasse dans le cou la personne à ta gauche, ou bois 4 gorgées.",
    "Action : Laisse le groupe regarder tes photos 'Masquées' ou 'Privées', ou bois cul sec.",
    "Action : Mime ta position sexuelle préférée, ou bois 3 gorgées.",
    "Action : Lèche sensuellement l'oreille de ton voisin de droite, ou bois 4 gorgées.",
    "Action : Avoue quel est ton fantasme inavouable, ou bois 5 gorgées.",
    "Action : Fais un lap-dance à la personne en face de toi pendant 30 sec, ou bois cul sec.",
    "Action : Simule un orgasme très bruyant pendant 5 secondes, ou bois 4 gorgées.",
    "Action : Laisse un joueur écrire 'J'ai envie de toi' à un contact au hasard, ou bois cul sec.",
    "Action : Montre ton historique de navigation privée, ou bois 5 gorgées.",
    "Action : Enlève un vêtement (pas les chaussures), ou bois 3 gorgées."
]

soft_dictateur = [
    "Le Dictateur décide : Interdiction de dire 'Oui' ou 'Non'. Le premier qui le fait boit 2 gorgées.",
    "Le Dictateur décide : Tu dois vouvoyer tout le monde. Si tu tutoies, tu bois.",
    "Le Dictateur décide : Choisis un mot interdit. Celui qui le dit boit 2 gorgées.",
    "Le Dictateur décide : Interdiction de toucher son téléphone, sinon cul sec.",
    "Le Dictateur décide : À chaque fois qu'on te pose une question, réponds par une question, sinon bois.",
    "Le Dictateur décide : Interdiction de croiser les bras ou les jambes. Si pris en flag, 1 gorgée.",
    "Le Dictateur décide : Le joueur à ta gauche est ton esclave, il doit te servir tes verres.",
    "Le Dictateur décide : Tu ne peux plus pointer du doigt. Si tu le fais, tu bois.",
    "Le Dictateur décide : Interdiction d'utiliser des prénoms. Si tu le fais, tu bois.",
    "Le Dictateur décide : À chaque fois qu'un joueur rit, il boit 1 gorgée."
]

hard_dictateur = [
    "Le Dictateur décide : Chaque joueur doit boire son verre en gardant un contact visuel intense avec son voisin.",
    "Le Dictateur décide : Interdiction de porter des chaussettes. Tout le monde doit montrer ses pieds.",
    "Le Dictateur décide : Le joueur de ton choix devient ton soumis sexuel (virtuel). Il doit t'appeler 'Maître/Maîtresse'.",
    "Le Dictateur décide : À chaque gorgée bue, on doit lâcher un petit gémissement de plaisir.",
    "Le Dictateur décide : Tous ceux qui portent des sous-vêtements noirs boivent 2 gorgées.",
    "Le Dictateur décide : La personne à ta droite doit masser tes épaules pendant 2 minutes.",
    "Le Dictateur décide : Pose une question indiscrète au joueur de ton choix, il doit répondre ou boire cul sec.",
    "Le Dictateur décide : Deux joueurs de ton choix doivent s'échanger un vêtement.",
    "Le Dictateur décide : Choisis deux personnes qui ont l'interdiction de se parler. S'ils communiquent, ils boivent.",
    "Le Dictateur décide : Tu peux palper le torse/les pecs du joueur de ton choix pour 'vérifier' sa musculature."
]

soft_serieux = [
    "Blague : 'Quelle est la différence entre les oiseaux et les banquiers ? Les oiseaux plumés ne volent plus.' (Ne ris pas)",
    "Blague : 'Que dit un aveugle quand on lui donne du papier de verre ? Putain c'est écrit petit.' (Ne ris pas)",
    "Blague : 'C'est l'histoire d'un pingouin qui respire par le cul. Un jour il s'assoit, et il meurt.' (Ne ris pas)",
    "Blague : 'Comment appelle-t-on un chien sans patte ? On ne l'appelle pas, on va le chercher.' (Ne ris pas)",
    "Blague : 'Quel est le point commun entre un parachute et l'humour ? Quand tu n'en as pas, tu t'écrases.' (Ne ris pas)"
]

hard_serieux = [
    "Blague : 'Quelle est la différence entre le sexe anal et le sexe oral ? Le goût.' (Ne ris pas, sinon bois 2 gorgées)",
    "Blague : 'Quel est le point commun entre un gynécologue et un livreur de pizza ? Ils peuvent le sentir, mais pas le manger.'",
    "Blague : 'Comment s'appelle le bout de peau inutile à l'extrémité du pénis ? L'homme.'",
    "Blague : 'Quelle est la différence entre un thermomètre buccal et un thermomètre rectal ? Le goût.'",
    "Blague : 'Que fait un spermatozoïde en costume ? Il va à une érection syndicale.'"
]

soft_7sec = [
    "Tu as 7 secondes pour citer 3 pires endroits pour rompre.",
    "Tu as 7 secondes pour citer 3 animaux qui ont l'air cons.",
    "Tu as 7 secondes pour citer 3 choses à faire avec un cadavre.",
    "Tu as 7 secondes pour citer 3 mots qui commencent par 'Z'.",
    "Tu as 7 secondes pour citer 3 choses qu'il ne faut pas mettre au micro-ondes."
]

hard_7sec = [
    "Tu as 7 secondes pour citer 3 synonymes vulgaires de l'acte sexuel.",
    "Tu as 7 secondes pour citer 3 positions sexuelles.",
    "Tu as 7 secondes pour citer 3 objets insolites qu'on peut utiliser comme sex-toy.",
    "Tu as 7 secondes pour citer 3 mots que tu aimes entendre au lit.",
    "Tu as 7 secondes pour citer 3 IST (infections sexuellement transmissibles)."
]

soft_roulette = [
    "Roulette : Le joueur le plus jeune boit 2 gorgées.",
    "Roulette : Tous ceux qui ont un vêtement noir boivent 1 gorgée.",
    "Roulette : Le joueur avec le plus de batterie distribue 3 gorgées.",
    "Roulette : Tous les célibataires boivent 2 gorgées. S'il n'y en a pas, tout le monde boit.",
    "Roulette : Le dernier à toucher le sol avec sa main boit 2 gorgées."
]

hard_roulette = [
    "Roulette : Ceux qui ont déjà envoyé des nudes boivent 2 gorgées.",
    "Roulette : Le/la plus pervers(e) du groupe (désigné à l'unanimité) boit 3 gorgées.",
    "Roulette : Ceux qui n'ont pas eu de rapport sexuel depuis plus d'un mois boivent 3 gorgées.",
    "Roulette : Ceux qui ont déjà trompé boivent cul sec (soyez honnêtes).",
    "Roulette : La personne avec le plus gros 'body count' distribue 4 gorgées."
]

soft_menteur = [
    "Vrai ou Faux : Les cochons peuvent manger un corps humain entier (os compris). (Vrai)",
    "Vrai ou Faux : On avale en moyenne 8 araignées par an en dormant. (Faux, légende)",
    "Vrai ou Faux : Les loutres de mer se tiennent la main en dormant. (Vrai)",
    "Vrai ou Faux : Hitler a été nominé pour le prix Nobel de la paix. (Vrai)",
    "Vrai ou Faux : Le miel est du vomi d'abeille. (Vrai)"
]

hard_menteur = [
    "Vrai ou Faux : Cléopâtre a inventé le premier vibromasseur en utilisant une gourde remplie d'abeilles vivantes. (Vrai)",
    "Vrai ou Faux : Le clitoris contient plus de 8000 terminaisons nerveuses. (Vrai)",
    "Vrai ou Faux : Il est médicalement impossible de se fracturer le pénis. (Faux, c'est possible et horrible)",
    "Vrai ou Faux : Les bonobos résolvent 90% de leurs conflits par des actes sexuels. (Vrai)",
    "Vrai ou Faux : Le sperme est excellent pour la peau car il contient du zinc et des vitamines C. (Vrai)"
]

soft_kamikaze = [
    "Kamikaze : Thème 'Animaux'. Le 1er qui se trompe boit 3 gorgées.",
    "Kamikaze : Thème 'Insultes douces'. Le 1er qui se trompe boit 3 gorgées.",
    "Kamikaze : Thème 'Légumes'. Le 1er qui se trompe boit 3 gorgées.",
    "Kamikaze : Thème 'Maladies mortelles'. Le 1er qui se trompe boit 3 gorgées.",
    "Kamikaze : Thème 'Prénoms de beaufs'. Le 1er qui se trompe boit 3 gorgées."
]

hard_kamikaze = [
    "Kamikaze : Thème 'Positions sexuelles'. Le 1er qui se trompe boit 3 gorgées.",
    "Kamikaze : Thème 'Noms de sex-toys'. Le 1er qui se trompe boit 3 gorgées.",
    "Kamikaze : Thème 'Synonymes de pénis'. Le 1er qui se trompe boit 3 gorgées.",
    "Kamikaze : Thème 'Lieux insolites pour faire l'amour'. Le 1er qui se trompe boit 3 gorgées.",
    "Kamikaze : Thème 'Actrices ou Acteurs X'. Le 1er qui se trompe boit 3 gorgées."
]

soft_dilemme = [
    "Tu préfères : Ne plus avoir de dents OU ne plus avoir de nez ?",
    "Tu préfères : Savoir QUAND tu vas mourir OU COMMENT tu vas mourir ?",
    "Tu préfères : Manger du caca goût chocolat OU du chocolat goût caca ?",
    "Tu préfères : Toujours dire à voix haute ce que tu penses OU devenir muet ?",
    "Tu préfères : Trouver un poil dans tous tes plats OU boire toujours de l'eau tiède ?"
]

hard_dilemme = [
    "Tu préfères : Coucher avec le/la partenaire de ton meilleur ami OU que ton meilleur ami couche avec ton/ta partenaire ?",
    "Tu préfères : Avoir des dents à la place des poils pubiens OU des poils pubiens à la place des dents ?",
    "Tu préfères : Ne plus jamais pouvoir jouir de ta vie OU devoir crier à pleins poumons à chaque fois que tu jouis ?",
    "Tu préfères : Être surpris en train de te masturber par tes parents OU surprendre tes parents en train de faire l'amour ?",
    "Tu préfères : Ne pouvoir faire l'amour que dans l'obscurité totale pour le reste de ta vie OU devoir toujours le faire en plein jour en public ?"
]

phrases_obj = {
    "soft": {
        "tribunal": soft_tribunal, "draft": soft_draft, "prefere": soft_prefere, "daube": soft_daube, "redflag": soft_redflag,
        "boire_susceptible": soft_susceptible, "boire_jamais": soft_jamais, "boire_action": soft_action, "boire_dictateur": soft_dictateur,
        "boire_serieux": soft_serieux, "boire_7sec": soft_7sec, "boire_roulette": soft_roulette, "boire_menteur": soft_menteur,
        "boire_kamikaze": soft_kamikaze, "boire_dilemme": soft_dilemme
    },
    "hard": {
        "tribunal": hard_tribunal, "draft": hard_draft, "prefere": hard_prefere, "daube": hard_daube, "redflag": hard_redflag,
        "boire_susceptible": hard_susceptible, "boire_jamais": hard_jamais, "boire_action": hard_action, "boire_dictateur": hard_dictateur,
        "boire_serieux": hard_serieux, "boire_7sec": hard_7sec, "boire_roulette": hard_roulette, "boire_menteur": hard_menteur,
        "boire_kamikaze": hard_kamikaze, "boire_dilemme": hard_dilemme
    }
}

import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the phrases object
match = re.search(r'const phrases = \{.*?\n        \};\n', content, flags=re.DOTALL)

if match:
    new_phrases = "const phrases = " + json.dumps(phrases_obj, ensure_ascii=False, indent=12) + ";\n"
    content = content[:match.start()] + new_phrases + content[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully replaced phrases object")
else:
    print("Could not find phrases object in index.html")
