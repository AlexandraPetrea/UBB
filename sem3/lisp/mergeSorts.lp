; d) Write a function to merge two sorted lists without keeping double values

(defun merge_sorted (a b)
	(cond
		((null a) b)
		((null b) a)
		((<= (car a) (car b)) (cons (car a) (merge_sorted (cdr a) b)))
		(T (cons (car b) (merge_sorted a (cdr b))))
	)
)

(print (merge_sorted '(1 2 3 3) '(3 4 4 5 5 7)))
; => (1 2 3 3 4 4 5 7)


(defun remove_doubles (l)
    (cond
        ((null l) nil)
        ((null (cdr l)) (list (car l)))
        ((= (car l) (cadr l)) (remove_doubles (cdr l)))
        (T (cons (car l) (remove_doubles (cdr l))))
    )
)

(print (remove_doubles '(1 2 3 3 4 4 5 7)))
;=> (1 2 3 4 5 7) 

(defun solve (a b)
    (remove_doubles (merge_sorted a b))
)

(print (solve '(1 2 3 3) '(3 4 4 5 5 7)))
;=> (1 2 3 4 5 7) 