print("\n =============================== \n ====== Roda a Roda do Bau ===== \n =============================== \n")
palavra = ['chuteira', 'gasolina', 'volante', 'banheiro', 'feijoada', 'pedreiro', 'banheiro', 'sabonete', 'farmacia', 'ambulancia']
dica = ['Futebol', 'Combustível', 'Automóvel', 'Higiene', 'Comida', 'Profissão', 'Tem em casa', 'Banho', 'Saúde', 'Hospital']
premio = [100, 200, 300, 400, 500, 600,700, 800,900, 1000, 'Passou a vez', 'Passou a vez',  'Passou a vez', 'Perdeu tudo',' Perdeu tudo']
nome = input('Digite seu nome: ')
ganho_total_jog = []
print(f' \n O seu saldo em todas as rodadas é {sum(ganho_total_jog)}  reais! \n')
jogador = float(input('\n Escolha o seu rival no jogo! \n Digite 1 para escolher João, 2 para escolher José ou 3 para escolher maria: '))
import emoji
if jogador == 1:
    print(emoji.emojize(' Seu rival será o João  :person_with_blond_hair:', use_aliases=True))
    rival = 'João'
elif jogador == 2:
    print(emoji.emojize('O seu rival será o José  :rage4:', use_aliases=True))
    rival = 'José'
elif jogador == 3:
    print(emoji.emojize('O seu rival será a Maria   :woman:', use_aliases=True))
    rival = 'Maria'
else:
    jogador = input('Digite 1, 2 ou 3 para escolher um dos jogadores disponíveis: ')
traço = '________  '
palpites = []
import string
n = 0
p = 2
import random
import time

while n >= 0:
    print(f'\n ------------------------------ \n --------- RODADA {n + 1} -----------\n ------------------------------ \n')
    print(f' \n O seu saldo em todas as rodadas é {sum(ganho_total_jog)}  reais! \n')
    ganho_jogador = []
    ganho_rival = []
    y = 0
    alfabeto = list(string.ascii_lowercase)
    sorteio = random.sample(palavra, 1)
    acerto = list('-'*len(sorteio[0]))
    print(f'\n A dica é {dica[palavra.index(str(sorteio[0]))]} \n A palavra é {acerto}')

    while p % 2 == 0 and acerto.count('-') > 0:
        roda = float(input(' \n Roda a roda (Digite 1): '))
        if roda == 1:
            valor = random.sample(premio, 1)
            x = 4
            while x >=0:
                time.sleep(.5)
                print(' \t * \t')
                x -= 1
            print(f' \n **** {valor} **** \n ')
        if str(valor[0]).isnumeric()==True and acerto.count('-') > 3:
            print(f'\n A dica é {dica[palavra.index(str(sorteio[0]))]}. Valendo {valor} reais,')
            letra = input('Digite uma letra: ').lower()
            if letra in acerto:
                print(f'A letra {letra} já foi digitada')
            alfabeto.remove(letra)
            for i in range(0, len(sorteio[0])):
                if letra in str(sorteio[0])[i]:
                    acerto[i] = letra
                else:
                    continue
            print(f'\n Você digitou a letra {letra}. Painel, tem a letra {letra}? \n')
            if letra in sorteio[0]:
                ganho_jogador.append(acerto.count(letra) * valor[0])
                print(f'\n {nome}, você acertou a letra !!!')
                print(acerto)
                if acerto.count('-') <= 3:
                    resposta = input(f' \n Valendo {sum(ganho_jogador)}, {nome}, digite a palavra completa: ').lower()
                    if resposta == sorteio[0]:
                        print(f' \n A palavra está correta, ganhou {sum(ganho_jogador)} reais!')
                        ganho_total_jog.append(sum(ganho_jogador))
                        acerto = str(palavra)
                    else:
                        p += 1
            else:
                time.sleep(1.3)
                print(f' \n A palavra não tem a letra que você digitou, {nome}. Agora é a vez do(a) {rival} \n')
                p +=1
            if premio == 'Perdeu tudo':
                ganho_jogador = [0]
        elif str(valor[0]).isnumeric()==True and acerto.count('-') <= 3:
            print(acerto)
            resposta = input(f' \n Valendo {sum(ganho_jogador)}, {nome}, digite a palavra completa: ').lower()
            if resposta == sorteio[0]:
                print(f' \n A palavra está correta, ganhou {sum(ganho_jogador)} reais!')
                ganho_total_jog.append(sum(ganho_jogador))
                acerto = str(palavra)
            else:
                p += 1
        else:
            print(f'iiiiii, {valor[0]}')
            p += 1

        while p % 2 != 0 and acerto.count('-') > 0:
            valor_rival = random.sample(premio, 1)
            print(f' \n \n {rival}, é a sua vez. Roda a Roda \n')
            x = 4
            while x >= 0:
                time.sleep(.5)
                print(' \t * \t')
                x -= 1
            print(f' \n **** {valor_rival} **** \n ')
            print(acerto)
            if str(valor_rival[0]).isnumeric() == True and acerto.count('-') > 3:
                print(f'\n Valendo {valor_rival} reais, uma letra: ')
                letra_rival = random.sample(alfabeto, 1)[0]
                palpites.append(letra_rival)
                time.sleep(1)
                print(f'\n {letra_rival}')
                time.sleep(1)
                print(f' \n \n {rival} escolheu a letra {letra_rival}. Painel tem a letra {letra_rival}? \n')
                for i in range(0, len(sorteio[0])):
                    if str(letra_rival) in sorteio[0][i]:
                        acerto[i] = letra_rival
                        alfabeto.remove(str(letra_rival))
                        print(letra_rival)
                        ganho_rival.append(valor_rival)
                if str(letra_rival) in sorteio[0]:
                    time.sleep(.5)
                    print(f' \n {acerto}')
                    time.sleep(.5)
                    print(f'\n Tem a letra {letra_rival}, {rival} ganhou {valor_rival*acerto.count(letra_rival)} reais! ')
                    print(f'\n Roda a roda {rival}! \n')
                else:
                    time.sleep(.5)
                    print(acerto)
                    time.sleep(.5)
                    print(f'\n Não tem a letra {letra_rival}. \n {nome} é a sua vez, roda a roda! \n ')
                    p +=1
            if str(valor_rival[0]).isnumeric() == False:
                print(f'iiiiii, {rival}, {valor_rival[0]}')
                p +=1
                n += 1
            if str(valor_rival[0]).isnumeric() == True and acerto.count('-') <= 3:
                ganho_rival.append(valor_rival[0])
                print(f'\n {rival}, digite a palavra completa!')
                time.sleep(1)
                print(sorteio)
                time.sleep(.8)
                #print(f'{rival} acertou a palavra e ganhou {sum(ganho_rival)} reais!')
                acerto = str(palavra)
                p += 1
    n += 1








