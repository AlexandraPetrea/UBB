;Find the level of a given node. The root has level 0 (n-ary trees)
(defun level(L N)
	(cond
		((atom L)	0)
		((exists L N) (+ 1 (apply #'+ (mapcar #'(lambda(L) (level L N)) L ))))
		(T	 (apply #'+ (mapcar #'(lambda(L) (level L N)) L )) )
	)
)

(defun levelWrap(L N)
	(- (level L N) 1)
)