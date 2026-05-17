#Conversor de Temperatura
#Variável "celsius" com a captura já com casting de conversão de texto para decimal
celsius = float(input("Digite um número: ")) 
print("Temperatura em Graus: ", celsius) #Temperatura em Celsius com os dados já salvos
#Variável "fahrenheit" com a fórmula do calculo já com os dados da Temperatura Celsius
fahrenheit = celsius * 9/5 + 32
print(f"A temperatura convertida é {fahrenheit} graus Fahrenheit.") #Comunicado final da conversão