; b) Write a function to test if a linear list of numbers has a "mountain" aspect (a list has a "mountain"
; aspect if the items increase to a certain point and then decreases.
;  Eg. (10 18 29 17 11 10). The list must have at least 3 atoms to fullfil this criteria.

(defun _mountain (l decreasing)
	(cond
		((= (list-length l) 1) (if decreasing nil T))
		((and (< (car l) (cadr l)) (not decreasing)) nil)
		((and (> (car l) (cadr l)) decreasing) (_mountain (cdr l) nil))
		(T (_mountain (cdr l) decreasing))
	)
)

(defun mountain (l)
	(if (< (list-length l) 3)
		nil
		(_mountain l T)
	)
)

(print (mountain '(10 18 29 17 11 10)))
; => T

(print (mountain '(10 18 29 17 11 29 10)))
;=> nil
