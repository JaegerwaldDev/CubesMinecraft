import os, sys, json, shutil

input("Are the requirements installed? If yes, press enter.")

if not os.path.exists("./data/"):
    os.mkdir("data")
if not os.path.exists("./dump/"):
    os.mkdir("dump")

def get_png(texture):
    return "./data/assets/minecraft/textures/" + texture.split("minecraft:")[1] + ".png"

def write_model(path, model_name):
    with open(path, "r") as mdl_f:
        mdl_c = mdl_f.read()
        mdl_f.close()
        mdl_c = json.loads(mdl_c)
        if "parent" in mdl_c:
            if mdl_c["parent"] == "minecraft:block/cube":
                print(path+(80-len(path))*" ","| block/cube         | 6 textures")
                with open("./dump/models.html", "a") as tex_f:
                    tex_f.write("<code>" + model_name + "</code> ")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["down"]) + "\">")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["east"]) + "\">")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["north"]) + "\">")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["south"]) + "\">")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["up"]) + "\">")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["west"]) + "\">")
                    tex_f.write("<br>")
                    tex_f.close()
                shutil.copy(get_png(mdl_c["textures"]["down"]),"./data/textures/block/")
                shutil.copy(get_png(mdl_c["textures"]["east"]),"./data/textures/block/")
                shutil.copy(get_png(mdl_c["textures"]["north"]),"./data/textures/block/")
                shutil.copy(get_png(mdl_c["textures"]["south"]),"./data/textures/block/")
                shutil.copy(get_png(mdl_c["textures"]["up"]),"./data/textures/block/")
                shutil.copy(get_png(mdl_c["textures"]["west"]),"./data/textures/block/")

                shutil.copy(path,"./data/models/")

            elif mdl_c["parent"] == "minecraft:block/cross" or mdl_c["parent"] == "minecraft:block/tinted_cross":
                print(path+(80-len(path))*" ","| block/cross        | 1 texture")
                with open("./dump/models.html", "a") as tex_f:
                    tex_f.write("<code>" + model_name + "</code> ")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["cross"]) + "\">")
                    tex_f.write("<br>")
                    tex_f.close()
                shutil.copy(get_png(mdl_c["textures"]["cross"]),"./data/textures/block/")
                shutil.copy(path,"./data/models/")

            elif mdl_c["parent"] == "minecraft:block/cube_column":
                print(path+(80-len(path))*" ","| block/cube_column  | 2 textures")
                with open("./dump/models.html", "a") as tex_f:
                    tex_f.write("<code>" + model_name + "</code> ")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["end"]) + "\">")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["side"]) + "\">")
                    tex_f.write("<br>")
                    tex_f.close()
                shutil.copy(get_png(mdl_c["textures"]["end"]),"./data/textures/block/")
                shutil.copy(get_png(mdl_c["textures"]["side"]),"./data/textures/block/")

                shutil.copy(path,"./data/models/")

            elif mdl_c["parent"] == "minecraft:block/cube_all":
                print(path+(80-len(path))*" ","| block/cube_all     | 1 texture")
                with open("./dump/models.html", "a") as tex_f:
                    tex_f.write("<code>" + model_name + "</code> ")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["all"]) + "\">")
                    tex_f.write("<br>")
                    tex_f.close()
                shutil.copy(get_png(mdl_c["textures"]["all"]),"./data/textures/block/")
                shutil.copy(path,"./data/models/")

            elif mdl_c["parent"] == "minecraft:block/leaves":
                print(path+(80-len(path))*" ","| block/leaves       | 1 texture")
                with open("./dump/models.html", "a") as tex_f:
                    tex_f.write("<code>" + model_name + "</code> ")
                    tex_f.write("<img height=\"32px\" width=\"32px\" src=\"../" + get_png(mdl_c["textures"]["all"]) + "\">")
                    tex_f.write("<br>")
                    tex_f.close()
                shutil.copy(get_png(mdl_c["textures"]["all"]),"./data/textures/block/")
                shutil.copy(path,"./data/models/")

def put_assets_folder():
    input("""
    Please take a vanilla "assets" folder (1.20+) from any source
    and put it into the "data" folder. To Forkers: If you wish to
    use a Texturepack, merge the Texturepacks's texture folder with
    Vanilla Minecraft's texture folder. Press enter to continue.""")
    if os.path.exists("./data/assets/minecraft/models/block/") and os.path.exists("./data/assets/minecraft/lang/en_us.json") and os.path.exists("./data/assets/minecraft/textures/block/"):
        shutil.copy("./data/assets/minecraft/lang/en_us.json","./data/")
        print("")
        filter_models()
    else:
        print("\nMissing assets! Repeat")
        put_assets_folder()

def filter_models():
    if not os.path.exists("./data/models/"):
        os.mkdir("data/models")
    if not os.path.exists("./data/textures/"):
        os.mkdir("data/textures")
        os.mkdir("data/textures/block")
    elif not os.path.exists("./data/textures/block"):
        os.mkdir("data/textures/block")
    with open("./dump/models.html", "w") as tex_f:
        tex_f.write("<style>img{transform:translateY(12px);image-rendering:pixelated}body{padding-bottom:16px}</style>")
        tex_f.close()
        
    for file in os.listdir("./data/assets/minecraft/models/block/"):
        if file.endswith(".json"): 
            write_model(os.path.join("./data/assets/minecraft/models/block/",file), file)

    input("""
    A "models" folder should have been created in "data", please
    filter out any models that the engine does not support. You can
    see the list of supported models in the read me. Press enter to
    continue.""")
    complete()

def complete():
    if os.path.exists("./generated/"):
        shutil.rmtree("./generated/")
    os.mkdir("generated")
    input("""
    Build setup is now complete; please go ahead now and run the
    "build.py" script. Press enter to exit.
    """)

put_assets_folder()