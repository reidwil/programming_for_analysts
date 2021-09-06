package main

// Make fibbonacci sequence
func fib(n int) int {
	if n <= 0 {
		return n
	}
	return fib(n-1) + fib(n-2)
}

func worker(send <-chan int, receive chan<- int) {
	for n := range send {
		results <- fib(n)
	}
}

func main() {
	send := make(chan int, 100)
	receive := make(chan int, 100)

	go worker(send, receive)

}
