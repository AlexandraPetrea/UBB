; d) Write a function which returns the product of numerical even atoms from a list, to any level.
(defun productL (l)
    (cond
        ((numberp l) l)
        ((atom l) 1)
        (T (apply '* (mapcar 'productL l)))
    )
)

(print (productL '(1 2 3 (4 5 (6)) (7))))
;=> 5040