import random
from cartas import baralho

def jogar():
    print("=== SUPER TRUNFO ===")
    jogador = random.choice(baralho)
    computador = random.choice(baralho)

    print("\nSua carta é:")
    for atributo, valor in jogador.items():
        print(f"{atributo}: {valor}")

    escolha = input("\nQual atributo você escolhe? ").strip().lower()

    if escolha not in jogador:
        print("Atributo inválido!")
        return

    print(f"\nComputador escolheu a carta: {computador}")

    if jogador[escolha] > computador[escolha]:
        print("\n🎉 Você venceu!")
    elif jogador[escolha] < computador[escolha]:
        print("\n😢 Você perdeu!")
    else:
        print("\n🤝 Empate!")

if __name__ == "__main__":
    jogar()
