(ns project-euler.core
  (:require [project-euler.primes :as primes]))

;; 1
(- (+ (reduce + (range 0 1000 3)) (reduce + (range 0 1000 5)))
   (reduce + (range 0 1000 15)))

;; 2
;; nice lazy fibonacci sequence implementation from wikibooks
(def fib-seq
  (lazy-cat [1 2] (map + (rest fib-seq) fib-seq)))

(reduce + (filter even? (take-while (partial > 4e6) fib-seq)))

;; 3
(last (primes/prime-factors 600851475143))

;; 4
(first (reverse (sort (filter #(= (str %) (clojure.string/reverse (str %))) (flatten (map #(map (partial * %) (range 999 0 -1)) (range 999 0 -1)))))))

;; 5
;; FIXME - most definitely does not work right now
(defn smallest-multiple
  [range-end]
  (letfn [(hcf [a b]
            (first (filter #(= 0 (mod a %)) (filter #(= 0 (mod b %)) (range 1 b)))))
          (contrib [current x]
            (* current (/ x (hcf current x))))]
    (reduce contrib (range 2 range-end))))