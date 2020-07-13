; d) Build a list which contains positions of a minimum numeric element from a given linear list.

(defun my_min (a b)
    (if (< a b) a b)
)

(defun pos (l e i)
    (cond
        ((null l) nil)
        ((equal (car l) e) (cons i (pos (cdr l) e (+ i 1))))
        (T (pos (cdr l) e (+ i 1)))
    )
)

(defun my_length (l)
    (cond
        ((atom l) 1)
        (T (apply '+ (mapcar 'my_length l)))
    )
)

(defun min_list (l)
    (if (equal (my_length l) 1)
        (car l)
        (my_min (car l) (min_list (cdr l)))
    )
)

(defun solve (l)
    (pos l (min_list l) 1)
)

(print (solve '(3 2 5 6 2 7 7 2 3 9)))