package main

import (
	"fmt"
	"time"
)

/*
This is an example to remind myself how concurrent channels work in Go
*/

func main() {
	// This is how you make channels
	c1 := make(chan string)
	c2 := make(chan string)

	// These are anonymous functions that just run
	// Note the use of `for` here makes these inifinite
	go func() {
		for {
			c1 <- "500ms"
			time.Sleep(time.Millisecond * 500)
		}
	}()

	go func() {
		for {
			c2 <- "2s"
			time.Sleep(time.Second * 2)
		}
	}()

	// infinitely collect the values from each channel when they come in
	for {
		select {
		case msg1 := <-c1:
			fmt.Println(msg1)
		case msg2 := <-c2:
			fmt.Println(msg2)
		}
	}
}
