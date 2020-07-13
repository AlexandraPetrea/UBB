; c) Write a function to determine the number of all sublists of a given list, on any level.
;  A sublist is either the list itself, or any element that is a list, at any level. Example:
;  (1 2 (3 (4 5) (6 7)) 8 (9 10)) => 5 lists:
;  (list itself, (3 ...), (4 5), (6 7), (9 10)).

(defun countList (l)
    (cond
        ((atom l) 0)
        ((listp l) (+ 1 (apply '+ (mapcar 'countList l))))
    )
)

(print (countList '(1 2 (3 (4 5) (6 7)) 8 (9 10))))