###################
# Modulo de Filas #
###################

class Fila:
    # Tamanho da Fila
    TAMANHO_FILA = 1000
    # Processos executados
    todos_processos = list()
    # Fila de processos de tempo real
    processos_real = []
    # Fila de processos de usuario
    processos_usuario1 = []
    processos_usuario2 = []
    processos_usuario3 = []

    def adiciona_em_fila(self, proc):

        if (proc.prioridade == 0):
            if len(self.processos_real) < self.TAMANHO_FILA:
                self.processos_real.append(proc)
                self.todos_processos.append(proc)
        elif (proc.prioridade == 1):
            if len(self.processos_usuario1) < self.TAMANHO_FILA:
                self.processos_usuario1.append(proc)
                self.todos_processos.append(proc)
        elif (proc.prioridade == 2):
            if len(self.processos_usuario2) < self.TAMANHO_FILA:
                self.processos_usuario2.append(proc)
                self.todos_processos.append(proc)
        elif (proc.prioridade == 3):
            if len(self.processos_usuario3) < self.TAMANHO_FILA:
                self.processos_usuario3.append(proc)
                self.todos_processos.append(proc)
        else:
            print("Prioridade invalida")
            exit(0)

        self.processos_real.sort(key=lambda x: x.tempo_init)  # Ordena os processos por ordem de chegada
        self.processos_usuario1.sort(key=lambda x: x.tempo_init)
        self.processos_usuario2.sort(key=lambda x: x.tempo_init)
        self.processos_usuario3.sort(key=lambda x: x.tempo_init)

    def aging_process(self):
        if(self.posicoes_livres_na_fila1(len(self.processos_usuario2))):
            self.processos_usuario1.extend(self.processos_usuario2)
            self.processos_usuario2[:] = []
        if(self.posicoes_livres_na_fila2(len(self.processos_usuario3))):
            self.processos_usuario2.extend(self.processos_usuario3)
            self.processos_usuario3[:] = []

    def posicoes_livres_na_fila1(self, posicoes_necessarias):
        posicoes_livres = 1000 - len(self.processos_usuario1)
        return posicoes_necessarias <= posicoes_livres

    def posicoes_livres_na_fila2(self, posicoes_necessarias):
        posicoes_livres = 1000 - len(self.processos_usuario2)
        return posicoes_necessarias <= posicoes_livres

    def err_fila(self):
        print("Pilha cheia")

    def existe_processos_para_executar(self):
        return (len(self.processos_real) != 0) or (len(self.processos_usuario1) > 0) or (
            len(self.processos_usuario2) > 0) or (len(self.processos_usuario3) > 0)

    def existe_processo_real(self):
        return len(self.processos_real) != 0

    def existe_processo_1(self):
        return len(self.processos_usuario1) != 0

    def existe_processo_2(self):
        return len(self.processos_usuario2) != 0

    def existe_processo_3(self):
        return len(self.processos_usuario3) != 0

    def existe_processo_usuario(self):
        return (len(self.processos_usuario3) != 0) or (len(self.processos_usuario2) != 0) or (
        len(self.processos_usuario3))

    def aging(self):
        if(len(self.processos_usuario3) > 0):
            if(len(self.processos_usuario2) > 0):
                self.swap_filas(self.processos_usuario2,self.processos_usuario3)
            else:
                processo = self.processos_usuario3.pop(self.menos_executado_fila(self.processos_usuario3))
                self.processos_usuario2.append(processo)

        if(len(self.processos_usuario2) > 0):
            if(len(self.processos_usuario1) > 0):
                self.swap_filas(self.processos_usuario1,self.processos_usuario2)
            else:
                processo2 = self.processos_usuario2.pop(self.menos_executado_fila(self.processos_usuario2))
                self.processos_usuario1.append(processo2)


    def swap_filas(self,fila1,fila2):
        processo1 = fila1.pop(self.mais_executado_fila(fila1))
        processo2 = fila2.pop(self.menos_executado_fila(fila2))
        processo1.tempo_cpu = processo1.tempo_cpu - (processo1.tempo_decorrido - 1)
        processo1.tempo_decorrido = 1
        fila1.append(processo2)
        fila2.append(processo1)


    def mais_executado_fila(self,fila):
        tempo_decorrido = 0
        posicao = 0
        for i in range(0,len(fila)):
            if(fila[i].tempo_decorrido > tempo_decorrido):
                tempo_decorrido = fila[i]
                posicao = i
        return posicao


    def menos_executado_fila(self,fila):
        tempo_decorrido = fila[0].tempo_decorrido
        posicao = 0
        for i in range(0,len(fila)):
            if(fila[i].tempo_decorrido < tempo_decorrido):
                tempo_decorrido = fila[i]
                posicao = i

        return posicao


