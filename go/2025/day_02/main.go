package main

import (
	"aoc/utils"
	"fmt"
	"strconv"
	"strings"
)

const FILENAME = "input.txt"

func isValid(num int) bool {
	// Convert to str.
	str := strconv.Itoa(num)

	// If num digits is odd, then it's valid.
	if len(str)%2 == 1 {
		return true
	}

	// If num digits is even, split half and compare the two chunks.
	half := len(str) / 2
	first := str[:half]
	second := str[half:]
	return first != second
}

func sumInvalidDigits(part string) int {
	// Split part by "-".
	parts := strings.Split(part, "-")
	num1, err := strconv.Atoi(parts[0])
	if err != nil {
		panic(err)
	}
	num2, err := strconv.Atoi(parts[1])
	if err != nil {
		panic(err)
	}

	// Iterate through the numbers
	tot := 0
	for num := num1; num <= num2; num++ {
		// Check if the number is invalid.
		if !isValid(num) {
			tot += num
		}
	}
	return tot
}

func processLine(line string) int {
	// Split the line by commas.
	parts := strings.Split(line, ",")
	tot := 0
	for _, part := range parts {
		tot += sumInvalidDigits(part)
	}
	return tot
}

func main() {
	lines := utils.ReadLines(FILENAME)
	// IMPLEMENT
	fmt.Println("Part 1: ", processLine(lines[0]))
	fmt.Println("Part 2: ", len(lines))
}
