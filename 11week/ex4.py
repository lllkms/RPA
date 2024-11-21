import qrcode

name = input("이름을 입력하시오 : ")
studentcode = input("학번을 입력하시오 : ")
maior = input("전공을 입력하시오 : ")

qr_data= f"{name} {studentcode} {maior}"
qr_img =qrcode.make(qr_data)


save_path = 'my_info.data.png'
qr_img.save(save_path)

