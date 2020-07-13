; b) Write a function to test if a linear list of integer numbers has a "valley" aspect (a list has a valley
; aspect if the items decrease to a certain point and then increase. Eg. 10 8 6 17 19 20). A list must
; have at least 3 elements to fulfill this condition.

(defun _valley (l decreasing)
	(cond
		((= (list-length l) 1) (if decreasing nil T))
		((and (> (car l) (cadr l)) (not decreasing)) nil)
		((and (< (car l) (cadr l)) decreasing) (_valley (cdr l) nil))
		(T (_valley (cdr l) decreasing))
	)
)

(defun valley (l)
	(if (< (list-length l) 3)
		nil
		(_valley l T)
	)
)

(print (valley '(5 4 3 4)))
; => T
