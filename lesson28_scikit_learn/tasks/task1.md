# Міні-завдання: інший датасет, ті самі підходи

**Тема:** закріплення KNN-класифікації та лінійної регресії у scikit-learn
**Тривалість:** 30–40 хв на парі

## Частина A — KNN на датасеті **Wine**

Класифікуємо вид вина за базовими хімічними вимірами.

1. Завантажте дані:

   ```python
   from sklearn import datasets
   wine = datasets.load_wine()
   X = wine.data[:, [1, 9]]  # malic_acid, color_intensity
   y = wine.target
   ```
   Подивіться на датасет та визначте яка у нього структура    

2. Розділіть датасет: **Для цього можна скористатися функцією train_test_split із scikit-learn**.

   ```python
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=50, random_state=42, shuffle=True)
   ```
3. Навчіть **KNeighborsClassifier** із кількома значеннями `k` (наприклад, 3, 5, 7). Для кожного `k`:

   * `fit` на тренуванні;
   * `score` на тесті (це accuracy);
4. Візуалізації:

   * **Scatter** точок тесту: вісь X — malic_acid, вісь Y — color_intensity, wine.target — **істинний** клас `y_test`.
   * **Bar chart** точності для різних `k`.

💡 Підказка (фрагменти, не повний розв’язок)

```python
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

ks = [1, 2, 3, 5, 7, 10]
acc = []
for k in ks:
    knn = KNeighborsClassifier(n_neighbors=k)
    # TODO підставити дані в класифікатор створений вище (метод .fit(X, y))
    # TODO виміряти точність за допомогою метода .score(X, y)
# TODO: scatter X_test[:,0] vs X_test[:,1], колір = y_test
# TODO: побудувати стовпчикову діаграму точності для ks
```