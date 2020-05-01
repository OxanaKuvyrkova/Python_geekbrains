time = int(input("Please enter your time\n"))
sec = time % 60
hour = time // 3600
min = int((time - hour * 3600 - sec) / 60)

if sec < 10:
    sec = str(f"0{sec}")
if min < 10:
    min = str(f"0{min}")
if hour < 10:
    hour = str(f"0{hour}")

print(f"{str(hour)}:{str(min)}:{str(sec)}")
