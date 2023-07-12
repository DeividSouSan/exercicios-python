
# Definindo os códigos de escape ANSI para cores
RESET = "\033[0m"      # Resetar todas as configurações
BOLD = "\033[1m"       # Texto em negrito
ITALIC = "\033[3m"     # Texto em itálico
UNDERLINE = "\033[4m"
NEGATIVE = "\033[7m"

# Cores do texto
C_BLACK = "\033[30m"     # Preto
C_RED = "\033[31m"       # Vermelho
C_GREEN = "\033[32m"     # Verde
C_YELLOW = "\033[33m"    # Amarelo
C_BLUE = "\033[34m"      # Azul
C_MAGENTA = "\033[35m"   # Magenta
C_CYAN = "\033[36m"      # Ciano
C_WHITE = "\033[37m"     # Branco

# Cores do plano de fundo
BG_BLACK = "\033[40m"     # Preto
BG_RED = "\033[41m"       # Vermelho
BG_GREEN = "\033[42m"     # Verde
BG_YELLOW = "\033[43m"    # Amarelo
BG_BLUE = "\033[44m"      # Azul
BG_MAGENTA = "\033[45m"   # Magenta
BG_CYAN = "\033[46m"      # Ciano
BG_WHITE = "\033[47m"     # Branco

END_C = "\033[m"

def cprint(str, decoration="", color="", bg_color="", end="\n"):
    """
    A função possui quatro parâmetros: string, decoration, color e bgcolor.
    Na string passada como parâmetro o ! é usado para marcar o início e o fim do pedaço da string que deve ser colorido. Se não for passado nada toda a string será colorida.

    str -> O texto que você quer mostrar na tela
    decoration -> RESET, BOLD, ITALIC, UNDERLINE ou NEGATIVE
    color -> BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
    bg_color -> BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE
    """
    placeholderON = str.count("!")  >= 2

    if placeholderON:
        firstKeyPos = str.index("!")
        secondKeyPos = str.index("!", firstKeyPos+1)
        
        placeholder = str[firstKeyPos+1:secondKeyPos]
        colorized = decoration + color + bg_color + placeholder + END_C

        str = str.replace(f"!{placeholder}!", colorized);
    else:
        str = decoration + color + bg_color + str

    print(str, end=end)
