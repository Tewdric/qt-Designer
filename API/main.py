import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWebEngineWidgets import QWebEngineView

class VideoPlayer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Carrega a interface do Qt Designer
        uic.loadUi("pokemon.ui", self)

        # Conecta o botão à função de reprodução
        self.pushButton.clicked.connect(self.reproduzir_video)

        # Cria um QWebEngineView para renderizar o vídeo
        self.video_widget = QWebEngineView()
        self.ui.widgetLayout.addWidget(self.video_widget)
        
    def reproduzir_video(self):
        # Pega o link ou ID do vídeo do QLineEdit
        link = self.lineEdit.text()

    
        # Converte o link para o formato embed do YouTube
        if "youtube.com" in link:
            video_id = link.split("v=")[1].split("&")[0]  # Extrai o ID do vídeo
        else:
            video_id = link  # Assume que o usuário digitou apenas o ID

        embed_url = f"https://www.youtube.com/embed/{video_id}"

        # Carrega o vídeo no QWebEngineView
        self.video_widget.setUrl(embed_url)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())