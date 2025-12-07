//  Name: برآورد هزینه رویداد
// URL:  https://quera.org/problemset/306523

package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	var ans int64
	var s, c int64
	for i := 0; i < n; i++ {
		_, _ = fmt.Scan(&s, &c)
		ans += s * c
	}

	fmt.Println(ans)
}
