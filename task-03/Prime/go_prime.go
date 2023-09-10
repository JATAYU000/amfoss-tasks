package main

import "fmt"

func main() {
	var n int
	fmt.Println("enter the num: ")
	fmt.Scan(&n)
	
	if n == 1 || n ==0{
		fmt.Println("no prime")
	
	} else if n ==2 {
		fmt.Println("2")
	
	} else {
		for i:=2;i<=n;i++{
			k:=0
			for j:=2;j<=i;j++{
				if i%j !=0 {
					k++
				}
			}
			if k == i-2{
				fmt.Println(i)
			}
		}
	
	}
}