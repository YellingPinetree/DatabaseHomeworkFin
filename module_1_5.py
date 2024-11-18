immutable_var = 'cat', 5, 4.13, True
#immutable_var[0] = 'dog'
print(immutable_var[0])
print(immutable_var), print(type(immutable_var))
# Вторая строка взята под #, чтобы не рушить дальнейший код. Если убрать #, вылезет ошибка и работа остановится.
# Переменная "immutable_var" не меняется потому, что её тип - tupple, является неизменяемым, и не важно, находится в списке.
# Однако, мы всё ещё можем работать с частями списка, например...
print(immutable_var[1] + 5)
# Тип list тоже является списком, но его составляющие можно изменить.
mutable_list = ['dog', 6, 3.14, False]
print(type(mutable_list))
print(mutable_list)
mutable_list[0] = 'parrot'
mutable_list[3] = 'penguin'
print(mutable_list)