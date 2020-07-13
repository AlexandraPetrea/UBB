;Replace all the nodes on a given level K of an n-ary tree with a given value E

(defun replaceNode(X LVL K E)
	(cond
		( (null X)	nil)
		( ( and (atom X) (equal LVL K))	E)
		( (listp X)	 (mapcar #'(lambda(Y)
								(replaceNode Y (+ 1 LVL) K E)
								) X))
		( t	X)
	)
)

(defun replaceNodeWrap(X K E)
	(replaceNode X -1 K E)
)