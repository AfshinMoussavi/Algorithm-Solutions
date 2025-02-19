// Name: کتاب‌خانه‌ی پردردسر
// URL:  https://quera.org/problemset/181681

package library

import (
	"strings"
)

type Library struct {
	capacity int
	books    map[string]string
}

func NewLibrary(capacity int) *Library {
	return &Library{
		capacity: capacity,
		books:    make(map[string]string),
	}
}

func (library *Library) AddBook(name string) string {
	for key := range library.books {
		if strings.ToLower(key) == strings.ToLower(name) {
			return "The book is already in the library"
		}
	}

	if len(library.books) == library.capacity {
		return "Not enough capacity"
	}

	library.books[name] = ""
	return "OK"
}

func (library *Library) BorrowBook(bookName, personName string) string {
	for key, borrower := range library.books {
		if strings.ToLower(key) == strings.ToLower(bookName) {
			if borrower != "" {
				return "The book is already borrowed by " + borrower
			}
			library.books[key] = personName
			return "OK"
		}
	}

	return "The book is not defined in the library"
}

func (library *Library) ReturnBook(bookName string) string {
	for key, borrower := range library.books {
		if strings.ToLower(key) == strings.ToLower(bookName) {
			if borrower == "" {
				return "The book has not been borrowed"
			}
			library.books[key] = ""
			return "OK"
		}
	}

	return "The book is not defined in the library"
}
