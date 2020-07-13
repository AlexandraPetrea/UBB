; d) Write a function to test the equality of two sets, without using the difference of two sets.

(defun remov (l e)
    (cond
        ((null l) nil)
        ((equal (car l) e) (remov (cdr l) e))
        (T (cons (car l) (remov (cdr l) e)))
    )
)

(defun set= (l k)
    (cond
        ((and (null l) (null k)) T)
        ((or (null l) (null k)) nil)
        (T (set= (cdr l) (remov k (car l))))
    )
)

(print (set= '(1 2 7 3) '(1 6 2 3)))