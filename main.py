import matplotlib.pyplot as plt

#Definir la funcion para calcular costos y emisiones de CO" de cada funte de energia
def costo_solar(consumo):
  costo = consumo * 0.15 #relativo
  return costo

def costo_eolica(consumo):
  costo = consumo * 0.12 #relativo
  return costo

def emisiones_solar(consumo):
  emisiones = consumo * 0.01 #relativo
  return emisiones

def emisiones_eolica(consumo):
  emisiones = consumo * 0.02 #relativo
  return emisiones

# Funcion para optener los datos del usuario
def obtener_datos_usuario():
  consumo = float(input('Ingrese su consumo mensual de energia en kwh: '))
  return consumo

# Funcion principal que llama a las funciones anteriores y muestra los resultados
def main():
  consumo = obtener_datos_usuario()
  costos = [costo_solar(consumo), costo_eolica(consumo)]
  emisiones = [emisiones_solar(consumo), emisiones_eolica(consumo)]

  #Visualizaciones 
  plt.bar(['Solar', 'Eolica'], costos)
  plt.title('Comparacion de costos')
  plt.ylabel('Costo ($)')
  plt.show()

  plt.bar(['Solar', 'Eolica'], emisiones)
  plt.title('Comparacion de emisiones')
  plt.ylaber('Emisiones (kg CO2')
  plt.show()
  
if __name__ == '__main__':
  main()