"""
Referência :  https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/

O processo de aprendizado por reforço envolve:

1. Observar o ambiente
2. Detectar como agir usando alguma estrategia
3. Agir de acordo com essa estrategia
4. Avaliar o resultado da ação e penalizar ou recompensar 
5. Aprender atraves das experiencias refinando nossa estrategia 
6. Iterar ate uma estrategia otima ser encontrada

O problema apresentado a seguir é uma simplicação de um táxi autônomo,
o objetivo do táxi é pegar um passageiro e o transportar para um determinado
local no menor tempo possivel, cuidando para não inflingir nenhuma regra de trafico. 

Dentro do contexto de RL (Reinforcement Learning) existe 3 conceitos principais:
    Ações: É o conjunto de ações que se pode realizar em determinada momento (estado).
    Para o caso do problema do carro, existe 6 ações possiveis:
        1. ir para a dereita
        2. ir para a esquerda
        3. ir para tras
        4. ir para frente 
        5. Pagar o passageiro
        6. Deixar o passageiro

    Estado: No contexto de aprendizado por reforço o agente se encontra em um estado
    e deve realizar uma ação para ir para outro estado.

    Recompensas: É o valor dado ao agente pela sua ação em determinado estado, esse 
    valor é positivo caso a ação seja uma recompensa e negativo em caso de penalização.

O objetivo do aprendizado por reforço é encontrar uma sequencia de ações que maximize
a recompensa do agente.
"""

import gym

env = gym.make("Taxi-v3").env
env.render()
