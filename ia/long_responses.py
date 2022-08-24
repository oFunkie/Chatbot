import random
from urllib import response

R_EATING = "des pates carbo"
R_LOVE = "non, bizarre en plus..."
R_DO = "Rien... je te parle ^^"
R_SQUID_LOVE = "J'aime bien, j'étais sceptique au début, mais la série est géniale, la fin était triste." 
R_NAME = "Samantha"
R_BAISE = "Bah non mdr, cringe un peu..."
R_WHAT = "Un humain Pakistanais assis sur une chaise en train de disctuter sur coco.fr."
R_COLOR = "J'aime le noir, mais pas les noirs, paradoxal nan ?"
R_VACANCES = "on est dans le sud de la france, à coté de Marseille. Et vous ?"
R_VACANCESRES = "Oh c'est jolie là-bas :D"

R_OUT = "peux pas sorry"                     


def unknow():
    response = ["Je n'ai pas bien compris, peux-tu répéter ?",
                "... hein ?",
                "de quoi ?",
                "Reformule stp",
                "ça veut dire quoi ?"][random.randrange(4)]
    return response            