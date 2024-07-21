# Python. Функция трансформации T(n: int) -> int выполняется 5 минут. N - список типа int.
# Требуется вернуть список трансформированных значений N, которые больше нуля.
# Предложи решение, которое удовлетворяет следующим критериям:
# 1. в одну строчку
# 2. эффективно с точки зрения времени выполнения
# 3. не использует map()

import time


def T(n: int) -> int:
    print(f"T({n})")
    time.sleep(1)
    return 2 * n


N: list[int] = [5, 5, 5, 5, 5, 5, 5]

# [T(5), T(10), T(15), T(20), 25, 5, 10 ]

# [ T(n) for n in N if T(n)>0 ]

# [result for n, result in ((n, T(n)) for n in N) if result > 0]

# cached_results = {n: T(n) for n in set(N) }
# result_list = [cached_results[n] for n in N if cached_results[n] > 0]

# cached = {n: T(n) for n in set(N)}
# result_list = [cached[n] for n in N if cached[n] > 0]


# cached = {n: T(n) for n in set(N)}
# result_list = [cached[n] for n in N if cached[n] > 0]

# result_list = (lambda cached: [cached[n] for n in N if cached[n] > 0])({n: T(n) for n in set(N)})

# (lambda nums: [x**2 for x in nums if x > 5])(numbers)

# cached = {n: T(n) for n in set(N)}
# result_list = [cached[n] for n in N if cached[n] > 0]


# result_list = (lambda nums: [ T(i) for i in set(nums) ]  )(N)
# result_list = (lambda my_dict: [my_dict[i] for i in N if my_dict[i] > 0])({i: T(i) for i in set(N)})
#
#
# print(result_list)

# res = (lambda my_dict: [  my_dict[i]  for i in N if my_dict[i] > 0])({i: T(i) for i in set(N)})
# print(res)

print((lambda my_dict: [  my_dict[i]  for i in N if my_dict[i] > 0])({i: T(i) for i in set(N)}))