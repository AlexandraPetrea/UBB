; b) Write a function to replace the first occurence of an element E in a given list with an other element O.

(defun replaceFirstElement (l e o)
    (cond
        ((null l) nil)
        ((= (car l) e) (cons o (cdr l)))
        (T (cons (car l) (replaceFirstElement (cdr l) e o)))
    )
)

(print (replaceFirstElement '(1 2 3 4 5 6 7 6 4 6) 6 0))
;=> (1 2 3 4 5 0 7 6 4 6) 
