; c) Remove all occurrences of a maximum numerical element from a nonlinear list.

(defun max_nb (a b)
    (if (> a b) a b)
)


(defun max_num (l)
    (cond
        ((null l) -1)
        ((and (null (cdr l)) (numberp (car l))) (car l))
        ((numberp (car l)) (max_nb (car l) (max_num (cdr l))))
        ((listp (car l)) (max_nb (max_num (car l)) (max_num (cdr l))))
        (t (max_num (cdr l)))
     )
)

(print (max_num '(1 2 (3 (a) (1 3)) 4 5)))
; => 5
