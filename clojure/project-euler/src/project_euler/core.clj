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
(defn smallest-multiple
  [range-end]
  (let [prime-factors (map #(primes/prime-factors %) (range 1 (inc range-end)))
        freqs (map frequencies prime-factors)
        factor-counts (apply merge-with #(if (> %1 %2) %1 %2) freqs)]
    (reduce * (map (fn [[k v]] (int (Math/pow k v))) factor-counts))))

(smallest-multiple 20)

;; 6
(- (int (Math/pow (reduce + (range 1 101)) 2)) (int (reduce + (map #(Math/pow % 2) (range 1 101)))))

;; 7
(nth (primes/lazy-primes) (dec 10001))