; c) Write a function that, with a list given as parameter, inverts only continuous
;  sequences of atoms. Example:
;  (a b c (d (e f) g h i)) ==> (c b a (d (f e) i h g))

(defun my_reverse (l)
    (if (null l)
        nil
        (my_append (my_reverse (cdr l)) (list (car l)))
    )        
)

(defun inv_list (l aux)
    (cond
        ((null l) (my_reverse aux))
        ((listp (car l)) (my_append (my_reverse aux) (cons (inv_list (car l) nil) (inv_list (cdr l) nil))))
        (T (inv_list (cdr l) (my_append aux (list (car l)))))
    )
)

(print (inv_list '(a b c (d (e f) g h i)) nil))
