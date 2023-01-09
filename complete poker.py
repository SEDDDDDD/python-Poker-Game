#----------------모듈 불러오기
import random
import time
import os

def clear():
    command = 'cls'
    os.system(command)                  #터미널 화면 clear
print(f"-----------------------------------------------------------------------------------------")
print(f"-------------------------------FIVE-STUD-POKER-------------------------------------------")
print(f"-----------------------------------------------------------------------------------------")

start = input("                          시작 하겠습니까? ( Y or N ) : ")

clear()
time.sleep(1)

if start == ("Y" and "y"):
    print(f"-----------------------------------------------------------------------------------------\n"
          f"                               게임을 시작합니다.\n"
          f"-----------------------------------------------------------------------------------------")
    time.sleep(2)
    clear()
else:
    print(f"-----------------------------------------------------------------------------------------\n"
          f"                               게임을 종료합니다.\n"
          f"-----------------------------------------------------------------------------------------")
    time.sleep(1)
    clear()
    exit()

while True:
    #돈 지급
    myMoney = 1000000
    ComMoney = 1000000

    #첫 베팅금 500
    myMoney -= 5000
    ComMoney -= 5000
    #누적 베팅금
    totalBetMoney = 1000



    print(f"게임 시작전 돈 100000원을 지급합니다.")
    time.sleep(1)
    print(f"카드를 생성합니다.")
    time.sleep(1)
    print(f"카드를 섞습니다.")


    deck = []
    for c in ["c", "d", "h", "s"]:  # c : 클로버, d = 다이아, h = 하트, s = 스페이드
        for i in range(1, 14):  # (문양, 번호) 식의 튜플로 카드 생성하여 deck 리스트에 넣음
            deck.append((c, i))  # J, Q, K 는  11, 12, 13 으로 대체 ("s", 12) : 스페이드Q

    for i in range(10):                     #카드가 충분히 섞이도록 10번 반복1
        random.shuffle(deck)

    def StartAction(a, b):
        for i in range(2):                              # 플레이어한테 deck 의 1,2 번째 카드 지급
            a.append(deck[i])                 # COM 한테 deck 의 3,4번재 카드지급(1,2번째는 플레이어가 가져갔기때문)
            b.append(deck[i+2])
        del deck[0:4]                                   #지급된 카드 삭제

    card_player = []  # 플레이어 카드덱
    COM = []  # COM 카드

    StartAction(card_player, COM)

    def oneCardAction(a, b):                # 카드 1장씩 돌리기
        for i in range(1):
            a.append(deck[i])
            b.append(deck[i+1])
        del deck[0:2]

    def comBetChoice(card_name):
        cardNum = []  # 카드 숫자값 list 초기화
        cardShape = []  # 카드 모양값 list 초기화

        for i in range(len(card_name)):
            cardNum.append(card_name[i][1])  # 카드 첫번째~다섯번째 카드 까지의 숫자 값만 cardNum 에 담는다.
            cardShape.append(card_name[i][0])
        cardNum.sort()
        if len(card_name) <= 5:  # 카드가 5장이 아닐경우 아직 패를 돌리고 배팅을 더 진행해야 하기 때문에 if 문으로 진행 방향을 나눔
            pair = 0
            shape = 0

            for num1 in range(len(card_name) - 1):
                for num2 in range(num1 + 1, len(card_name)):
                    if cardNum[num1] == cardNum[num2]:  # num1 번째 카드와 num2 번째 카드 숫자 비교
                        pair += 1
                    if cardShape[num1] == cardShape[num2]:  # num1 번째 카드와 num2 번째 카드 모양 비교
                        shape += 1
            if (pair == 1 or 0) or (shape == 1 or 0):  # 갖고 있는 카드 조합이 하이카드 or 원페어 일때 Check 값 리턴
                COM_check = 1

            elif pair >= 3 or shape >= 3:  # 갖고 있는 카드 조합이 최소 트리플 이상일 경우 Raise 값 리턴
                COM_check = 2

            else:
                COM_check = random.randint(3, 100)  # 카드 덱이 족보에 없다면 난수 값 리턴
            return COM_check


    # 플레이어 및 컴퓨터 베팅, 최초 2장의 카드 지급 후 게임이 계속 진행 됬을 시 총 3번의 카드를 더 지급해야하기 때문에 3번 반복 진행
    # 베팅 진행 중 플레이어나 컴퓨터가 fold 를 선택했을 시 그대로 게임은 끝나고 다시 시작 할지 선택 메세지 출력
    for i in range(3):
        playerBetChoice = int(input(
            f"-----------------------------------------------------------------------------------------\n"
            f"---------------PLYAER : {card_player}\n"
            f"---------------COM : {COM}\n-----------------------------------------------------------------------------------------\n"
            f"베팅 하세요. 현재 누적 베팅액 {totalBetMoney}원 \n"
            f" 1 : Check \n 2 : Raise \n 3 : Fold \n 번호 입력 : "))
        clear()

            # 1번을 고를 경우 check 선택 메세지 출력
        if playerBetChoice == 1:
            print("Player 가 Check 를 선택했습니다.")
            time.sleep(0.5)

            # 2번을 고를 경우 raise 선택 메세지 출력
        elif playerBetChoice == 2:
            # raise를 고를 경우, 총 베팅금액의 1.5배에 해당하는 금액 베팅
            print(f"Player 가 Raise 를 선택했습니다. "
                  f"\n\n{int(totalBetMoney * 1.5)}원 을 베팅합니다.\n")
            myMoney -= int(totalBetMoney * 1.5)                         # 베팅 금액만큼 내 돈에서 차감
            totalBetMoney += int(totalBetMoney * 1.5)                   # 베팅금을 총 베팅금에 더함
            time.sleep(1)

            # 3번을 고를 경우 Player Fold(기권) 출력
        elif playerBetChoice == 3:
            print(f"Player 가 Fold 를 선택했습니다.")
            time.sleep(1)
            break

        COM_choice = comBetChoice(COM)

        #컴퓨터 베팅
            # 컴퓨터 배팅 함수의 값이 1 or 2 or 3 이거나 난수로 출력되어 해당범위에 있을 경우
            # Check, Raise, Fold 출력
            # 배팅 순서가 Player - > COM 이기때문에 COM 배팅후 총 누적 배팅액 및 남은 소지금 출력
        if (COM_choice == 1) or (3 <= COM_choice < 40):
            print("COM 이 Check 를 선택했습니다.\n")
            print(f"현재 보유금 : {myMoney}원\n\n총 누적 베팅액 : {totalBetMoney}원\n")
            print("베팅이 끝났습니다.\n카드를 한장씩 돌립니다.")
            time.sleep(1)
            oneCardAction(card_player, COM)

        elif (COM_choice == 2) or (41 <= COM_choice < 80):
            print(f"COM 이 Raise 를 선택했습니다. \n {int(totalBetMoney * 1.5)}원 을 베팅합니다.")  # totalBetMoney 의 1.5배
            ComMoney -= int(totalBetMoney * 1.5)
            totalBetMoney += int(totalBetMoney * 1.5)
            print(f"현재 보유금 : {myMoney}원\n총 누적 베팅액 : {totalBetMoney}원\n")
            print("베팅이 끝났습니다.\n카드를 한장씩 돌립니다.")
            time.sleep(1)
            oneCardAction(card_player, COM)

        elif 81 <= COM_choice <= 100:
            print(f"COM 이 Fold 를 선택했습니다.")
            break

    # 컴퓨터 기권 시 플레이어 승리 출력 및 베팅금 회수, 더 할지 묻는 메세지 출력
    if 81 <= COM_choice <= 100:
        print(f"COM 의 Fold(기권) (으)로 Player의 승리")
        myMoney = myMoney + totalBetMoney
        print(f"승리 상금 {totalBetMoney}원\n"
              f"총 보유금 : {myMoney}원\n")

        ask = input("게임을 더 하시겠습니까? (y/n)")
        if ask == "y" or ask == "Y":
            continue
        else:
            break

    # 플레이어 기권 시 위와 반대로 진행
    if playerBetChoice == 3:
        print(f"Playerd 의 Fold(기권) (으)로 COM 의 승리")
        ComMoney = ComMoney + totalBetMoney

        time.sleep(1)
        print(f"총 베팅금 {totalBetMoney}원은 소멸 됩니다.\n")
        ask = input("게임을 더 하시겠습니까? (y/n)")
        if ask == "y" or ask == "Y":
            continue
        else:
            break

    def cardHandRank(card_name):  # 카드 족보 함수 생성
            cardNum = []  # 카드 숫자값 list 초기화
            cardShape = []  # 카드 모양값 list 초기화
            for i in range(5):
                cardNum.append(card_name[i][1])  # 카드 첫번째~다섯번째 카드 까지의 숫자 값만 cardNum 에 담는다.
                cardShape.append(card_name[i][0])
            cardNum.sort()
            pair = 0  # 숫자가 같은 카드가 몇 쌍인지 의미하는 pair 값 초기화
            shape = 0  # 모양이 같은 카드가 몇 쌍인지 의미하는 shape 값 초기화
            for num1 in range(4):
                for num2 in range(num1 + 1, 5):  # 한장의 카드와 나머지 카드를 비교하기 위해서 range(num1+1, 5)로 작성
                    if cardNum[num1] == cardNum[num2]:  # num1 번째 카드와 num2 번째 카드 숫자 비교
                        pair += 1
                    if cardShape[num1] == cardShape[num2]:  # num1 번째 카드와 num2 번째 카드 모양 비교
                        shape += 1
            if cardNum[4] - cardNum[0] == 4:  # 카드 5장의 숫자 중 가장큰 수 - 가장 작은수 = 4 라면 스트레이트
                rank = 6  # 스트레이트 ( 숫자가 순서대로 )
                rankHand = "스트레이트"
                if shape == 10:
                    rank = 2  # 스트레이트 플러쉬 ( 모양이 같고 숫자가 순서대로 )
                    rankHand = "스트레이트 플러쉬"
            elif cardNum[4] - cardNum[0] == 12 & \
                    shape == 10 & \
                    cardShape.count("s") == 5:
                rank = 1  # 로얄 스트레이트 플러쉬
                rankHand = "로얄 스트레이트 플러쉬"
                # 가장 큰수에서 가장 작은 수를 뺀값이 12 이고,
                # 모양이 5장 모두 같으며
                # 그 모양이 "s" 스페이드인 경우
            elif pair == 6:
                rank = 3  # 포카드( 같은 숫자 4장 )
                rankHand = "포카드"
            elif pair == 4:
                rank = 4  # 풀하우스 ( 같은모양 3장 & 2장 )
                rankHand = "풀하우스"
            elif shape == 10:
                rank = 5  # 플러쉬 ( 5장 같은 모양 )
                rankHand = "플러쉬"
            elif pair == 3:
                rank = 7  # 트리플 ( 같은 숫자 3장 )
                rankHand = "트리플"
            elif pair == 2:
                rank = 8  # 투페어 ( 같은 숫자 2장 )
                rankHand = "투페어"
            elif pair == 1:
                rank = 9  # 원페어 ( 같은 숫자 1장 )
                rankHand = "원페어"
            else:
                rank = 10  # 하이카드 ( 족보에 없는 카드 )
                rankHand = "하이카드"

            return rank, rankHand  # 족보에 맞는 랭크 값을 리턴

    rank_player = cardHandRank(card_player)
    rank_COM = cardHandRank(COM)

    # 컴퓨터의 마지막 5번쨰 카드는 hidden 카드로 숨김 모든 베팅이 끝난 후 공개 하도록 CHC변수에 5번 카드값만 할당 해놓음
    CHC = COM[4]
    COM[4] = "hidden"

    #서로의 카드패가 총 5장일때 마지막 베팅 진행 코드
    if len(card_player) == 5:
        playerBetChoice = int(input(
            f"-----------------------------------------------------------------------------------------\n"
            f"---------------PLYAER : {card_player}\n"
            f"---------------COM : {COM}\n-----------------------------------------------------------------------------------------\n"
            f"베팅 하세요. 현재 누적 베팅액 {totalBetMoney}원 \n"
            f" 1 : Check \n 2 : Raise \n 3 : Fold \n 번호 입력 : "))
        clear()
        if playerBetChoice == 1:
            print("Player 가 Check 를 선택했습니다.")
            time.sleep(0.5)

        elif playerBetChoice == 2:
            print(f"Player 가 Raise 를 선택했습니다. "
                  f"\n{int(totalBetMoney * 1.5)}원 을 베팅합니다.\n")
            myMoney -= int(totalBetMoney * 1.5)
            totalBetMoney += int(totalBetMoney * 1.5)
            time.sleep(1)

        elif playerBetChoice == 3:
            print(f"Player 가 Fold 를 선택했습니다.")
            time.sleep(1)
            break

    # 마지막 베팅 후 서로의 카드패 공개를 위해 숨겨두었던 hidden 카드 원상 복구
    COM[4] = CHC
    COM_choice = comBetChoice(COM)


    # COM 의 카드덱이 족보에 없을때 무조건 fold 가 나오지 않고 random 함수를 이용한 난수를 돌려
    # 4:4:2 비율로 check : raise : fold 선택지를 구분

    if (COM_choice == 1) or (3 <= COM_choice < 40):
        print("COM 이 Check 를 선택했습니다.")
        print("베팅이 끝났습니다.")
        time.sleep(1)

    elif (COM_choice == 2) or (41 <= COM_choice < 80):
        print(f"COM 이 Raise 를 선택했습니다. \n {int(totalBetMoney * 1.5)}원 을 베팅합니다.")  # totalBetMoney 의 1.5배
        myMoney -= int(totalBetMoney * 1.5)
        totalBetMoney += int(totalBetMoney * 1.5)
        print(f"현재 잔액 : {myMoney}원\n총 누적 베팅액 : {totalBetMoney}원\n")
        print("베팅이 끝났습니다.")
        time.sleep(1)

    elif 81 <= COM_choice <= 100:
        print(f"COM 이 Fold 를 선택했습니다.")

    if 81 <= COM_choice <= 100:
        ask = input("게임을 더 하시겠습니까? (y/n)")
        if ask == "y" or ask == "Y":
            continue
        else:
            break

    #마지막 서로의 패와 족보 값을 출력
    print(f"------------------------------------------------------------------------------------------------------\n"
            f"---------------PLYAER : {card_player} ({rank_player[1]})\n"
            f"---------------COM : {COM} ({rank_COM[1]})\n"
          f"------------------------------------------------------------------------------------------------------\n")

    # 위의 족보 함수에서 나온 rank 값을 기준으로 더 낮은 값을 가진 상대가 승리메세지 출력
    def compareRank(a, b):
        if a < b:
            print(f"Player (이)가 이겼습니다!")

        elif a > b:
            print(f"COM (이)가 이겼습니다!")

        elif a == b:
            print(f"무승부 입니다.")

    print(f"플레이어 : {rank_player[1]}\n"
          f"COM : {rank_COM[1]}")


    time.sleep(1)

    compareRank(rank_player, rank_COM)          #player 패와 내패를 비교

    ask = input("게임을 더 하시겠습니까? (y/n)")
    if ask == "n" or ask == "N":
        break
