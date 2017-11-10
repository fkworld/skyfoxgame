from flask import url_for

class App(object):
    def __init__(self, name, icon_filename="icon.png", picture_filename="pic.png", txt_filename="txt.txt"):
        self.name = name
        url_name = self.name.lower().replace(" ", "_")
        from app_view import app_view
        self.url = url_for("app_view." + url_name)
        self.icon = url_for("static", filename="app/" + url_name + "/" + icon_filename)
        self.picture = url_for("static", filename="app/" + url_name + "/" + picture_filename)

        try:
            # 这里读取文件的路径需要删除第一个"/"字符
            file_url = url_for("static", filename="app/" + url_name + "/" + txt_filename).replace("/","",1)
            txt_file = open(file_url,"r")
            txts = txt_file.readlines()
            self.download_appstore = txts.pop(0)
            self.download_googleplay = txts.pop(0)
            self.download_taptap = txts.pop(0)
            self.text = txts
        finally:
            txt_file.close( )
        
