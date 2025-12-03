package main

import (
	"aoc/utils"
	"fmt"
	"strconv"
)

const FILENAME = "input_test.txt"

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

// remove characters from a string at the specified indices
func removeIndices(s string, indices []int) string {
	result := ""
	for i := range s {
		shouldRemove := false
		for _, idx := range indices {
			if i == idx {
				shouldRemove = true
				break
			}
		}
		if !shouldRemove {
			result += string(s[i])
		}
	}
	return result
}

func processLinePart2(line string) int {
	currMax := 0
	lenLine := len(line)
	for i := range lenLine {
		for j := i + 1; j < lenLine; j++ {
			for k := j + 1; k < lenLine; k++ {
				indices := []int{i, j, k}
				newLine := removeIndices(line, indices)
				newInt, err := strconv.Atoi(newLine)
				if err != nil {
					panic(err)
				}
				currMax = max(currMax, newInt)
			}
		}
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
