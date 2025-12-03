package main

import (
	"aoc/utils"
	"fmt"
	"strconv"
)

const FILENAME = "input.txt"

// For one line, return the direction (L or R), and the rotation amount.
func processLine(line string) (string, int) {
	// Direction is the first char.
	direction := string(line[0])
	// Rotation amount is the rest of the string, converted to an int.
	amount, err := strconv.Atoi(line[1:])
	if err != nil {
		panic(err)
	}
	return direction, amount
}

func moveOne(pos int, direction string) int {
	amount := 1
	if direction == "L" {
		newPos := pos - amount
		if newPos < 0 {
			newPos = 99
		}
		return newPos
	} else {
		newPos := pos + amount
		if newPos > 99 {
			newPos = 0
		}
		return newPos
	}
}

func main() {
	lines := utils.ReadLines(FILENAME)
	pos := 50
	count := 0
	for _, line := range lines {
		direction, amount := processLine(line)
		for range amount {
			pos = moveOne(pos, direction)
		}
		if pos == 0 {
			count++
		}
	}
	fmt.Println("Part 1: ", count)

	// Reset for Part 2.
	pos = 50
	count = 0
	for _, line := range lines {
		direction, amount := processLine(line)
		for range amount {
			pos = moveOne(pos, direction)
			if pos == 0 {
				count++
			}
		}
	}
	fmt.Println("Part 2: ", count)
}
