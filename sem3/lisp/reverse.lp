; b) Write a function to get from a given list the list of all atoms, on any
;  level, but reverse order. Example:
;  (((A B) C) (D E)) ==> (E D C B A)

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun all_atoms (l)
    (cond
        ((null l) nil)
        ((listp (car l)) (my_append (all_atoms (cdr l)) (all_atoms (car l))))
        (T (my_append (all_atoms (cdr l)) (list (car l))))
    )
)

(print (all_atoms '(((A B) C) (D E))))