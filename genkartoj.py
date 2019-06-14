#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, math, random

pagxekajxo = """\n\n \\pagebreak \n\n"""
pagxinterajxo = """\n\n\n"""

karto = """
        \\begin{{tikzpicture}}
        \\cardbackground{{{0}}}{{{1}}}
        \\cardtitle{{{2}}}
        \\cardcontent{{{3}}}
        \\cardborder  {4}
        \\mangxkvanto{{{5}}}
        \\end{{tikzpicture}}"""

dekstra = "\n\\fill (5.7,.33) -- (5.7,2.33) -- (6,1.33) -- cycle;"
maldekstra = "\\fill (.4,.33) -- (.4,2.33) -- (.1,1.33) -- cycle;\n"

def makeKart(jsEl):
    image, bgcolor, title, cont, mangxkvanto = jsEl["img"], jsEl["koloro"], \
                                  jsEl["title"], jsEl["teksto"], jsEl["mangxkvanto"]
    arrows = ""
    if jsEl["dekstra"]    : arrows += dekstra
    if jsEl["maldekstra"] : arrows += maldekstra
    return karto.format(image, bgcolor, title, cont, arrows, mangxkvanto)

cards = open("kartaro.json").read()
kartoj = json.loads(cards)
ludo = ". \n\n \\vspace{.95cm}\n\n"
c=0
for kart in kartoj:
    mangxkvantvaloroj = [int(key) for key in kart["mangxkvantoj"] for i in range(kart["mangxkvantoj"][key])]
    for j in range(kart["kvanto"]):
        kart["mangxkvanto"] = mangxkvantvaloroj[j]
        if c%9==0 and c!=0:
            ludo += pagxekajxo
        elif c%3==0 or c%6==0 and c!=0:
            ludo += pagxinterajxo
        ludo += makeKart(kart)
        c+=1
open("kartaro.tex","w").write(ludo)
