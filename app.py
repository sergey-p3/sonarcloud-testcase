print(" ".join(list(map(lambda number : [[str(number), "Fizz"], ["Buzz", "FizzBuzz"]][number % 5 == 0][number % 3 == 0], range(1, 21)))))
