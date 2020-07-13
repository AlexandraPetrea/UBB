; a) Write a function to test whether a list is linear.

(defun liniarList (l)
    (cond
        ((null l) T)
        ((listp (car l)) nil)
        (T (liniarList (cdr l)))
    )
)

(print (liniarList '(a (b c) (d (e (f))))))
;=> nil

(print (liniarList '(1 2 3 4)))
;=> T
