class MaquinaNorma:
    def __init__(self):
        self.registradores = {r: 0 for r in "ABCDEFGH"}
        self.instrucoes = []
        self.INSTRUCOES_VALIDAS = ["ZER", "ADD", "SUB"]

    def inicializar_registradores(self):
        print("Inicialização dos registradores (valores inteiros não-negativos).")
        for r in self.registradores:
            while True:
                try:
                    valor = int(input(f"Digite o valor para o registrador {r}: "))
                    if valor < 0:
                        raise ValueError("O valor deve ser não-negativo.")
                    self.registradores[r] = valor
                    break
                except ValueError as e:
                    print(f"Entrada inválida: {e}")
        print("Registradores inicializados com sucesso!")
        print("Estado atual dos registradores:")
        for r, val in self.registradores.items():
            print(f"  {r} = {val}")

    def _formatar_retorno(self, marcador):
        valores = tuple(self.registradores[r] for r in self.registradores)
        return f"({valores} {marcador})"
    
    def _descrever_instrucao(self, instrucao):
        nome = instrucao["instrucao"]
        reg = instrucao["registrador"]
        
        if nome == "ADD":
            return f"FACA ADD ({reg}) VA_PARA {instrucao['destino']}"
        elif nome == "SUB":
            return f"FACA SUB ({reg}) VA_PARA {instrucao['destino']}"
        elif nome == "ZER":
            return f"SE ZER ({reg}) ENTAO VA_PARA {instrucao['destino_true']} SENAO VA_PARA {instrucao['destino_false']}"
        else:
            return f"INSTRUÇÃO DESCONHECIDA: {nome}"

    def carregarPrograma(self, caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            linhas = [linha.strip() for linha in arquivo]
            
            for i in range(len(linhas)):
                numero, comando = linhas[i].split(":")
                numero = int(numero.strip())
                comando = comando.strip()
                for instrucao in self.INSTRUCOES_VALIDAS:
                    if comando.startswith(instrucao):
                        resto = comando[len(instrucao):]

                        if instrucao == "ZER":
                            registrador = resto[0]
                            partes = resto[1:].split(" ")
                            destino_true = int(partes[0])
                            destino_false = int(partes[1])
                            
                            self.instrucoes.append({
                                "linha": numero,
                                "instrucao": instrucao,
                                "registrador": registrador,
                                "destino_true": destino_true,
                                "destino_false": destino_false
                            })

                        else:
                            registrador = resto[0]
                            destino = int(resto[1:])
                            
                            self.instrucoes.append({
                                "linha": numero,
                                "instrucao": instrucao,
                                "registrador": registrador,
                                "destino": destino
                            })


    def executar(self):
        mapa = {inst["linha"]: inst for inst in self.instrucoes}

        linha_atual = 1

        while linha_atual in mapa:
            instrucao = mapa[linha_atual]
            nome = instrucao["instrucao"]
            reg = instrucao["registrador"]
            marcador = self.instrucoes.index(instrucao)

            if nome == "ADD":
                self.registradores[reg] += 1
                linha_atual = instrucao["destino"]
            elif nome == "SUB":
                if self.registradores[reg] > 0:
                    self.registradores[reg] -= 1
                else:
                    pass
                linha_atual = instrucao["destino"]
            elif nome == "ZER":
                if self.registradores[reg] == 0:
                    linha_atual = instrucao["destino_true"]
                else:
                    linha_atual = instrucao["destino_false"]
            else:
                print(f"Instrução inválida! {nome}")
                break

            retorno = self._formatar_retorno(marcador)
            descricao = self._descrever_instrucao(instrucao)
            print(f"{retorno} {descricao}")

        print("Execução finalizada.")
        print("Estado final dos registradores:")
        for r, val in self.registradores.items():
            print(f"  {r} = {val}")


if __name__ == "__main__":
    maquina = MaquinaNorma()
    progCarregado = False
    print("\nMáquina Norma:")
    print("Você deve primeiro carregar um programa e inicializar os registradores antes de executar.\n")
    print("--------------------")
    while True:
        if progCarregado == True:
            print("PROGRAMA CARREGADO")
        else:
            print("[0] - Carregar Programa; \n[1] - Inicializar e manipular registradores direto; \n[2] - Executar Programa.\n[9] Sair")

        try:
            opt = int(input("Escolha sua opção: "))
        except ValueError:
            print("❌ Opção inválida! Digite um número entre 0 e 2.\n")
        if opt == 0:
            try:
                maquina.carregarPrograma("programa.txt")
                print("Programa carregado com sucesso!\n")
                progCarregado = True
            except FileNotFoundError:
                print("❌ Arquivo não encontrado! Verifique se 'programa.txt' está no diretório correto.\n")
            except ValueError:
                print("❌ Erro de leitura! Verifique se todas as linhas estão no formato correto (ex: 1:ADD A2 ou 2:ZER B3 4).\n")
            except Exception as e:
                print(f"❌ Erro inesperado: {e}\n")

        elif opt == 1:
            maquina.inicializar_registradores()

        elif opt == 2:
            if progCarregado == False:
                print("Carregue o Programa antes de Executar\n")
            else:
                maquina.executar()

        elif opt == 9:
            print("Encerrando a Máquina Norma. Até logo!")
            break
        
        else:
            print("Opção inválida!\n")
