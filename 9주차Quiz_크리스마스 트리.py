# 사용자로부터 크리스마스 트리의 높이를 입력받기
height = int(input("크리스마스 트리의 높이를 설정하세요: "))

# 크리스마스 트리 출력
for i in range(1, height + 1):
    spaces = " " * (height - i)  # 공백 생성
    stars = "*" * (2 * i - 1)  # 별 생성
    print(spaces + stars)

# 크리스마스 트리의 기둥 출력
base_spaces = " " * (height - 1)
base_stem = "|"
print(base_spaces + base_stem)
