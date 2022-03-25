print("0~1 사이의 소숫값을 0~255의 RGB 값으로 변환하는 프로그램입니다\n종료 명령어(exit)를 입력하기 전까지 무한 반복됩니다\n도움말 : help 입력")
terminate = 1 #종료
mode = 0 #0~1을 0~255로 / 0~255를 0~1로 변환하는 모드 셀렉트 (0은 0~1, 1은 0~255)

while(terminate) :
    mode = 0
    a = input(" : ")
    b = a.split(", ")
    if(a == "exit") :
        terminate = 0
        break
    elif(a == "help") :
        print("\n입력 방법의 예시는 다음과 같습니다 | ex) 0.06, 0.43, 0.92, 1.0\n\n숫자 여러개를 동시에 입력 할 경우 쉼표와 띄어쓰기로 구분해주세요 | ex) 192, 168, 1, 1\n\n0~1 -> 0~255 | 0~255 -> 0~1 양방향 변환 가능합니다\n\n정보 : info 입력\n종료 : exit 입력")
    elif(a == "info") :
        print("[ZAPHKIEL(포루누키)/CC BY] 이 프로그램은 크리에이티브 커먼즈 [저작권 표시 대한민국 라이선스] 에 따라 자유롭게 이용 할 수 있습니다")
    else :
        try :
            for j in range(len(b)) :
                b[j] = float(b[j])
                if (b[j] > 1) :
                    mode = 1
            for i in range(len(b)) :
                b[i] = float(b[i])
                if (mode != 0) :
                    b[i] = b[i]/255
                    print(round(b[i], 3))
                else :
                    b[i] = b[i]*255
                    print(round(b[i], 3))
        except ValueError :
            print("ValueError\n다시 입력해주세요")
        except IndexError :
            print("IndexError\n다시 입력해주세요")
        except TypeError :
            print("TypeError\n다시 입력해주세요")
