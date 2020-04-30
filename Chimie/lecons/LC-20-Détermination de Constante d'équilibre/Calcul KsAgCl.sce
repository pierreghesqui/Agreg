deltaEp =381e-3
deltaE =150e-3
Veau = 50 //mL
Veq  = 15 //mL

Vo =10.0 
V = 5
Vp =23
Vtot = V+Vo+Veau
Vtotp= Vp+Vo+Veau
U =0.059
C1=0.0100
Co = C1*Veq/Vo



pKs = (deltaEp-deltaE)/U-log((C1*(Vp-Veq)/Vtotp)*(Co*Vo-C1*V)/Vtot)/log(100)
