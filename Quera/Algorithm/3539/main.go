// Name: تک‌رقمی
// URL:  https://quera.org/problemset/3539

package main

import "fmt"

func main() {
	var n string
	fmt.Scan(&n)
	for true {
		result := 0
		for index, _ := range n {
			result += int(n[index] - '0')
		}
		if result < 10 {
			fmt.Println(result)
			break
		}
		n = fmt.Sprintf("%d", result)
	}

}