from random import randint


def resultado(tabuleiro):

    if ganhei(tabuleiro):
        return 'ganhei'

    elif perdi(tabuleiro):
        return 'perdi'

    elif empatou(tabuleiro):
        return 'cheio'

    return False


def ganhei(tabuleiro):

    for l in range(3):
        mais = 0
        for c in range(3):
            mais += tabuleiro[l][c]
            if mais == -3:
                return True

    for c in range(3):
        mais = 0
        for l in range(3):
            mais += tabuleiro[l][c]
            if mais == -3:
                return True

    mais = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    if mais == -3:
        return True

    mais = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
    if mais == -3:
        return True
    return False


def perdi(tabuleiro):

    for l in range(3):
        mais = 0
        for c in range(3):
            mais += tabuleiro[l][c]
            if mais == 3:
                return True

    for c in range(3):
        mais = 0
        for l in range(3):
            mais += tabuleiro[l][c]
            if mais == 3:
                return True

    mais = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    if mais == 3:
        return True

    mais = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
    if mais == 3:
        return True
    return False


def empatou(tabuleiro):

    vazias = []
    for l in range(3):
        for c in range(3):
            if tabuleiro[l][c] == 0:
                vazias.append([int(l), int(c)])
    if len(vazias) == 0:
        return True


def jogar(tabuleiro):

    vazias = []
    for l in range(3):
        for c in range(3):
            if tabuleiro[l][c] == 0:
                vazias.append([int(l), int(c)])

    for casa in vazias:
        if Prstes_a_ganhar(casa, tabuleiro):
            return casa

    for casa in vazias:
        if Prestes_a_perder(casa, tabuleiro):
            return casa

    return melhor_jogada(vazias)


def Prstes_a_ganhar(casa, tabuleiro):

    mais = 0
    for c in range(3):
        mais += tabuleiro[casa[0]][c]
        if mais == -2:
            return True
    mais = 0
    for l in range(3):
        mais += tabuleiro[l][casa[1]]
        if mais == -2:
            return True
    mais = 0

    if casa[0] == 0 and casa[1] == 0:
        mais = tabuleiro[1][1] + tabuleiro[2][2]
        if mais == -2:
            return True
    mais = 0
    if casa[0] == 0 and casa[1] == 2:
        mais = tabuleiro[1][1] + tabuleiro[2][0]
        if mais == -2:
            return True
    mais = 0
    if casa[0] == 2 and casa[1] == 0:
        mais = tabuleiro[1][1] + tabuleiro[0][2]
        if mais == -2:
            return True
    mais = 0
    if casa[0] == 2 and casa[1] == 2:
        mais = tabuleiro[1][1] + tabuleiro[0][0]
        if mais == -2:
            return True
    mais = 0
    if casa[0] == 1 and casa[1] == 1:
        mais = tabuleiro[0][0] + tabuleiro[2][2]
        if mais == -2:
            return True
    mais = 0
    if casa[0] == 1 and casa[1] == 1:
        mais = tabuleiro[2][0] + tabuleiro[0][2]
        if mais == -2:
            return True
    return False


def Prestes_a_perder(casa, tabuleiro):

    mais = 0
    for c in range(3):
        mais += tabuleiro[casa[0]][c]
        if mais == 2:
            return True
    mais = 0
    for l in range(3):
        mais += tabuleiro[l][casa[1]]
        if mais == 2:
            return True
    mais = 0

    if casa[0] == 0 and casa[1] == 0:
        mais = tabuleiro[1][1] + tabuleiro[2][2]
        if mais == 2:
            return True
    mais = 0
    if casa[0] == 0 and casa[1] == 2:
        mais = tabuleiro[1][1] + tabuleiro[2][0]
        if mais == 2:
            return True
    mais = 0
    if casa[0] == 2 and casa[1] == 0:
        mais = tabuleiro[1][1] + tabuleiro[0][2]
        if mais == 2:
            return True
    mais = 0
    if casa[0] == 2 and casa[1] == 2:
        mais = tabuleiro[1][1] + tabuleiro[0][0]
        if mais == 2:
            return True
    mais = 0
    if casa[0] == 1 and casa[1] == 1:
        mais = tabuleiro[0][0] + tabuleiro[2][2]
        if mais == 2:
            return True
    mais = 0
    if casa[0] == 1 and casa[1] == 1:
        mais = tabuleiro[2][0] + tabuleiro[0][2]
        if mais == 2:
            return True
    return False


def melhor_jogada(vazias):

    if [1, 1] in vazias:
        return [1, 1]

    pos = randint(0, len(vazias)-1)
    return vazias[pos]
