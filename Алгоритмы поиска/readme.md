# Алгоритмы поиска на Python

## Линейный поиск
### Содержание:
инейный поиск — это один из самых простых и понятных алгоритмов поиска. Мы можем думать о нем как о расширенной версии нашей собственной реализации оператора in в Python.

Суть алгоритма заключается в том, чтобы перебрать массив и вернуть индекс первого вхождения элемента, когда он найден:

def LinearSearch(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1
Итак, если мы используем функцию для вычисления:

>>> print(LinearSearch([1,2,3,4,5,2,1], 2))
То получим следующий результат:

1
Это индекс первого вхождения искомого элемента, учитывая, что нумерация элементов в Python начинается с нуля.

Временная сложность линейного поиска равна O(n). Это означает, что время, необходимое для выполнения, увеличивается с увеличением количества элементов в нашем входном списке lys.

Линейный поиск не часто используется на практике, потому что такая же эффективность может быть достигнута с помощью встроенных методов или существующих операторов. К тому же, он не такой быстрый и эффективный, как другие алгоритмы поиска.

Линейный поиск хорошо подходит для тех случаев, когда нам нужно найти первое вхождение элемента в несортированной коллекции. Это связано с тем, что он не требует сортировки коллекции перед поиском (в отличие от большинства других алгоритмов поиска).

## Интерполяционный поиск
### Содержание:

Интерполяционный поиск — это еще один алгоритм «разделяй и властвуй», аналогичный бинарному поиску. В отличие от бинарного поиска, он не всегда начинает поиск с середины. Интерполяционный поиск вычисляет вероятную позицию искомого элемента по формуле:

index = low + [(val-lys[low])*(high-low) / (lys[high]-lys[low])]
В этой формуле используются следующие переменные:

lys — наш входной массив.
val — искомый элемент.
index — вероятный индекс искомого элемента. Он вычисляется как более высокое значение, когда значение val ближе по значению к элементу в конце массива (lys[high]), и более низкое, когда значение val ближе по значению к элементу в начале массива (lys[low]).
low — начальный индекс массива.
high — последний индекс массива.
Алгоритм осуществляет поиск путем вычисления значения индекса:

Если значение найдено (когда lys[index] == val), возвращается индекс.
Если значение val меньше lys[index], то значение индекса пересчитывается по формуле для левого подмассива.
Если значение val больше lys[index], то значение индекса пересчитывается по формуле для правого подмассива.

Если у нас большое количество элементов и наш индекс не может быть вычислен за одну итерацию, то мы продолжаем пересчитывать значение индекса после корректировки значений high и low.

Временная сложность интерполяционного поиска равна O(log log n), когда значения распределены равномерно. Если значения распределены неравномерно, временная сложность для наихудшего случая равна O(n) — так же, как и для линейного поиска.

Интерполяционный поиск лучше всего работает на равномерно распределенных, отсортированных массивах. В то время как бинарный поиск начинает поиск с середины и всегда делит массив на две части, интерполяционный поиск вычисляет вероятную позицию элемента и проверяет индекс, что повышает вероятность нахождения элемента за меньшее количество итераций.

## Jump Search поиск
### Содержание:
Jump Search похож на бинарный поиск тем, что он также работает с отсортированным массивом и использует аналогичный подход «разделяй и властвуй» для поиска по нему.

Его можно классифицировать как усовершенствованный алгоритм линейного поиска, поскольку он зависит от линейного поиска для выполнения фактического сравнения при поиске значения.

В заданном отсортированном массиве мы ищем не постепенно по элементам массива, а скачкообразно. Если у нас есть размер прыжка, то наш алгоритм будет рассматривать элементы входного списка lys в следующем порядке: lys[0], lys[0+jump], lys[0+2jump], lys[0+3jump] и так далее.

С каждым прыжком мы сохраняем предыдущее значение и его индекс. Когда мы находим множество значений (блок), где lys[i] < element < lys[i + jump], мы выполняем линейный поиск с lys[i] в качестве самого левого элемента и lys[i + jump] в качестве самого правого элемента 


Поскольку это сложный алгоритм, давайте рассмотрим пошаговое вычисление для следующего примера:

>>> print(JumpSearch([1,2,3,4,5,6,7,8,9], 5))
Jump search сначала определит размер прыжка путем вычисления math.sqrt(len(lys)). Поскольку у нас 9 элементов, размер прыжка будет √9 = 3.
Далее мы вычисляем значение переменной right. Оно рассчитывается как минимум из двух значений: длины массива минус 1 и значения left + jump, которое в нашем случае будет 0 + 3 = 3. Поскольку 3 меньше 8, мы используем 3 в качестве значения переменной right.
Теперь проверим, находится ли наш искомый элемент 5 между lys[0] и lys[3]. Поскольку 5 не находится между 1 и 4, мы идем дальше.
Затем мы снова делаем расчеты и проверяем, находится ли наш искомый элемент между lys[3] и lys[6], где 6 — это 3 + jump. Поскольку 5 находится между 4 и 7, мы выполняем линейный поиск по элементам между lys[3] и lys[6] и возвращаем индекс нашего элемента: 4

Временная сложность jump search равна O(√n), где √n — размер прыжка, а n — длина списка. Таким образом, с точки зрения эффективности jump search находится между алгоритмами линейного и бинарного поиска.

Единственное наиболее важное преимущество jump search по сравнению с бинарным поиском заключается в том, что он не опирается на оператор деления (/).

В большинстве процессоров использование оператора деления является дорогостоящим по сравнению с другими основными арифметическими операциями (сложение, вычитание и умножение), поскольку реализация алгоритма деления является итеративной.

Стоимость сама по себе очень мала, но когда количество искомых элементов очень велико, а количество необходимых операций деления растет, стоимость может постепенно увеличиваться. Поэтому jump search лучше бинарного поиска, когда в системе имеется большое количество элементов: там даже небольшое увеличение скорости имеет значение.

Чтобы ускорить jump search, мы могли бы использовать бинарный поиск или какой-нибудь другой алгоритм для поиска в блоке вместо использования гораздо более медленного линейного поиска.

## Экспоненциальный поиск
### Содержание:
Экспоненциальный поиск — это еще один алгоритм поиска, который может быть достаточно легко реализован на Python, по сравнению с jump search и поиском Фибоначчи, которые немного сложны. Он также известен под названиями galloping search, doubling search и Struzik search.

Экспоненциальный поиск зависит от бинарного поиска для выполнения окончательного сравнения значений. Алгоритм работает следующим образом:

Определяется диапазон, в котором, скорее всего, будет находиться искомый элемент.
В этом диапазоне используется двоичный поиск для нахождения индекса элемента.

Используем функцию, чтобы найти значение:

>>> print(ExponentialSearch([1,2,3,4,5,6,7,8],3))
Рассмотрим работу алгоритма пошагово.

Проверяем, соответствует ли первый элемент списка искомому значению: поскольку lys[0] равен 1, а мы ищем 3, мы устанавливаем индекс равным 1 и двигаемся дальше.
Перебираем все элементы в списке, и пока элемент с текущим индексом меньше или равен нашему значению, умножаем  значение индекса на 2:
index = 1, lys[1] равно 2, что меньше 3, поэтому значение index умножается на 2 и переменной index присваивается значение 2.
index = 2, lys[2] равно 3, что равно 3, поэтому значение index умножается на 2 и переменной index присваивается значение 4.
index = 4, lys[4] равно 5, что больше 3. Условие выполнения цикла больше не соблюдается и цикл завершает свою работу.
Затем выполняется двоичный поиск в полученном диапазоне (срезе) lys[:4]. В Python это означает, что подсписок будет содержать все элементы до 4-го элемента, поэтому мы фактически вызываем функцию следующим образом:
>>> BinarySearch([1,2,3,4], 3)
Функция вернет следующий результат:

2
Этот результат является индексом искомого элемента как в исходном списке, так и в срезе, который мы передаем алгоритму бинарного поиска.

Экспоненциальный поиск выполняется за время O(log i), где i — индекс искомого элемента. В худшем случае временная сложность равна O(log n), когда искомый элемент — это последний элемент в массиве (n — это длина массива).

Экспоненциальный поиск работает лучше, чем бинарный, когда искомый элемент находится ближе к началу массива. На практике мы используем экспоненциальный поиск, поскольку это один из наиболее эффективных алгоритмов поиска в неограниченных или бесконечных массивах.

## Бинарный поиск
### Содержание:
Бинарный поиск работает по принципу «разделяй и властвуй». Он быстрее, чем линейный поиск, но требует, чтобы массив был отсортирован перед выполнением алгоритма.

Предполагая, что мы ищем значение val в отсортированном массиве, алгоритм сравнивает val со значением среднего элемента массива, который мы будем называть mid.

Если mid — это тот элемент, который мы ищем (в лучшем случае), мы возвращаем его индекс.
Если нет, мы определяем, в какой половине массива мы будем искать val дальше, основываясь на том, меньше или больше значение val значения mid, и отбрасываем вторую половину массива.
Затем мы рекурсивно или итеративно выполняем те же шаги, выбирая новое значение для mid, сравнивая его с val и отбрасывая половину массива на каждой итерации алгоритма.
Алгоритм бинарного поиска можно написать как рекурсивно, так и итеративно. В Python рекурсия обычно медленнее, потому что она требует выделения новых кадров стека.

Если мы используем функцию для вычисления:

>>> BinarySearch([10,20,30,40,50], 20)
То получим следующий результат, являющийся индексом искомого значения:

1
На каждой итерации алгоритм выполняет одно из следующих действий:

Возврат индекса текущего элемента.
Поиск в левой половине массива.
Поиск в правой половине массива.
Мы можем выбрать только одно действие на каждой итерации. Также на каждой итерации наш массив делится на две части. Из-за этого временная сложность двоичного поиска равна O(log n).

Одним из недостатков бинарного поиска является то, что если в массиве имеется несколько вхождений элемента, он возвращает индекс не первого элемента, а  ближайшего к середине:

>>> print(BinarySearch([4,4,4,4,4], 4))
После выполнения этого фрагмента кода будет возвращен индекс среднего элемента:

2
Для сравнения: выполнение линейного поиска по тому же массиву вернет индекс первого элемента:

0
Однако мы не можем категорически утверждать, что двоичный поиск не работает, если массив содержит дубликаты. Он может работать так же, как линейный поиск, и в некоторых случаях возвращать первое вхождение элемента. Например:

>>> print(BinarySearch([1,2,3,4,4,4,5], 4))
3
Бинарный поиск довольно часто используется на практике, потому что он эффективен и быстр по сравнению с линейным поиском. Однако у него есть некоторые недостатки, такие как зависимость от оператора //. Существует много других алгоритмов поиска, работающих по принципу «разделяй и властвуй».


## Поиск Фибоначчи
### Содержание:

Поиск Фибоначчи — это еще один алгоритм «разделяй и властвуй», который имеет сходство как с бинарным поиском, так и с jump search. Он получил свое название потому, что использует числа Фибоначчи для вычисления размера блока или диапазона поиска на каждом шаге.

Числа Фибоначчи  — это последовательность чисел 0, 1, 1, 2, 3, 5, 8, 13, 21 …, где каждый элемент является суммой двух предыдущих чисел.

Алгоритм работает с тремя числами Фибоначчи одновременно. Давайте назовем эти три числа fibM, fibM_minus_1 и fibM_minus_2. Где fibM_minus_1 и fibM_minus_2 — это два числа, предшествующих fibM в последовательности:

fibM = fibM_minus_1 + fibM_minus_2

Мы инициализируем значения 0, 1, 1 или первые три числа в последовательности Фибоначчи. Это поможет нам избежать  IndexError в случае, когда наш массив lys содержит очень маленькое количество элементов.

Затем мы выбираем наименьшее число последовательности Фибоначчи, которое больше или равно числу элементов в нашем массиве lys, в качестве значения fibM. А два числа Фибоначчи непосредственно перед ним — в качестве значений fibM_minus_1 и fibM_minus_2. Пока в массиве есть элементы и значение fibM больше единицы, мы:

Сравниваем val со значением блока в диапазоне до fibM_minus_2 и возвращаем индекс элемента, если он совпадает.
Если значение больше, чем элемент, который мы в данный момент просматриваем, мы перемещаем значения fibM, fibM_minus_1 и fibM_minus_2 на два шага вниз в последовательности Фибоначчи и меняем индекс на индекс элемента.
Если значение меньше, чем элемент, который мы в данный момент просматриваем, мы перемещаем значения fibM, fibM_minus_1 и fibM_minus_2 на один шаг вниз в последовательности Фибоначчи.

Используем функцию FibonacciSearch для вычисления:

>>> print(FibonacciSearch([1,2,3,4,5,6,7,8,9,10,11], 6))
Давайте посмотрим на пошаговый процесс поиска:

Присваиваем переменной fibM наименьшее число Фибоначчи, которое больше или равно длине списка. В данном случае наименьшее число Фибоначчи, отвечающее нашим требованиям, равно 13.
Значения присваиваются следующим образом:
           fibM = 13

           fibM_minus_1 = 8

           fibM_minus_2 = 5

           index = -1

Далее мы проверяем элемент lys[4], где 4 — это минимум из двух значений — index + fibM_minus_2 (-1+5) и длина массива минус 1 (11-1). Поскольку значение lys[4] равно 5, что меньше искомого значения, мы перемещаем числа Фибоначчи на один шаг вниз в последовательности, получая следующие значения:
           fibM = 8

           fibM_minus_1 = 5

           fibM_minus_2 = 3

           index = 4

Далее мы проверяем элемент lys[7], где 7 — это минимум из двух значений: index + fibM_minus_2 (4 + 3) и длина массива минус 1 (11-1). Поскольку значение lys[7] равно 8, что больше искомого значения, мы перемещаем числа Фибоначчи на два шага вниз в последовательности, получая следующие значения: 
           fibM = 3

           fibM_minus_1 = 2

           fibM_minus_2 = 1

           index = 4

Затем мы проверяем элемент lys[5], где 5 — это минимум из двух значений: index + fibM_minus_2 (4+1) и длина массива минус 1 (11-1) . Значение lys[5] равно 6, и это наше искомое значение!
Получаем ожидаемый результат:

5
Временная сложность поиска Фибоначчи равна O(log n). Она такая же, как и у бинарного поиска. Это означает, что алгоритм в большинстве случаев работает быстрее, чем линейный поиск и jump search.

Поиск Фибоначчи можно использовать, когда у нас очень большое количество искомых элементов и мы хотим уменьшить неэффективность, связанную с использованием алгоритма, основанного на операторе деления.

Дополнительным преимуществом использования поиска Фибоначчи является то, что он может вместить входные массивы, которые слишком велики для хранения в кэше процессора или ОЗУ, потому что он ищет элементы с увеличивающимся шагом, а не с фиксированным.

