import random
import pandas as pd

class funcionarios():
    def __init__(self, nome, salario, cargo, horas_trabalhadas):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.horas_trabalhadas = horas_trabalhadas
        self.imposto_renda = 0

    def gerar_dados_aleatorios(self):
        nomes = ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Mariana", "Fernanda", "Rafael", "Gabriel"]
        self.nome = random.choice(nomes)
        self.salario = round(random.uniform(1820, 10000), 2)
        cargos = ["Gerente", "Analista", "Desenvolvedor", "Coordenador", "Estagiário"]
        self.cargo = random.choice(cargos)
        self.horas_trabalhadas = random.randint(160, 220)
    
    def criar_data(self):
        nome_arquivo = f"funcionario_{str(self.nome)}.txt"
        with open(nome_arquivo, "a", encoding="utf-8") as f:
            f.write(f"Nome: {self.nome}\n")
            f.write(f"Salario: {self.salario}\n")
            f.write(f"Cargo: {self.cargo}\n")
            f.write(f"Horas trabalhadas: {self.horas_trabalhadas}\n")
        print(f"Data escrita no arquivo {nome_arquivo} com sucesso.")

    def imprimir_data(self):
        print("Nome: ", self.nome)
        print("Salario: ", self.salario)
        print("Cargo: ", self.cargo)
        print("Horas trabalhadas: ", self.horas_trabalhadas)

    def ler_funcionario(self):
        nome_arquivo = f"funcionario_{str(self.nome)}.txt"
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            print(f.read())
        if self.salario <= 1500:
            self.imposto_renda = 0
        elif self.salario > 1500 and self.salario < 3000:
            self.imposto_renda = self.salario * 0.15
        elif self.salario > 3000 and self.salario < 5000:
            self.imposto_renda = self.salario * 0.20
        elif self.salario > 5000:     
            self.imposto_renda = self.salario * 0.27

    def impressao(self):
        print("O imposto de renda é: ", self.imposto_renda)
        print("O salario liquido é: ", self.salario - self.imposto_renda)
        print("O salario bruto é: ", self.salario)

    def menu_funcionarios(self):
        import os
        data = []
        for file in os.listdir():
            if file.startswith("funcionario_"):
                with open(file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    nome = lines[0].split(": ")[1].strip()
                    salario = float(lines[1].split(": ")[1].strip())
                    cargo = lines[2].split(": ")[1].strip()
                    horas_trabalhadas = int(lines[3].split(": ")[1].strip())
                    data.append([nome, salario, cargo, horas_trabalhadas])
        
        df = pd.DataFrame(data, columns=["Nome", "Salario", "Cargo", "Horas Trabalhadas"])
        print(df)



funcionario = funcionarios("", 0, "", 0)
funcionario.gerar_dados_aleatorios()
funcionario.criar_data()
funcionario.imprimir_data()
funcionario.ler_funcionario()
funcionario.impressao()
funcionario.menu_funcionarios()
    


  