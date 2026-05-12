const phrases = {
            "soft": {
                        "tribunal": [
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
                        ],
                        "draft": [
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
                        ],
                        "prefere": [
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
                        ],
                        "daube": [
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
                        ],
                        "redflag": [
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
                        ],
                        "boire_susceptible": [
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
                        ],
                        "boire_jamais": [
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
                        ],
                        "boire_action": [
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
                        ],
                        "boire_dictateur": [
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
                        ],
                        "boire_serieux": [
                                    "Blague : 'Quelle est la différence entre les oiseaux et les banquiers ? Les oiseaux plumés ne volent plus.' (Ne ris pas)",
                                    "Blague : 'Que dit un aveugle quand on lui donne du papier de verre ? Putain c'est écrit petit.' (Ne ris pas)",
                                    "Blague : 'C'est l'histoire d'un pingouin qui respire par le cul. Un jour il s'assoit, et il meurt.' (Ne ris pas)",
                                    "Blague : 'Comment appelle-t-on un chien sans patte ? On ne l'appelle pas, on va le chercher.' (Ne ris pas)",
                                    "Blague : 'Quel est le point commun entre un parachute et l'humour ? Quand tu n'en as pas, tu t'écrases.' (Ne ris pas)"
                        ],
                        "boire_7sec": [
                                    "Tu as 7 secondes pour citer 3 pires endroits pour rompre.",
                                    "Tu as 7 secondes pour citer 3 animaux qui ont l'air cons.",
                                    "Tu as 7 secondes pour citer 3 choses à faire avec un cadavre.",
                                    "Tu as 7 secondes pour citer 3 mots qui commencent par 'Z'.",
                                    "Tu as 7 secondes pour citer 3 choses qu'il ne faut pas mettre au micro-ondes."
                        ],
                        "boire_roulette": [
                                    "Roulette : Le joueur le plus jeune boit 2 gorgées.",
                                    "Roulette : Tous ceux qui ont un vêtement noir boivent 1 gorgée.",
                                    "Roulette : Le joueur avec le plus de batterie distribue 3 gorgées.",
                                    "Roulette : Tous les célibataires boivent 2 gorgées. S'il n'y en a pas, tout le monde boit.",
                                    "Roulette : Le dernier à toucher le sol avec sa main boit 2 gorgées."
                        ],
                        "boire_menteur": [
                                    "Vrai ou Faux : Les cochons peuvent manger un corps humain entier (os compris). (Vrai)",
                                    "Vrai ou Faux : On avale en moyenne 8 araignées par an en dormant. (Faux, légende)",
                                    "Vrai ou Faux : Les loutres de mer se tiennent la main en dormant. (Vrai)",
                                    "Vrai ou Faux : Hitler a été nominé pour le prix Nobel de la paix. (Vrai)",
                                    "Vrai ou Faux : Le miel est du vomi d'abeille. (Vrai)"
                        ],
                        "boire_kamikaze": [
                                    "Kamikaze : Thème 'Animaux'. Le 1er qui se trompe boit 3 gorgées.",
                                    "Kamikaze : Thème 'Insultes douces'. Le 1er qui se trompe boit 3 gorgées.",
                                    "Kamikaze : Thème 'Légumes'. Le 1er qui se trompe boit 3 gorgées.",
                                    "Kamikaze : Thème 'Maladies mortelles'. Le 1er qui se trompe boit 3 gorgées.",
                                    "Kamikaze : Thème 'Prénoms de beaufs'. Le 1er qui se trompe boit 3 gorgées."
                        ],
                        "boire_dilemme": [
                                    "Tu préfères : Ne plus avoir de dents OU ne plus avoir de nez ?",
                                    "Tu préfères : Savoir QUAND tu vas mourir OU COMMENT tu vas mourir ?",
                                    "Tu préfères : Manger du caca goût chocolat OU du chocolat goût caca ?",
                                    "Tu préfères : Toujours dire à voix haute ce que tu penses OU devenir muet ?",
                                    "Tu préfères : Trouver un poil dans tous tes plats OU boire toujours de l'eau tiède ?"
                        ]
            },
            "hard": {
                        "tribunal": [
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
                        ],
                        "draft": [
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
                        ],
                        "prefere": [
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
                        ],
                        "daube": [
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
                        ],
                        "redflag": [
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
                        ],
                        "boire_susceptible": [
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
                        ],
                        "boire_jamais": [
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
                        ],
                        "boire_action": [
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
                        ],
                        "boire_dictateur": [
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
                        ],
                        "boire_serieux": [
                                    "Blague : 'Quelle est la différence entre le sexe anal et le sexe oral ? Le goût.' (Ne ris pas, sinon bois 2 gorgées)",
                                    "Blague : 'Quel est le point commun entre un gynécologue et un livreur de pizza ? Ils peuvent le sentir, mais pas le manger.'",
                                    "Blague : 'Comment s'appelle le bout de peau inutile à l'extrémité du pénis ? L'homme.'",
                                    "Blague : 'Quelle est la différence entre un thermomètre buccal et un thermomètre rectal ? Le goût.'",
                                    "Blague : 'Que fait un spermatozoïde en costume ? Il va à une érection syndicale.'"
                        ],
                        "boire_7sec": [
                                    "Tu as 7 secondes pour citer 3 synonymes vulgaires de l'acte sexuel.",
                                    "Tu as 7 secondes pour citer 3 positions sexuelles.",
                                    "Tu as 7 secondes pour citer 3 objets insolites qu'on peut utiliser comme sex-toy.",
                                    "Tu as 7 secondes pour citer 3 mots que tu aimes entendre au lit.",
                                    "Tu as 7 secondes pour citer 3 IST (infections sexuellement transmissibles)."
                        ],
                        "boire_roulette": [
                                    "Roulette : Ceux qui ont déjà envoyé des nudes boivent 2 gorgées.",
                                    "Roulette : Le/la plus pervers(e) du groupe (désigné à l'unanimité) boit 3 gorgées.",
                                    "Roulette : Ceux qui n'ont pas eu de rapport sexuel depuis plus d'un mois boivent 3 gorgées.",
                                    "Roulette : Ceux qui ont déjà trompé boivent cul sec (soyez honnêtes).",
                                    "Roulette : La personne avec le plus gros 'body count' distribue 4 gorgées."
                        ],
                        "boire_menteur": [
                                    "Vrai ou Faux : Cléopâtre a inventé le premier vibromasseur en utilisant une gourde remplie d'abeilles vivantes. (Vrai)",
                                    "Vrai ou Faux : Le clitoris contient plus de 8000 terminaisons nerveuses. (Vrai)",
                                    "Vrai ou Faux : Il est médicalement impossible de se fracturer le pénis. (Faux, c'est possible et horrible)",
                                    "Vrai ou Faux : Les bonobos résolvent 90% de leurs conflits par des actes sexuels. (Vrai)",
                                    "Vrai ou Faux : Le sperme est excellent pour la peau car il contient du zinc et des vitamines C. (Vrai)"
                        ],
                        "boire_kamikaze": [
                                    "Kamikaze : Thème 'Positions sexuelles'. Le 1er qui se trompe boit 3 gorgées.",
                                    "Kamikaze : Thème 'Noms de sex-toys'. Le 1er qui se trompe boit 3 gorgées.",
                                    "Kamikaze : Thème 'Synonymes de pénis'. Le 1er qui se trompe boit 3 gorgées.",
                                    "Kamikaze : Thème 'Lieux insolites pour faire l'amour'. Le 1er qui se trompe boit 3 gorgées.",
                                    "Kamikaze : Thème 'Actrices ou Acteurs X'. Le 1er qui se trompe boit 3 gorgées."
                        ],
                        "boire_dilemme": [
                                    "Tu préfères : Coucher avec le/la partenaire de ton meilleur ami OU que ton meilleur ami couche avec ton/ta partenaire ?",
                                    "Tu préfères : Avoir des dents à la place des poils pubiens OU des poils pubiens à la place des dents ?",
                                    "Tu préfères : Ne plus jamais pouvoir jouir de ta vie OU devoir crier à pleins poumons à chaque fois que tu jouis ?",
                                    "Tu préfères : Être surpris en train de te masturber par tes parents OU surprendre tes parents en train de faire l'amour ?",
                                    "Tu préfères : Ne pouvoir faire l'amour que dans l'obscurité totale pour le reste de ta vie OU devoir toujours le faire en plein jour en public ?"
                        ]
            }
};

        const gameTitles = {
            tribunal: "Tribunal des Opinions",
            draft: "Draft de l'Absurde",
            prefere: "Tu Préfères... de l'Extrême",
            daube: "Pitch de Daube",
            redflag: "C'est un 10, MAIS...",
            boire_susceptible: "Qui est le plus susceptible",
            boire_jamais: "Je n'ai jamais (Sombre)",
            boire_action: "Action ou Cul Sec",
            boire_dictateur: "Le Dictateur",
            boire_serieux: "Garde ton sérieux",
            boire_7sec: "7 Secondes de l'Enfer",
            boire_roulette: "La Roulette Russe",
            boire_menteur: "Menteur ou Psychopathe",
            boire_kamikaze: "Le Kamikaze",
            boire_dilemme: "Dilemme Mortel"
        };

        const shopItems = [
            // Soft / Amusants
            { name: "Choix de la playlist musicale (30 min)", cost: 10, type: "soft" },
            { name: "Surnom ridicule pour l'autre", cost: 10, type: "soft" },
            { name: "Répondre avec un accent au choix (10 min)", cost: 20, type: "soft" },
            { name: "Droit de veto absolu sur un vote", cost: 30, type: "soft" },
            { name: "Massage des épaules (10 min)", cost: 40, type: "soft" },
            { name: "Action Joker : Petite corvée à l'arrivée", cost: 50, type: "soft" },
            
            // Epicés (Tirés d'Amiocoin)
            { name: "Baiser où tu veux, quand tu veux", cost: 20, type: "spicy" },
            { name: "Manger qqch directement dans la bouche de l'autre", cost: 30, type: "spicy" },
            { name: "Toucher l'autre en public sans se faire capter", cost: 40, type: "spicy" },
            { name: "Droit à une sieste collée-serrée", cost: 50, type: "spicy" },
            { name: "Lancer de dé coquin (6 idées sexy)", cost: 60, type: "spicy" },
            { name: "Massage érotique à l’huile ce soir", cost: 80, type: "spicy" },
            { name: "Gage mystère à exécuter sans le savoir", cost: 100, type: "spicy" },
            { name: "Shooting photo sexy (privé)", cost: 120, type: "spicy" },
            { name: "Nuit de plaisir avec toutes les envies réalisées", cost: 150, type: "spicy" },
            { name: "Fantasme surprise réalisé sans tabou", cost: 200, type: "spicy" }
        ];


        let currentGame = '';
        let currentTheme = 'soft';
        let availableIndices = {};
        let players = [];
        let timerInterval;
        let isEcoMode = false;
        let audioCtx = null;

        // --- Moteur Audio Procédural ---
        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        let audioUnlocked = false;
        function unlockAudio() {
            if(audioUnlocked) return;
            initAudio();
            if(audioCtx) {
                const buffer = audioCtx.createBuffer(1, 1, 22050);
                const source = audioCtx.createBufferSource();
                source.buffer = buffer;
                source.connect(audioCtx.destination);
                source.start(0);
                audioCtx.resume().then(() => {
                    audioUnlocked = true;
                });
            }
            document.removeEventListener('touchstart', unlockAudio);
            document.removeEventListener('click', unlockAudio);
        }
        document.addEventListener('touchstart', unlockAudio, {once: true});
        document.addEventListener('click', unlockAudio, {once: true});

        function playSound(type) {
            if (!audioCtx) return;
            if (audioCtx.state === 'suspended') audioCtx.resume();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            
            const now = audioCtx.currentTime;
            if (type === 'coin') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(1000, now);
                osc.frequency.exponentialRampToValueAtTime(1500, now + 0.1);
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
                osc.start(now);
                osc.stop(now + 0.1);
            } else if (type === 'tick') {
                osc.type = 'square';
                osc.frequency.setValueAtTime(150, now);
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);
                osc.start(now);
                osc.stop(now + 0.05);
            } else if (type === 'alarm') {
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(300, now);
                osc.frequency.linearRampToValueAtTime(400, now + 0.2);
                gain.gain.setValueAtTime(0.4, now);
                gain.gain.linearRampToValueAtTime(0.01, now + 0.5);
                osc.start(now);
                osc.stop(now + 0.5);
            }
        }

        function triggerVibe(pattern) {
            if (navigator.vibrate) navigator.vibrate(pattern);
        }

        function toggleEcoMode() {
            isEcoMode = !isEcoMode;
            if(isEcoMode) document.body.classList.add('eco-mode');
            else document.body.classList.remove('eco-mode');
            triggerVibe(50);
        }

        // --- Quête du Jour ---
        const dailyQuests = [
            "Faites croire à un serveur/vendeur que c'est votre anniversaire de rencontre.",
            "Le premier à se plaindre d'avoir chaud ou d'avoir faim paie un verre.",
            "Réussir à placer le mot 'choucroute' dans une discussion avec un inconnu.",
            "Interdiction de regarder son téléphone pendant le repas. Le premier qui flanche paie l'addition.",
            "Inventez un nom de code pour désigner les personnes que vous trouvez moches dans la rue.",
            "Le perdant du prochain jeu devra porter le sac de l'autre pendant 1h."
        ];

        function checkDailyQuest() {
            const today = new Date().toDateString();
            const savedDate = localStorage.getItem('voyage_quest_date');
            let questIndex = localStorage.getItem('voyage_quest_index');
            
            if (savedDate !== today || questIndex === null) {
                questIndex = Math.floor(Math.random() * dailyQuests.length);
                localStorage.setItem('voyage_quest_date', today);
                localStorage.setItem('voyage_quest_index', questIndex);
            }
            
            document.getElementById('quest-text').innerText = dailyQuests[questIndex];
            document.getElementById('quest-banner').style.display = 'flex';
        }

        function initIndices() {
            availableIndices = {};
            for (let theme in phrases) {
                for (let key in phrases[theme]) {
                    availableIndices[theme + '_' + key] = Array.from({length: phrases[theme][key].length}, (_, i) => i);
                }
            }
            saveState();
        }

        function saveState() {
            localStorage.setItem('voyage_players', JSON.stringify(players));
            localStorage.setItem('voyage_availableIndices', JSON.stringify(availableIndices));
        }

        function loadState() {
            const savedVersion = localStorage.getItem('voyage_version');
            if (savedVersion !== 'v5_gigaupdate') {
                localStorage.clear();
                localStorage.setItem('voyage_version', 'v5_gigaupdate');
            }

            const savedPlayers = localStorage.getItem('voyage_players');
            if (savedPlayers) {
                players = JSON.parse(savedPlayers);
                // Patch pour l'inventaire
                players.forEach(p => { if(!p.inventory) p.inventory = []; });
            }

            const savedIndices = localStorage.getItem('voyage_availableIndices');
            if (savedIndices) {
                availableIndices = JSON.parse(savedIndices);
            } else {
                initIndices();
            }
            checkDailyQuest();
        }

        function resetMemory() {
            if(confirm("Veux-tu vraiment effacer tous les joueurs, l'inventaire et les coins ?")) {
                localStorage.removeItem('voyage_players');
                localStorage.removeItem('voyage_availableIndices');
                players = [];
                initIndices();
                alert("Mémoire effacée !");
            }
        }

        function handleEnter(event) {
            if (event.key === 'Enter') addPlayer();
        }

        function addPlayer() {
            const input = document.getElementById('player-input');
            const name = input.value.trim();
            if (name) {
                players.push({ name: name, score: 0, coins: 0, inventory: [] });
                input.value = '';
                saveState();
                renderPlayers();
                triggerVibe(50);
            }
        }

        function removePlayer(index) {
            players.splice(index, 1);
            saveState();
            renderPlayers();
            triggerVibe(50);
        }

        function renderPlayers() {
            const list = document.getElementById('players-list');
            list.innerHTML = '';
            players.forEach((p, index) => {
                list.innerHTML += `
                    <div class="player-item">
                        <span>${p.name} <small style="color:#ffd700">(${p.coins} 🪙)</small></span>
                        <button class="btn-remove" onclick="removePlayer(${index})">&times;</button>
                    </div>
                `;
            });
        }

        function switchView(fromId, toId, callback) {
            const fromView = document.getElementById(fromId);
            const toView = document.getElementById(toId);
            
            fromView.style.opacity = '0';
            fromView.style.transform = 'scale(0.9)';
            
            setTimeout(() => {
                fromView.style.display = 'none';
                toView.style.display = 'flex';
                
                if(callback) callback();
                
                setTimeout(() => {
                    toView.style.opacity = '1';
                    toView.style.transform = 'scale(1)';
                }, 50);
            }, 300);
        }

        function startGame(gameKey) {
            initAudio();
            triggerVibe(50);
            currentGame = gameKey;
            if (gameKey === 'chaos') {
                currentTheme = Math.random() > 0.5 ? 'soft' : 'hard';
                switchView('menu-view', 'players-setup-view', () => {
                    document.getElementById('player-input').focus();
                });
            } else {
                switchView('menu-view', 'theme-setup-view');
            }
        }

        function selectTheme(theme) {
            triggerVibe(50);
            currentTheme = theme;
            switchView('theme-setup-view', 'players-setup-view', () => {
                document.getElementById('player-input').focus();
            });
        }

        function returnToMenu(currentViewId) {
            triggerVibe(50);
            document.body.classList.remove('timer-flash');
            clearInterval(timerInterval);
            switchView(currentViewId, 'menu-view');
        }

        function beginGame() {
            triggerVibe([50, 50, 50]);
            players.forEach(p => p.score = 0); 
            
            switchView('players-setup-view', 'game-view', () => {
                const gameTitle = document.getElementById('game-title');
                
                if (currentGame === 'chaos') {
                    gameTitle.innerText = "Jeu Surprise ! 🌪️";
                    gameTitle.className = 'txt-boire';
                } else {
                    gameTitle.innerText = gameTitles[currentGame] + (currentTheme === 'hard' ? ' 🌶️' : '');
                    gameTitle.className = 'txt-' + currentGame.replace('boire_', 'boire'); 
                    if (currentGame.includes('boire')) gameTitle.className = 'txt-boire';
                    if (currentGame === 'tribunal') gameTitle.className = 'txt-tribunal';
                    if (currentGame === 'draft') gameTitle.className = 'txt-draft';
                    if (currentGame === 'prefere') gameTitle.className = 'txt-prefere';
                    if (currentGame === 'daube') gameTitle.className = 'txt-daube';
                    if (currentGame === 'redflag') gameTitle.className = 'txt-redflag';
                }
                
                updateScoreboard();
                renderVoteButtons();
                nextPhrase(true);
            });
        }

        // --- Chrono ---
        function startTimer() {
            triggerVibe(50);
            const display = document.getElementById('timer-display');
            const btn = document.getElementById('btn-timer-start');
            let timeLeft = 7;
            
            btn.style.display = 'none';
            display.innerText = timeLeft;
            display.classList.remove('timer-flash');
            document.body.classList.remove('timer-flash');

            clearInterval(timerInterval);
            timerInterval = setInterval(() => {
                timeLeft--;
                display.innerText = timeLeft;
                playSound('tick');
                if (timeLeft <= 3) triggerVibe(100);
                
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    display.innerText = "0 ! BOIS !";
                    document.body.classList.add('timer-flash');
                    display.classList.add('timer-flash');
                    btn.innerText = "Relancer ⏱️";
                    btn.style.display = 'block';
                    triggerVibe([200, 100, 200, 100, 200]);
                    playSound('alarm');
                }
            }, 1000);
        }

        // --- Inventaire & Boutique ---
        function openShop() {
            if(players.length === 0) {
                alert("Ajoutez d'abord des joueurs pour ouvrir la boutique !");
                return;
            }
            triggerVibe(50);
            switchView('menu-view', 'shop-view', () => {
                const select = document.getElementById('shop-player-select');
                select.innerHTML = players.map((p, i) => `<option value="${i}">${p.name}</option>`).join('');
                renderShopItems();
            });
        }

        function renderShopItems() {
            const select = document.getElementById('shop-player-select');
            const playerIndex = select.value;
            const player = players[playerIndex];
            
            document.getElementById('shop-balance').innerText = player.coins + " 🪙";
            
            const grid = document.getElementById('shop-grid');
            grid.innerHTML = shopItems.map((item, index) => {
                const canAfford = player.coins >= item.cost;
                return `
                    <div class="shop-item type-${item.type}">
                        <div class="shop-item-info">
                            <div class="shop-item-name">${item.name}</div>
                            <div class="shop-item-cost">${item.cost} 🪙</div>
                        </div>
                        <button class="btn-buy" onclick="buyItem(${index})" ${!canAfford ? 'disabled' : ''}>Acheter</button>
                    </div>
                `;
            }).join('');
        }

        function buyItem(itemIndex) {
            const select = document.getElementById('shop-player-select');
            const playerIndex = select.value;
            const player = players[playerIndex];
            const item = shopItems[itemIndex];
            
            if (player.coins >= item.cost) {
                player.coins -= item.cost;
                player.inventory.push(item.name);
                saveState();
                playSound('coin');
                triggerVibe([50, 50, 100]);
                alert(`🎁 Ajouté à l'inventaire de ${player.name} !`);
                renderShopItems();
            }
        }

        function openInventory() {
            if(players.length === 0) {
                alert("Aucun joueur n'est enregistré !");
                return;
            }
            triggerVibe(50);
            const playerNameSpan = document.getElementById('inv-player-name');
            const invList = document.getElementById('inventory-list');
            
            // On affiche le premier joueur par défaut, idéalement à améliorer avec un select
            let pIndex = 0; 
            const player = players[pIndex];
            playerNameSpan.innerText = player.name;
            
            if (player.inventory.length === 0) {
                invList.innerHTML = `<div style="color:white; opacity:0.6;">Inventaire vide.</div>`;
            } else {
                invList.innerHTML = player.inventory.map((itemName, idx) => `
                    <div class="inventory-item">
                        <span>${itemName}</span>
                        <button class="btn-action" style="padding: 5px 15px; font-size: 0.9rem;" onclick="useItem(${pIndex}, ${idx})">Utiliser</button>
                    </div>
                `).join('');
            }
            document.getElementById('inventory-modal').style.display = 'flex';
        }

        function useItem(pIndex, itemIdx) {
            triggerVibe(50);
            if (confirm("Veux-tu utiliser cet objet maintenant ? Il sera consommé.")) {
                players[pIndex].inventory.splice(itemIdx, 1);
                saveState();
                openInventory();
            }
        }

        function closeInventory() {
            triggerVibe(50);
            document.getElementById('inventory-modal').style.display = 'none';
        }

        // --- Roue de la Punition ---
        const punishments = [
            "Bois 3 gorgées 🍻", "Cul Sec ! 🍺", "Enlève un vêtement 🧦",
            "Masse les épaules d'un joueur (2min) 💆", "-50 BussCoins 🪙",
            "Mime ta position sexuelle 🛏️", "Donne 5 gorgées 🎯", "Révèle un secret 🤫",
            "Fais 10 pompes 💪", "Poste une story gênante 📱"
        ];
        function spinWheel() {
            triggerVibe(50);
            document.getElementById('wheel-modal').style.display = 'flex';
            document.getElementById('wheel-result').innerText = "Prêt à tourner ?";
            document.getElementById('btn-spin').style.display = 'inline-block';
        }
        function closeWheel() {
            triggerVibe(50);
            document.getElementById('wheel-modal').style.display = 'none';
        }
        function executeSpin() {
            const btn = document.getElementById('btn-spin');
            btn.style.display = 'none';
            const resultDiv = document.getElementById('wheel-result');
            let count = 0;
            let maxCount = 20 + Math.floor(Math.random() * 10);
            
            let spinInterval = setInterval(() => {
                resultDiv.innerText = punishments[count % punishments.length];
                triggerVibe(20);
                playSound('tick');
                count++;
                if (count > maxCount) {
                    clearInterval(spinInterval);
                    const finalResult = punishments[count % punishments.length];
                    resultDiv.innerText = `🎯 ${finalResult} !`;
                    triggerVibe([100, 50, 100]);
                    playSound('coin');
                }
            }, 100);
        }

        // --- Logique de Jeu ---
        function updateScoreboard() {
            const scoreboard = document.getElementById('scoreboard');
            if (players.length === 0) {
                scoreboard.style.display = 'none';
                return;
            }
            scoreboard.style.display = 'flex';
            scoreboard.innerHTML = players.map(p => `
                <div class="score-badge">
                    <span>${p.name}</span>
                    <span class="score-value">${p.score} pts</span>
                    <span class="coin-value">${p.coins} 🪙</span>
                </div>
            `).join('');
        }

        function renderVoteButtons() {
            const container = document.getElementById('vote-controls');
            if (players.length === 0) {
                container.innerHTML = `<button class="btn-action btn-next" onclick="nextPhrase()">Suivant</button>`;
                container.style.display = 'flex';
                return;
            }
            
            container.style.display = 'grid';
            let html = players.map((p, index) => `
                <button class="btn-vote" onclick="votePlayer(${index})">
                    <span>+1 Point pour ${p.name}</span>
                    <small>Gagne 10 🪙</small>
                </button>
            `).join('');
            
            html += `<button class="btn-vote btn-skip" onclick="nextPhrase()">Passer la manche</button>`;
            
            container.innerHTML = html;
        }

        function votePlayer(index) {
            triggerVibe(30);
            players[index].score += 1;
            players[index].coins += 10;
            saveState();
            updateScoreboard();
            nextPhrase();
        }

        function nextPhrase(isFirst = false) {
            triggerVibe(30);
            let activeGame = currentGame;
            let activeTheme = currentTheme;

            if (currentGame === 'chaos') {
                const keys = Object.keys(phrases['soft']);
                activeGame = keys[Math.floor(Math.random() * keys.length)];
                activeTheme = Math.random() > 0.5 ? 'soft' : 'hard';
                document.getElementById('game-title').innerText = `Chaos : ${gameTitles[activeGame]} ${activeTheme === 'hard' ? '🌶️' : ''}`;
            }

            const memKey = activeTheme + '_' + activeGame;
            let list = availableIndices[memKey];
            
            if (!list || list.length === 0) {
                list = Array.from({length: phrases[activeTheme][activeGame].length}, (_, i) => i);
                availableIndices[memKey] = list;
            }
            
            const randomIndexList = Math.floor(Math.random() * list.length);
            const phraseIndex = list.splice(randomIndexList, 1)[0];
            saveState();
            
            const textElement = document.getElementById('game-text');
            const cardElement = document.getElementById('game-card');

            // Timer display logic
            if (activeGame === 'boire_7sec') {
                document.getElementById('timer-container').style.display = 'flex';
                document.getElementById('timer-display').innerText = '7';
                document.getElementById('timer-display').classList.remove('timer-flash');
                document.getElementById('btn-timer-start').style.display = 'block';
                document.getElementById('btn-timer-start').innerText = 'Lancer le Chrono ⏱️';
                document.body.classList.remove('timer-flash');
                clearInterval(timerInterval);
            } else {
                document.getElementById('timer-container').style.display = 'none';
                document.body.classList.remove('timer-flash');
                clearInterval(timerInterval);
            }
            
            if (isFirst) {
                textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];
                textElement.className = 'text-pop-in';
            } else {
                textElement.className = 'text-pop-out';
                cardElement.style.transform = 'scale(0.98)';
                
                setTimeout(() => {
                    textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];
                    textElement.className = 'text-pop-in';
                    cardElement.style.transform = 'scale(1)';
                }, 250);
            }
        }

        // --- Swipe Events ---
        let touchStartX = 0;
        let touchEndX = 0;
        document.addEventListener('DOMContentLoaded', () => {
            loadState();
            
            const gameCard = document.getElementById('game-card');
            gameCard.addEventListener('touchstart', e => {
                touchStartX = e.changedTouches[0].screenX;
            }, {passive: true});
            
            gameCard.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                if (touchStartX - touchEndX > 50) {
                    // Swiped Left
                    nextPhrase();
                } else if (touchEndX - touchStartX > 50) {
                    // Swiped Right
                    nextPhrase();
                }
            }, {passive: true});
            
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.register('sw.js')
                .then(() => console.log('Service Worker Registered'));
            }
        });

