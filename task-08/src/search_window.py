
from PySide6.QtWidgets import QDialog, QHBoxLayout, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap, QFont, QPalette, QFontDatabase
import random
import os
import requests




class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    
    def __init__(self):
        super().__init__()
       
        self.w = None        
        self.setFixedSize(850, 500)
        self.setWindowTitle("Pokedex")
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Pokemon")
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 190, 40)

        background_image = QPixmap("../assets/landing.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, background_image)
        self.setPalette(palette)
        layout = QVBoxLayout()
        self.setLayout(layout)


        id = QFontDatabase.addApplicationFont("../assets/arcadeclassic/ARCADECLASSIC.TTF")
        families = QFontDatabase.applicationFontFamilies(id)
        my_font = QFont("Times New Roman", 14)


        self.pokedex = QLabel(self)
        self.pokedex.setGeometry(250,0,600,500)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(300,100,200,200)

        label2 = QLabel("Enter the name", self)
        label2.setGeometry(50,2,600,70)
        label2.setFont(my_font)

        self.info_label = QLabel(self)
        self.info_label.setFont(QFont(families[0], 18))
        self.info_label.setStyleSheet('QLabel { color: black ;}')
        self.info_label.setGeometry(330,190,600,470)

        self.info_label2 = QLabel(self)
        self.info_label2.setFont(QFont(families[0], 18))
        self.info_label2.setStyleSheet('QLabel { color: black ;}')
        self.info_label2.setGeometry(500,190,600,470)

        self.poke_name =QLabel(self)
        self.poke_name.setFont(QFont(families[0], 26))
        self.poke_name.setStyleSheet('QLabel { color: black ;}')
        self.poke_name.setGeometry(560,25,220,220)

        self.poke_ab =QLabel(self)
        self.poke_ab.setFont(QFont(families[0], 13))
        self.poke_ab.setStyleSheet('QLabel { color: black ;}')
        self.poke_ab.setGeometry(620,190,220,220)
        
        self.poke_tp =QLabel(self)
        self.poke_tp.setFont(QFont(families[0], 13))
        self.poke_tp.setStyleSheet('QLabel { color: black ;}')
        self.poke_tp.setGeometry(620,150,220,220)

        self.poke_det =QLabel(self)
        self.poke_det.setFont(QFont(families[0], 16))
        self.poke_det.setStyleSheet('QLabel { color: black ;}')
        self.poke_det.setGeometry(320,200,220,220)

        self.but_style="""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QMainWindow {
                background-color: black;
            }
            QLabel {
                font-size: 32px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.setStyleSheet(self.but_style)
        enter_button.clicked.connect(self.searchPoke)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.setStyleSheet(self.but_style)
        capture_button.clicked.connect(self.capturePoke)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.setStyleSheet(self.but_style)
        display_button.clicked.connect(self.displayCapturedPokemon)



    ## TO-DO ##
    # 1 #
    # Fetch the data from from the API.
    def dispPokeDetails(self,pokemon_data):
        
        pokedx = QPixmap("../assets/pokedex.jpg")
        self.pokedex.setScaledContents(True)
        self.pokedex.setPixmap(pokedx)

        name = pokemon_data['name'].upper()
        ability = random.choice(pokemon_data['abilities'])
        types = [type_data['type']['name'] for type_data in pokemon_data['types']]
        stats = [f"{stat['stat']['name']}: {stat['base_stat']}" for stat in pokemon_data['stats']]
        poke_nm = name
        poke_abbs = "Ability : \n "+str(ability['ability']['name'])
        poke_typ = f"Types: \n{', '.join(types)}\n"
        
        info_text1,info_text2 = "",""
        for i in stats[:3]:
            info_text1 = info_text1+str(i)+"\n" 
        for i in stats[3:]:
            info_text2 = info_text2+str(i)+"\n" 

        self.poke_det.clear()
        self.info_label.setText(info_text1)
        self.info_label2.setText(info_text2)
        self.poke_ab.setText(poke_abbs)
        self.poke_name.setText(poke_nm)
        self.poke_tp.setText(poke_typ)
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    
    def searchPoke(self):
        self.pokemon_name = self.textbox.text().strip().lower()
        if not self.pokemon_name:
            return
        
        # Fetch data from the Pokémon API
        self.api_url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_name}"
        self.response = requests.get(self.api_url)

        if self.response.status_code == 200:
            self.pokemon_data = self.response.json()
            self.dispPokeDetails(self.pokemon_data)
            
            
            image_url = self.pokemon_data["sprites"]['other']['official-artwork']["front_default"]
            print(image_url)
            self.image = QPixmap()
            self.image_label.clear() 
            self.image.loadFromData(requests.get(image_url).content)
            self.image_label.setPixmap(self.image)
            self.image_label.setScaledContents(True)
            self.image_label.show()
        else:
            self.info_label.clear()
            self.info_label2.clear()
            self.poke_ab.clear()
            self.poke_tp.clear()
            self.poke_name.clear()
            self.poke_det.setText("Pokemon  Not  Found")
            self.image_label.clear() 
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.
    def capturePoke(self):
        if hasattr(self, 'pokemon_data'):
            pokemon_name = self.pokemon_data['name'].upper()
            image_url = self.pokemon_data['sprites']['other']['official-artwork']['front_default']

            # Define the path where you want to save the image
            save_folder = "../Bag/"
            os.makedirs(save_folder, exist_ok=True)
            save_path = os.path.join(save_folder, f"{pokemon_name}.png")

            # Check if the image file already exists
            if os.path.exists(save_path):
                self.poke_det.setText(f"{pokemon_name} is already captured.")
                return

            # Download the image using requests
            response = requests.get(image_url)

            if response.status_code == 200:
                # Open a local file for writing
                with open(save_path, 'wb') as file:
                    file.write(response.content)
                self.poke_det.setText(f"Captured {pokemon_name}")
            else:
                self.poke_det.setText(f"Failed to capture {pokemon_name}")
        else:
            self.poke_det.setText("No Pokémon to capture.")
        
        
    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.

    def displayCapturedPokemon(self):
        # Create a dialog to display the captured Pokémon images
        dialog = QDialog(self)
        dialog.setWindowTitle("Captured Pokémon")
        layout = QVBoxLayout()

        # Get the list of image files in the "../Bag/" folder
        image_files = [f for f in os.listdir("../Bag/") if f.endswith(".png")]

        # Initialize an index to keep track of the current image
        self.current_image_index = 0

        # Create labels to display the Pokémon images

        self.image_label = QLabel()
        self.display_image()
        layout.addWidget(self.image_label)

        
        
        # Create "Previous" and "Next" buttons
        button_layout = QHBoxLayout()
        previous_button = QPushButton("Previous")
        previous_button.setStyleSheet(self.but_style)
        next_button = QPushButton("Next")
        next_button.setStyleSheet(self.but_style)

        def previous_image():
            self.current_image_index -= 1
            if self.current_image_index < 0:
                self.current_image_index = len(image_files) - 1
            self.display_image()

        def next_image():
            self.current_image_index += 1
            if self.current_image_index >= len(image_files):
                self.current_image_index = 0
            self.display_image()

        previous_button.clicked.connect(previous_image)
        next_button.clicked.connect(next_image)

        button_layout.addWidget(previous_button)
        button_layout.addWidget(next_button)
        layout.addLayout(button_layout)


        dialog.setLayout(layout)
        dialog.exec_()

    def display_image(self):
        # Get the list of image files in the "../Bag/" folder
        image_files = [f for f in os.listdir("../Bag/") if f.endswith(".png")]

        # Check if there are any captured Pokémon images
        if not image_files:
            self.image_label.clear() 
            self.pokemon_name_label.clear()
            return

        # Load and display the current Pokémon image
        current_image_file = image_files[self.current_image_index]
        image_path = os.path.join("../Bag/", current_image_file)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaledToHeight(300))


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())