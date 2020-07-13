; a) Write twice the n-th element of a linear list. Example: for (10 20 30 40 50) and n=3 will produce 
; (10 20 30 30 40 50).

(defun twice (l n)
    (cond
        ((null l) nil)
        ((= n 1) (cons (car l) l))
        (T (cons (car l) (twice (cdr l) (- n 1))))
    )
)

(print (twice '(10 20 30 40 50) 3))
;=> (10 20 30 30 40 50)
