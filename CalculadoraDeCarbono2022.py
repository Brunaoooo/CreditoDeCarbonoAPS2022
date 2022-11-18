print("Calculadora de crédito de carbono")
dist=int(input("Digite a distância percorrida por dia em Km:"))
temp=int(input("Digite a quantidade de dias em uma semana onde ocorrem percursos:"))
tipo=int(input("Digite 1 para gasolina e 2 para diesel:"))
while tipo!=1 and tipo!=2:
    tipo=int(input("Digite 1 para gasolina e 2 para diesel:"))
con=int(input("Digite a taxa de consumo (Km/L):"))
dia=dist/con
ano=dia*53
if tipo==1:
    co2=((dist*temp*53)/con)*(0.82*0.75*3.7)
elif tipo==2:
    co2=((dist*temp*53)/con)*(0.83*3.7)
else:
    co2=0
print("O consumo diário em litros é de:%.2f"%dia)
print("O consumo anual em litros é de:%.2f"%ano)
print("É emitido um total de (kg de CO2):%.2f"%(co2))
print("É emitido um total de (ton de CO2):%.2f"%(co2/1000))
print("Lucro total por meio de créditos de carbonos em R$:%.2f"%(co2/1000*1.7))
