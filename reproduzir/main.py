import sys
import os
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget,QSlider,QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput
from PyQt5.QtCore import Qt,QUrl

from player import Ui_MainWindow

class player(QMainWindow):
    def __init__(self):
        super(player, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.numero = 0 
        songs=[ 
        {   
            'Posição': '0',
            'nome_musica': 'Amanhã não se sabe',
            'duracao': '4:41',
            'art': 'LS Jack'
        },
        {
            'Posição': '1',
            'nome_musica': 'Walk',
            'duracao': '5:58',
            'art': 'Foo Fighters'
        },
        {
            'Posição': '2',
            'nome_musica': 'My Way',
            'duracao': '4:34',
            'art': 'Frank Sinatra'
        },
        {
            'Posição': '3',
            'nome_musica': 'La vie en rose',
            'duracao': '3:23',
            'art': 'Louis Armstrong'
        },
        {
            'Posição': '4',
            'nome_musica': "Can't Help Falling In Love",
            'duracao': '3:00',
            'art': 'Elvis Presley'
        }
    ]
        
        self.ajustando_tabela()
        self.preencher_tabela(songs)
        
        self.ui.pushButton_player.clicked.connect(self.play_music)
        self.ui.pushButton_pause.clicked.connect(self.pause_music)
        self.ui.tableWidget.itemClicked.connect(self.selecionar_musica)
        self.ui.pushButton_random.clicked.connect(lambda: self.random_music(songs))
        
        
        
        while True:
            self.ui.pushButton_next_song.clicked.connect(lambda: self.next_music())
            self.ui.pushButton_previous_song.clicked.connect(lambda: self.previous_music())

            break
        
        self.image_dir = "imagens/"
        self.image_files = self.get_image_files()
        self.current_index = 1  # Índice da imagem atual
        
        self.load_image(0)
        self.ui.label_nome.setText(songs[0]['nome_musica'])
        self.ui.label_art.setText(songs[0]['art'])
        self.ui.label_duracao.setText(songs[0]['duracao'])

        self.media_player = QMediaPlayer()
        
        # Conectar o slider para acompanhar a música
        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.durationChanged.connect(self.set_duration)
        self.ui.sliderProgress.sliderReleased.connect(self.set_position)
        self.ui.sliderProgress.sliderMoved.connect(self.set_position) 
     
    def get_image_files(self):
        """ Obtém uma lista de arquivos de imagem no diretório especificado """
        if not os.path.exists(self.image_dir):
            return []
        
        return sorted([f for f in os.listdir(self.image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))])
    
    def load_image(self, index):
        """ Carrega e exibe a imagem no índice especificado """
        if not self.image_files:
            self.ui.label_imagem.setText("Nenhuma imagem encontrada.")
            return

        image_path = os.path.join(self.image_dir, self.image_files[index])
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            self.ui.label_imagem.setText("Erro ao carregar a imagem.")
        else:
            self.ui.label_imagem.setPixmap(pixmap)
            self.ui.label_imagem.setScaledContents(True)

    def selecionar_musica(self):
        
        songs=[
        {   
            'Posição': '0',
            'nome_musica': 'Amanhã não se sabe',
            'duracao': '4:41',
            'art': 'LS Jack'
        },
        {
            'Posição': '1',
            'nome_musica': 'Walk',
            'duracao': '5:58',
            'art': 'Foo Fighters'
        },
        {
            'Posição': '2',
            'nome_musica': 'My Way',
            'duracao': '4:34',
            'art': 'Frank Sinatra'
        },
        {
            'Posição': '3',
            'nome_musica': 'La vie en rose',
            'duracao': '3:23',
            'art': 'Louis Armstrong'
        },
        {
            'Posição': '4',
            'nome_musica': "Can't Help Falling In Love",
            'duracao': '3:00',
            'art': 'Elvis Presley'
        }
        ]
        index = self.ui.tableWidget.currentRow()
        
        if index >= 0:
            
            musica_selecionada = songs[index]
            self.ui.label_nome.setText(musica_selecionada['nome_musica'])
            self.ui.label_art.setText(musica_selecionada['art'])
            self.ui.label_duracao.setText(musica_selecionada['duracao'])

            res = int(musica_selecionada['Posição'])
            self.load_image(res)
            
            file_name = "musicas/" + musica_selecionada['nome_musica'] + ".mp3"
            if not os.path.exists(file_name):
                QMessageBox.critical(self, "Erro", "A música selecionada não foi encontrada.")
                return
    
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.media_player.play()
    
    def next_music(self):
        self.numero += 1
        if self.numero == 5:
            self.numero = 0
        songs=[
        {   
            'Posição': '0',
            'nome_musica': 'Amanhã não se sabe',
            'duracao': '4:41',
            'art': 'LS Jack'
        },
        {
            'Posição': '1',
            'nome_musica': 'Walk',
            'duracao': '5:58',
            'art': 'Foo Fighters'
        },
        {
            'Posição': '2',
            'nome_musica': 'My Way',
            'duracao': '4:34',
            'art': 'Frank Sinatra'
        },
        {
            'Posição': '3',
            'nome_musica': 'La vie en rose',
            'duracao': '3:23',
            'art': 'Louis Armstrong'
        },
        {
            'Posição': '4',
            'nome_musica': "Can't Help Falling In Love",
            'duracao': '3:00',
            'art': 'Elvis Presley'
        }
        ]
        index = self.ui.tableWidget.currentRow()
        index += self.numero
        print(index)
        
        if index == len(songs):
            index = 0
        if index >= 0:
            
            musica_selecionada = songs[index]
            self.ui.label_nome.setText(musica_selecionada['nome_musica'])
            self.ui.label_art.setText(musica_selecionada['art'])
            self.ui.label_duracao.setText(musica_selecionada['duracao'])

            res = int(musica_selecionada['Posição'])
            self.load_image(res)
            
            file_name = "musicas/" + musica_selecionada['nome_musica'] + ".mp3"
            if not os.path.exists(file_name):
                QMessageBox.critical(self, "Erro", "A musica selecionada nao foi encontrada.")
                return
            
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.media_player.play()

    def previous_music(self):
        self.numero -= 1
        if self.numero < 0:
            self.numero = 0
        songs=[
        {   
            'Posição': '0',
            'nome_musica': 'Amanhã não se sabe',
            'duracao': '4:41',
            'art': 'LS Jack'
        },
        {
            'Posição': '1',
            'nome_musica': 'Walk',
            'duracao': '5:58',
            'art': 'Foo Fighters'
        },
        {
            'Posição': '2',
            'nome_musica': 'My Way',
            'duracao': '4:34',
            'art': 'Frank Sinatra'
        },
        {
            'Posição': '3',
            'nome_musica': 'La vie en rose',
            'duracao': '3:23',
            'art': 'Louis Armstrong'
        },
        {
            'Posição': '4',
            'nome_musica': "Can't Help Falling In Love",
            'duracao': '3:00',
            'art': 'Elvis Presley'
        }
        ]
        index = self.ui.tableWidget.currentRow()
        index += self.numero
        print(index)
        if index == 0:
            index = 0
        if index >= 0:
            
            musica_selecionada = songs[index]
            self.ui.label_nome.setText(musica_selecionada['nome_musica'])
            self.ui.label_art.setText(musica_selecionada['art'])
            self.ui.label_duracao.setText(musica_selecionada['duracao'])

            res = int(musica_selecionada['Posição'])
            self.load_image(res)
            
            file_name = "musicas/" + musica_selecionada['nome_musica'] + ".mp3"
            if not os.path.exists(file_name):
                QMessageBox.critical(self, "Erro", "A musica selecionada nao foi encontrada.")
                return
            
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.media_player.play()

    def random_music(self, songs):
        num_aleatorio = random.randint(0, 4)
        self.numero = num_aleatorio
        index = num_aleatorio
        if index >= 0:
            
            musica_selecionada = songs[index]
            self.ui.label_nome.setText(musica_selecionada['nome_musica'])
            self.ui.label_art.setText(musica_selecionada['art'])
            self.ui.label_duracao.setText(musica_selecionada['duracao'])

            res = int(musica_selecionada['Posição'])
            self.load_image(res)
            
            file_name = "musicas/" + musica_selecionada['nome_musica'] + ".mp3"
            if not os.path.exists(file_name):
                QMessageBox.critical(self, "Erro", "A musica selecionada nao foi encontrada.")
                return
            
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.media_player.play()
    def play_music(self):
        print(self.media_player.state())
        if self.media_player.state() == QMediaPlayer.PausedState:
            self.media_player.play()

    def pause_music(self):
        print(self.media_player.state())
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()

    def update_slider(self, position):
        """Atualiza a barra de progresso conforme a música toca."""
        duration = self.media_player.duration()
        if duration > 0:
            self.ui.sliderProgress.setValue(int((position / duration) * self.ui.sliderProgress.maximum()))
        if position == self.ui.sliderProgress.maximum():
            self.next_music()
    def set_duration(self, duration):
        """Define o range correto da barra de progresso."""
        if duration > 0:
            self.ui.sliderProgress.setRange(0, duration)

    def set_position(self):
        """Move a música para a posição escolhida no slider."""
        self.media_player.setPosition(self.ui.sliderProgress.value())
            
    def ajustando_tabela(self):
        self.tableWidget = self.ui.tableWidget
        self.tableWidget.setColumnWidth(0, 500)  # Segunda coluna com 200px

    def preencher_tabela(self, songs):
        self.tableWidget.setRowCount(len(songs))
        
        for i, song in enumerate(songs):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(song['nome_musica']))    
            # self.tableWidget.setItem(i, 1, QTableWidgetItem(song['duracao']))
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = player()
    window.show()
    sys.exit(app.exec_())