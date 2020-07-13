; a) Write a function that merges two sorted linear lists and keeps double values.

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