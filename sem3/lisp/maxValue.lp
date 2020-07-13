; d) Write a list to return the maximum value of the numerical atoms from a list, at superficial level.

(defun my_max (a b)
    (cond
        ((and (not (numberp a)) (not (numberp b))) nil)
        ((not (numberp a)) b)
        ((not (numberp b)) a)
        ((> a b) a)
        (T b)
    )
)

(defun max_list (l)
    (if (null (cdr l)) 
        (car l)
        (my_max (car l) (max_list (cdr l)))
    )
)

(print (max_list '(A 1 B 4 5 3 C F)))