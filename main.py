class EntradaInvalida(Exception):
    pass


class OperacaoInvalida(Exception):
    pass


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def soma_digitos(numero):
    if numero < 10:
        return numero
    return numero % 10 + soma_digitos(numero // 10)


def processar_operacao(linha):
    dados = linha.split()

    if not dados:
        raise EntradaInvalida()

    operacao = dados[0]

    if operacao == "M":
        if len(dados) != 3:
            raise EntradaInvalida()

        try:
            a = int(dados[1])
            b = int(dados[2])
        except ValueError:
            raise EntradaInvalida()

        if a <= 0 or b <= 0:
            raise EntradaInvalida()

        return f"MDC = {mdc(a, b)}"

    elif operacao == "S":
        if len(dados) != 2:
            raise EntradaInvalida()

        try:
            numero = int(dados[1])
        except ValueError:
            raise EntradaInvalida()

        if numero < 0:
            raise EntradaInvalida()

        return f"SOMA = {soma_digitos(numero)}"

    else:
        raise OperacaoInvalida()


def main():
    try:
        q = int(input())

        if q < 1:
            raise EntradaInvalida()

        for _ in range(q):
            linha = input()
            resultado = None

            try:
                resultado = processar_operacao(linha)

            except EntradaInvalida:
                resultado = "ERRO: EntradaInvalida"

            except OperacaoInvalida:
                resultado = "ERRO: OperacaoInvalida"

            finally:
                if resultado is not None:
                    print(resultado)

    except ValueError:
        print("ERRO: EntradaInvalida")

    except EntradaInvalida:
        print("ERRO: EntradaInvalida")


if __name__ == "__main__":
    main()