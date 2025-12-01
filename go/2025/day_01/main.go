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

func getModPos(pos int, num int) (int, int) {
	if pos > 99 {
		return getModPos(pos - 100, num + 1)
	}

	if pos < 0 {
		return getModPos(pos + 100, num + 1)
	}

	return pos, num
}


func main() {
	lines := utils.ReadLines(FILENAME)
	pos := 50
	count := 0
	for _, line := range lines {
		direction, amount := processLine(line)
		if direction == "L" {
			pos -= amount
		} else {
			pos += amount
		}
		// Wrap.
		newPos, _ := getModPos(pos, 0)
		// fmt.Println("The dial is roated: ", line, "pos: ", newPos)
		if newPos == 0 {
			count++
		}
		pos = newPos
	}
	fmt.Println("Part 1: ", count)

	// Reset for Part 2.
	pos = 50
	count = 0
	for _, line := range lines {
		direction, amount := processLine(line)
		if direction == "L" {
			pos -= amount
		} else {
			pos += amount
		}
		// Wrap.
		newPos, num := getModPos(pos, 0)
		fmt.Println("The dial is roated: ", line, "pos: ", newPos, "num: ", num)
		count += num
		// if newPos == 0 {
		// 	count++
		// }
		pos = newPos
	}

	if pos == 0 {
		count++
	}
	fmt.Println("Part 2: ", count)
}

// 2651 is wrong
// 6671 is still wrong (and it's someone else's answer lol how)