// --- SUPABASE & MULTIJOUEUR ---
const SUPABASE_URL = 'https://pzdbkegmbxsvabkvffdi.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_esYFZqPxzRx24Wh_VrGFqQ_QybEoy_w';
let supabase = null;
let isPremium = localStorage.getItem('voyage_premium') === 'true';
let syncMode = localStorage.getItem('voyage_sync_mode'); // 'online' ou 'offline'

if (window.supabase) {
    supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
}

document.addEventListener('DOMContentLoaded', () => {
    // Le modal s'affiche à chaque lancement d'application comme demandé
    document.getElementById('sync-modal').style.display = 'flex';
});

function openSyncModal() {
    triggerVibe(50);
    document.getElementById('sync-modal').style.display = 'flex';
}

function chooseSync(mode) {
    syncMode = mode;
    localStorage.setItem('voyage_sync_mode', mode);
    document.getElementById('sync-modal').style.display = 'none';
    if(mode === 'online') {
        alert("Le multijoueur sera bientôt activé ! Pour l'instant, profitez de la sauvegarde en ligne.");
    }
}

// --- UGC (Proposer une phrase) ---
function openUGC() {
    triggerVibe(50);
    document.getElementById('ugc-modal').style.display = 'flex';
}

function closeUGC() {
    triggerVibe(50);
    document.getElementById('ugc-modal').style.display = 'none';
}

