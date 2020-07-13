; d) Write a function to return T if a list has an even number of elements on the first level, and NIL on
; the contrary case, without counting the elements of the list.

(defun even_length (l)
    (cond
        ((null l) T)
        ((null (cdr l)) nil)
        (T (even_length (cddr l)))
    )
)

(print (even_length '(1 2 2 4)))
; => T

(print (even_length '(1 2 4 2 4)))
; => nil