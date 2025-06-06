import pakiet

# po dodaniu w __init__
pakiet.powitanie()

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