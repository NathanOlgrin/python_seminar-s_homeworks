# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in range (False,True+1):
    for j in range (False,True+1):
        for k in range (False,True+1):
            left = not(i or j or k)
            right = not i and not j and not k
            if left==right:
                print(f'Утверждение истинно для X={i} Y={j} Z={k}')