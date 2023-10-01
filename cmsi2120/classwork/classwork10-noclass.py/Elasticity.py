# TBDY 2018'e göre "Yatay Elastik Tasarım Spektrumu" hesabı
import numpy as np

# INPUTS
Ss = 1.518 ; Fs = 0.800 ; S1 = 0.417 ; F1 = 2.366

# CALCULATIONS
Sds = Ss*Fs
Sd1 = S1*F1
Ta = 0.2*Sd1/Sds 
Tb = Sd1/Sds
Tl = 6.0

# define a function for spectrum value calculation
def spec(Ti):
    if Ti <= Ta:
        Saei = (0.4 + 0.6*Ti/Ta)*Sds
    elif Ti > Ta and Ti <= Tb:
        Saei = Sds
    elif Ti > Tb and Ti <= Tl:
        Saei = Sd1/Ti
    else: 
        Saei = Sd1*Tl/Ti**2
        
    return Saei


# Calculate all Sae values for any  given T range
T = np.arange(0.01, 7.1, 0.1)

Sae = list()    # [g]; elastik tasarım spektral ivmeleri
for Ti in T:
    Saei = spec(Ti)
    Sae.append(Saei)

print("T=", T) 
print("Sae=", Sae)