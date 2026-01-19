# xox.py

tahta = [" " for _ in range(9)]

def tahta_yazdir():
    print()
    print(f" {tahta[0]} | {tahta[1]} | {tahta[2]} ")
    print("---+---+---")
    print(f" {tahta[3]} | {tahta[4]} | {tahta[5]} ")
    print("---+---+---")
    print(f" {tahta[6]} | {tahta[7]} | {tahta[8]} ")
    print()

def kazanan_var_mi(oyuncu):
    kazanma_kombinasyonlari = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in kazanma_kombinasyonlari:
        if tahta[a] == tahta[b] == tahta[c] == oyuncu:
            return True
    return False

def beraberlik_mi():
    return " " not in tahta

oyuncu = "X"

while True:
    tahta_yazdir()
    print(f"Sıra: {oyuncu}")

    try:
        hamle = int(input("Hamle (1-9): ")) - 1
        if tahta[hamle] != " ":
            print("⚠️ Burası dolu!")
            continue
        tahta[hamle] = oyuncu
    except:
        print("⚠️ Geçersiz giriş!")
        continue

    if kazanan_var_mi(oyuncu):
        tahta_yazdir()
        print(f"🎉 {oyuncu} kazandı!")
        break

    if beraberlik_mi():
        tahta_yazdir()
        print("🤝 Beraberlik!")
        break

    oyuncu = "O" if oyuncu == "X" else "X"
