import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        # Lista de palavras para o jogo
        self.words = ['python', 'javascript', 'html', 'css', 'react', 'node']

        # Inicializar variáveis do jogo
        self.chosen_word = ""
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        
        # Criar widgets da interface gráfica
        self.create_widgets()
        
        # Iniciar o jogo
        self.start_game()

    def create_widgets(self):
        """Criar todos os widgets da interface gráfica"""
        # Label para exibir a palavra
        self.word_label = tk.Label(self.root, font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        # Canvas para desenhar o boneco da forca
        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack(pady=20)

        # Entrada de texto para tentar adivinhar uma letra
        self.letter_input = tk.Entry(self.root, font=("Helvetica", 18), width=5)
        self.letter_input.pack(pady=10)
        self.letter_input.bind("<Return>", self.make_guess)

        # Botão para tentar a letra
        self.guess_button = tk.Button(self.root, text="Tentar", font=("Helvetica", 14), command=self.make_guess)
        self.guess_button.pack(pady=10)

        # Label para mostrar as letras já tentadas
        self.used_letters_label = tk.Label(self.root, font=("Helvetica", 14))
        self.used_letters_label.pack(pady=10)

        # Label para status do jogo (se ganhou ou perdeu)
        self.status_label = tk.Label(self.root, font=("Helvetica", 14))
        self.status_label.pack(pady=10)

    def start_game(self):
        """Iniciar um novo jogo"""
        self.chosen_word = random.choice(self.words)
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.update_word_display()

    def update_word_display(self):
        """Atualizar a exibição da palavra com as letras adivinhadas"""
        display_word = ''
        for letter in self.chosen_word:
            if letter in self.guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '
        self.word_label.config(text=display_word.strip())
        self.used_letters_label.config(text="Letras usadas: " + ', '.join(self.guessed_letters))
        self.check_game_status()

    def make_guess(self, event=None):
        """Fazer uma tentativa de adivinhar uma letra"""
        letter = self.letter_input.get().lower()
        
        if letter and letter.isalpha() and len(letter) == 1:
            if letter not in self.guessed_letters:
                self.guessed_letters.append(letter)

                if letter not in self.chosen_word:
                    self.incorrect_guesses += 1
                    self.draw_hangman()

                self.update_word_display()
            else:
                self.status_label.config(text="Você já tentou essa letra.")
        else:
            self.status_label.config(text="Por favor, insira uma letra válida.")

        self.letter_input.delete(0, tk.END)  # Limpar a entrada após tentar

    def draw_hangman(self):
        """Desenhar a forca conforme o número de tentativas incorretas"""
        self.canvas.delete("all")
        # A base do boneco
        self.canvas.create_line(50, 150, 150, 150)
        self.canvas.create_line(100, 50, 100, 150)
        self.canvas.create_line(50, 50, 100, 50)
        
        # Desenho do corpo do boneco baseado nas tentativas incorretas
        if self.incorrect_guesses > 0:
            self.canvas.create_oval(85, 60, 115, 90)  # Cabeça
        if self.incorrect_guesses > 1:
            self.canvas.create_line(100, 90, 100, 130)  # Corpo
        if self.incorrect_guesses > 2:
            self.canvas.create_line(100, 110, 85, 130)  # Braço esquerdo
        if self.incorrect_guesses > 3:
            self.canvas.create_line(100, 110, 115, 130)  # Braço direito
        if self.incorrect_guesses > 4:
            self.canvas.create_line(100, 130, 85, 150)  # Perna esquerda
        if self.incorrect_guesses > 5:
            self.canvas.create_line(100, 130, 115, 150)  # Perna direita

    def check_game_status(self):
        """Verificar se o jogo acabou (vitória ou derrota)"""
        if self.incorrect_guesses >= self.max_incorrect_guesses:
            self.status_label.config(text="Você perdeu! A palavra era: " + self.chosen_word)
            self.guess_button.config(state=tk.DISABLED)
        elif all(letter in self.guessed_letters for letter in self.chosen_word):
            self.status_label.config(text="Você ganhou! A palavra foi: " + self.chosen_word)
            self.guess_button.config(state=tk.DISABLED)
        else:
            self.status_label.config(text="")

# Inicializar a janela do Tkinter
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
