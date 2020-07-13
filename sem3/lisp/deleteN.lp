; a) Write a function to eliminate the n-th element of a linear list.

(defun deleteN (l n)
    (cond
        ((null l) nil)
        ((= n 1) (cdr l))
        (T (cons (car l) (deleteN (cdr l) (- n 1))))
    )
)

(print (deleteN '(1 2 3 4 5 6 7 8) 5))
