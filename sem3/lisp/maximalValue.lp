; b) Write a function to return the maximum value of all the numerical atoms of a list, at any level.

(defun maxL (l)
    (cond
        ((numberp l) l)
        ((atom l) -1)
        (T (apply 'max (mapcar 'maxL l)))
    )
)

(print (maxL '(1 A (B C) ((5) 8))))
;=> 8