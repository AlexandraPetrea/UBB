; d) Write a function to return the sum of all numerical atoms in a list at superficial level.

(defun sumSup (l)
    (cond
        ((numberp l) l)
        ((atom l) 0)
        ((listp l) (apply '+ (mapcar 'sumSup l)))
    )
)

(print (sumSup '(1 2 (3 (4 5) (6 7)) 8 (9 10 11))))
;=> 66