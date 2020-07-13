;Find the number of nodes on a given level K of an n-ary tree
(defun nodes(L LVL K)
	(cond
		( (null L)	nil)
		( (and (equal LVL K)(atom L))	1)
		( (listp L)	(apply #'+ (mapcar #'(lambda(X)
					(nodes X (+ 1 LVL) K)			
							) L )))
		( t	0)
	)
)

(defun nodesWrap(L K)
	(nodes L -1 K)
)
(print (nodesWrap '(a b (c d e)) 1))