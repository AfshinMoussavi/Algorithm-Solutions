// Name: بله یا خیر؟
// URL:  https://quera.org/problemset/106381

package main

import "fmt"

func main() {
	var input string
	fmt.Scan(&input)
	items := []string{}
	for index, _ := range input {
		if index+4 <= len(input) {
			if input[index:index+4] == "bale" {
				items = append(items, "bale")
				index += 3
			}
		}

		if index+5 <= len(input) {
			if input[index:index+5] == "kheir" {
				items = append(items, "kheir")
				index += 4
			}
		}

		if index+4 <= len(input) {
			if input[index:index+4] == "areh" {
				items = append(items, "areh")
				index += 3
			}
		}

		if index+2 <= len(input) {
			if input[index:index+2] == "na" {
				items = append(items, "na")
				index += 1
			}
		}

	}

	if len(items)%2 != 0 {
		fmt.Println("NO")
		return
	}

	stack := []string{}
	for _, item := range items {
		if item == "bale" || item == "areh" {
			stack = append(stack, item)
		} else if item == "kheir" {
			if len(stack) == 0 || stack[len(stack)-1] != "bale" {
				fmt.Println("NO")
				return
			}
			stack = stack[:len(stack)-1]
		} else if item == "na" {
			if len(stack) == 0 || stack[len(stack)-1] != "areh" {
				fmt.Println("NO")
				return
			}
			stack = stack[:len(stack)-1]
		}
	}
	if len(stack) == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}