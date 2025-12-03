package main

import (
	"aoc/utils"
	"fmt"
	"strconv"
)

const FILENAME = "input.txt"

func processLine(line string) int {
	currMax := 0
	lenLine := len(line)
	for i := range lenLine {
		iNum := string(line[i])
		for j := i + 1; j < lenLine; j++ {
			jNum := string(line[j])

			ijNum := iNum + jNum
			ijNumInt, err := strconv.Atoi(ijNum)
			if err != nil {
				panic(err)
			}

			currMax = max(currMax, ijNumInt)
		}
	}
	return currMax
}

func processLines(lines []string) int {
	tot := 0
	for _, line := range lines {
		tot += processLine(line)
	}
	return tot
}

// 12 + 1: iterate through the string to remove one character and see if it's the biggest.
func getMaxS(s string) string {
	maxS := ""
	maxSInt := 0
	for i := range len(s) {
		sMinusChar := s[:i] + s[i+1:]
		sMinusCharInt, err := strconv.Atoi(sMinusChar)
		if err != nil {
			panic(err)
		}
		if sMinusCharInt > maxSInt {
			maxS = sMinusChar
			maxSInt = sMinusCharInt
		}
	}
	return maxS
}

func processLinePart2(line string) int {
	currMax := 0
	n := 12

	// Take the last 12 characters.
	s := line[len(line)-n:]

	// Reverse iterate through the rest of the string.
	for i := len(line) - n - 1; i >= 0; i-- {
		char := string(line[i])
		sPlusChar := char + s
		maxSPlusChar := getMaxS(sPlusChar)
		maxSPlusCharInt, err := strconv.Atoi(maxSPlusChar)
		if err != nil {
			panic(err)
		}
		currMax = max(currMax, maxSPlusCharInt)
		s = maxSPlusChar
	}

	return currMax
}

func processLinesPart2(lines []string) int {
	tot := 0
	for _, line := range lines {
		tot += processLinePart2(line)
	}
	return tot
}

func main() {
	lines := utils.ReadLines(FILENAME)
	fmt.Println("Part 1: ", processLines(lines))
	fmt.Println("Part 2: ", processLinesPart2(lines))
}
