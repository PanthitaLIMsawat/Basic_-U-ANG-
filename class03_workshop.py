monster = 100
gun = 60
sword = 30
arrow = 20
while True:
    print("จะเล่นหรือจะหนี")
    print("เลือก [1] เพื่อเล่น")
    print("เลือก [2] เพื่อหนี")
    x = int(input("กรุณากรอกเลข: "))
    if (x == 1):
        print("มาเอาชนะเจ้าmonsterกัน!!!")
        break
    elif (x == 2):
        print("ถ้าฟาร์มของแล้วมาใหม่นะ!")
        break
if (x == 1):
    round = int(input("กรุณากรอกเลขจำนวนการโจมตี: "))
    for i in range(round):
        print("จะใช้อาวุธอะไรดี")
        print("เลือก [1] เพื่อใช้ปืน")
        print("เลือก [2] เพื่อใช้ดาบ")
        print("เลือก [3] เพื่อใช้ธนู")
        w = int(input("กรุณากรอกเลข: "))
        if (w == 1):
            print("!!!")
            monster-=gun
            print("monster เลือดเหลือ",monster)
        elif (x == 2):
            print("!!")
            monster-=sword
            print("monster เลือดเหลือ",monster)
        elif (x == 3):
            print("!")
            monster-=arrow
            print("monster เลือดเหลือ",monster)
        if (monster<0):
            monster=monster*-1
            print("ตีแรงเกินไป ทำให้ปลุกพลังที่ซ่อนอยู่ของmonsterขึ้นมา monsterฮีลตัวเองจนเลือดเหลือ",monster)
    if (monster == 0):
        print("ชนะแล้ว ยินดีด้วย!!!")
    else:
        print("คุณไม่สามารถปราบmonsterได้ ทำให้คุณเป็นฝ่ายโดนmonsterคิลเอง เสียใจด้วยแต่คุณเสียชีวิตแล้ว")
    
        