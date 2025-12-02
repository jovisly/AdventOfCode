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

func isValidPart2(num int) bool {
	str := strconv.Itoa(num)
	lenStr := len(str)

	for i := 0; i < lenStr/2+1; i++ {
		subStr := str[:i]

		if len(subStr) > 0 && lenStr%len(subStr) == 0 {
			repeat := lenStr / len(subStr)
			repeatedStr := strings.Repeat(subStr, repeat)
			if repeatedStr == str {
				return false
			}
		}
	}

	return true
}

func sumInvalidDigits(part string, partNum int) int {
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
		if partNum == 1 {
			if !isValid(num) {
				tot += num
			}
		} else {
			if !isValidPart2(num) {
				tot += num
			}
		}
	}
	return tot
}

func processLine(line string, partNum int) int {
	// Split the line by commas.
	parts := strings.Split(line, ",")
	tot := 0
	for _, part := range parts {
		tot += sumInvalidDigits(part, partNum)
	}
	return tot
}

func main() {
	lines := utils.ReadLines(FILENAME)
	fmt.Println("Part 1: ", processLine(lines[0], 1))
	fmt.Println("Part 2: ", processLine(lines[0], 2))

	// fmt.Print(isValidPart2(12345))
	// fmt.Print(isValidPart2(1234512345))
	// fmt.Print(isValidPart2(123451234))
}
