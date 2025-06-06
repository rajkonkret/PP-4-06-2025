# tworzymy pakiet (python package)
# w pakiecie tworzymy plik fun.py
# w tym pliku tworzymy funkcje powitanie()
import pakiet

# po dodaniu w __init__ funkcji powitanie()
# zmienna __all__ steruje widocznością elementów pakietu
pakiet.powitanie()

# dodajemy funkcje info()
from pakiet import fun

fun.info()  # Jestem pakietem
fun.powitanie()

import pakiet.fun as pk  # jako alias

pk.info()
pk.powitanie()
# Cześć
# Jestem pakietem
# Cześć
# Jestem pakietem
# Cześć
