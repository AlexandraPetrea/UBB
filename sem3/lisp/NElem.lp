; a) Write a function to return the n-th element of a list, or NIL if such an element does not exist;

; _n_elem (l n pos) = 
    ; nil, n = 0
    ; l0, n = pos
    ; _n_elem(l1...ln, n, pos + 1)

(defun _n_elem (l n pos)
    (cond
        ((null l) nil)
        ((= n pos) (car l))
        (T (_n_elem (cdr l) n (+ pos 1)))
    )
)

(defun n_elem (l n)
    (_n_elem l n 1)
)

(print (n_elem '(1 2 3 4 5 6 7 8 9 10) '5))