async function submitUGC() {
    triggerVibe(50);
    const theme = document.getElementById('ugc-theme').value;
    const game = document.getElementById('ugc-game').value;
    const text = document.getElementById('ugc-text').value.trim();
    const author = document.getElementById('ugc-author').value.trim() || 'Anonyme';

    if(!text) {
        alert("La phrase ne peut pas être vide !");
        return;
    }

    if (!supabase) {
        alert("Erreur de connexion à la base de données.");
        return;
    }

    try {
        const { error } = await supabase.from('pending_phrases').insert([
            { theme: theme, game_mode: game, content: text, submitted_by: author }
        ]);
        
        if (error) throw error;
        
        playSound('coin');
        alert("Merci ! Ta phrase a été envoyée et sera ajoutée après validation. 🚀");
        document.getElementById('ugc-text').value = '';
        closeUGC();
    } catch (e) {
        alert("Erreur lors de l'envoi. Vérifie ta connexion internet.");
        console.error(e);
    }
}

// --- FREEMIUM ---
function requirePremium(callback) {
    if (isPremium) {
        callback();
    } else {
        triggerVibe(50);
        document.getElementById('paywall-modal').style.display = 'flex';
    }
}

function closePaywall() {
    triggerVibe(50);
    document.getElementById('paywall-modal').style.display = 'none';
}

function simulatePurchase() {
    triggerVibe([50, 100, 50]);
    playSound('coin');
    isPremium = true;
    localStorage.setItem('voyage_premium', 'true');
    closePaywall();
    alert("🎉 Achat validé ! Vous avez maintenant accès à tout le contenu Premium.");
}

// Hook Premium into selectTheme and startGame
const originalSelectTheme = selectTheme;
selectTheme = function(theme) {
    if (theme === 'hard') {
        requirePremium(() => originalSelectTheme(theme));
    } else {
        originalSelectTheme(theme);
    }
};

const originalStartGame = startGame;
startGame = function(gameKey) {
    if (gameKey === 'chaos') {
        requirePremium(() => originalStartGame(gameKey));
    } else {
        originalStartGame(gameKey);
    }
};
