import os, sys, json, shutil

block_types = {}

with open("./data/en_us.json","r",encoding="utf-8") as lang_f:
    lang_c = json.loads(lang_f.read())
    lang_f.close()

def addModel(file,m_css):
    with open(os.path.join("./data/assets/minecraft/models/block/",file), "r") as mdl_f:
        mdl_c = json.loads(mdl_f.read())
        mdl_f.close()
    
    match(mdl_c["parent"]):
        case "minecraft:block/cube":
            try:
                block_types[str(file).replace(".json","")] = {
                    "name": lang_c["block.minecraft." + str(file).replace(".json","")]
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face:is(.bottom) {
  background-image: url(""" + str(mdl_c["textures"]["down"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.left) {
  background-image: url(""" + str(mdl_c["textures"]["east"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.front) {
  background-image: url(""" + str(mdl_c["textures"]["north"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.back) {
  background-image: url(""" + str(mdl_c["textures"]["south"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.top) {
  background-image: url(""" + str(mdl_c["textures"]["up"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.right) {
  background-image: url(""" + str(mdl_c["textures"]["west"]).replace("minecraft:","textures/") +""".png);
}""")
            except: # normally i wouldnt do this, but its for translation strings soooooooooo - jae
                block_types[str(file).replace(".json","")] = {
                    "name": "block.minecraft." + str(file).replace(".json","")
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face:is(.bottom) {
  background-image: url(""" + str(mdl_c["textures"]["down"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.left) {
  background-image: url(""" + str(mdl_c["textures"]["east"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.front) {
  background-image: url(""" + str(mdl_c["textures"]["north"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.back) {
  background-image: url(""" + str(mdl_c["textures"]["south"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.top) {
  background-image: url(""" + str(mdl_c["textures"]["up"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.right) {
  background-image: url(""" + str(mdl_c["textures"]["west"]).replace("minecraft:","textures/") +""".png);
}""")

        case "minecraft:block/cross":
            try:
                block_types[str(file).replace(".json","")] = {
                    "name": lang_c["block.minecraft." + str(file).replace(".json","")],
                    "shape": "cutout"
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face {
  background-image: url(""" + str(mdl_c["textures"]["cross"]).replace("minecraft:","textures/") +""".png);
}""")
            except:
                block_types[str(file).replace(".json","")] = {
                    "name": "block.minecraft." + str(file).replace(".json",""),
                    "shape": "cutout"
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face {
  background-image: url(""" + str(mdl_c["textures"]["cross"]).replace("minecraft:","textures/") +""".png);
}""")

        case "minecraft:block/tinted_cross":
            try:
                block_types[str(file).replace(".json","")] = {
                    "name": lang_c["block.minecraft." + str(file).replace(".json","")],
                    "shape": "cutout"
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face {
  background-image: url(""" + str(mdl_c["textures"]["cross"]).replace("minecraft:","textures/") +""".png);
}""")
            except:
                block_types[str(file).replace(".json","")] = {
                    "name": "block.minecraft." + str(file).replace(".json",""),
                    "shape": "cutout"
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face {
  background-image: url(""" + str(mdl_c["textures"]["cross"]).replace("minecraft:","textures/") +""".png);
}""")

        case "minecraft:block/cube_column":
            try:
                block_types[str(file).replace(".json","")] = {
                    "name": lang_c["block.minecraft." + str(file).replace(".json","")]
                }
                # TODO: fortnite

                # .block.oak_log .face:is(.left, .right, .front, .back) {
                # background-image: url("textures/block/oak_log.png");
                # }

                # .block.oak_log .face:is(.top, .bottom) {
                # background-image: url("textures/block/oak_log_top.png");
                # }

                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face:is(.left, .right, .front, .back) {
  background-image: url(""" + str(mdl_c["textures"]["side"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.top, .bottom) {
  background-image: url(""" + str(mdl_c["textures"]["end"]).replace("minecraft:","textures/") +""".png);
}""")
            except:
                block_types[str(file).replace(".json","")] = {
                    "name": "block.minecraft." + str(file).replace(".json","")
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face:is(.left, .right, .front, .back) {
  background-image: url(""" + str(mdl_c["textures"]["side"]).replace("minecraft:","textures/") +""".png);
}
.block.""" + str(file).replace(".json","") + """ .face:is(.top, .bottom) {
  background-image: url(""" + str(mdl_c["textures"]["end"]).replace("minecraft:","textures/") +""".png);
}""")

        case "minecraft:block/cube_all":
            try:
                block_types[str(file).replace(".json","")] = {
                    "name": lang_c["block.minecraft." + str(file).replace(".json","")]
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face {
  background-image: url(""" + str(mdl_c["textures"]["all"]).replace("minecraft:","textures/") +""".png);
}""")
            except:
                block_types[str(file).replace(".json","")] = {
                    "name": "block.minecraft." + str(file).replace(".json","")
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face {
  background-image: url(""" + str(mdl_c["textures"]["all"]).replace("minecraft:","textures/") +""".png);
}""")

        case "minecraft:block/leaves":
            try:
                block_types[str(file).replace(".json","")] = {
                    "name": lang_c["block.minecraft." + str(file).replace(".json","")]
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face {
  background-image: url(""" + str(mdl_c["textures"]["all"]).replace("minecraft:","textures/") +""".png);
}""")
            except:
                block_types[str(file).replace(".json","")] = {
                    "name": "block.minecraft." + str(file).replace(".json","")
                }
                m_css.write("""
.block.""" + str(file).replace(".json","") + """ .face {
  background-image: url(""" + str(mdl_c["textures"]["all"]).replace("minecraft:","textures/") +""".png);
}""")

with open("./generated/models.css","a") as m_css:
    for file in os.listdir("./data/models/"):
        addModel(file,m_css)
    m_css.close()
with open("./generated/models.js","w",encoding="utf-8") as m_js:
    m_js.write("blockTypes = " + json.dumps(block_types,indent=2) + ";")
    m_js.close()