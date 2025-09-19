// Name: کتاب‌خانه‌ی پردردسر
// URL:  https://quera.org/problemset/181681

package library

import "strings"

const (
	msgNotBorrowed       = "The book has not been borrowed"
	msgAlreadyBorrowed   = "The book is already borrowed by "
	msgAlreadyInLib      = "The book is already in the library"
	msgNotDefined        = "The book is not defined in the library"
	msgNotEnoughCapacity = "Not enough capacity"
	msgOK                = "OK"
)

type Book struct {
	Title    string
	Borrower string
}

type Library struct {
	capacity int
	books    map[string]*Book
}

func NewLibrary(capacity int) *Library {
	if capacity < 0 {
		capacity = 0
	}

	return &Library{
		capacity: capacity,
		books:    make(map[string]*Book, capacity),
	}
}

func (library *Library) AddBook(name string) string {
	key := strings.ToLower(strings.TrimSpace(name))

	if _, exists := library.books[key]; exists {
		return msgAlreadyInLib
	}

	if len(library.books) >= library.capacity {
		return msgNotEnoughCapacity
	}

	library.books[key] = &Book{Title: name}

	return msgOK
}

func (library *Library) BorrowBook(bookName, personName string) string {
	key := strings.ToLower(strings.TrimSpace(bookName))

	b, ok := library.books[key]
	if !ok {
		return msgNotDefined
	}

	if b.Borrower != "" {
		return msgAlreadyBorrowed + b.Borrower
	}

	b.Borrower = strings.TrimSpace(personName)

	return msgOK
}

func (library *Library) ReturnBook(bookName string) string {
	key := strings.ToLower(strings.TrimSpace(bookName))

	b, ok := library.books[key]
	if !ok {
		return msgNotDefined
	}

	if b.Borrower == "" {
		return msgNotBorrowed
	}

	b.Borrower = ""

	return msgOK
}
