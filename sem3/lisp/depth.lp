;Find the depth of a given n-ary tree.
(defun depth(L)
	(cond
		((atom L)	0)
		(T	(+ 1 (apply #'max (mapcar #'depth L))))
	)
)

