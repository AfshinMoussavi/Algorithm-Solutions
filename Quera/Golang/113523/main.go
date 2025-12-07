package main

import (
	"errors"
	"fmt"

	"snapp/helper"
	"snapp/the_lib"
)

func main() {
	// تست LoadData
	_, err := the_lib.LoadData()
	if err != nil {
		if errors.Is(err, helper.ErrNoPath) {
			fmt.Println("Matched:", err)
		}
	}

	// تست LoadDataWithPath
	_, err = the_lib.LoadDataWithPath("short")
	if err != nil {
		if errors.Is(err, helper.ErrPathShort) {
			fmt.Println("Matched:", err)
		}
	}

	// تست Manipulate
	data := &the_lib.Data{}
	err = data.Manipulate(nil)
	if err != nil {
		if errors.Is(err, helper.ErrDataNil) {
			fmt.Println("Matched:", err)
		}
	}
}
