// Name: مدیریت زمان نیما
// URL:  https://quera.org/problemset/181680

package main

import "fmt"

func main() {
	var w, s, i int
	fmt.Scan(&w, &s, &i)

	result := 24 - ((w - i) + (s - i) + i)
	fmt.Println(result)

}