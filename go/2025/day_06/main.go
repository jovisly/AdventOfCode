// The question that makes me miss python :p
package main

import (
	"aoc/utils"
	"fmt"
	"slices"
	"strconv"
	"strings"
)

const FILENAME = "input.txt"

func processLinesP1(lines []string) int {
	processedLines := [][]string{}
	for _, line := range lines {
		segs := strings.Fields(line)
		processedLines = append(processedLines, segs)
	}

	// fmt.Printf("%#v\n", processedLines)

	ops := processedLines[len(processedLines)-1]
	tot := 0

	for i, op := range ops {
		val := 0
		if op == "*" {
			val = 1
		}

		for _, line := range processedLines[:len(processedLines)-1] {
			num, err := strconv.Atoi(line[i])
			if err != nil {
				panic(err)
			}
			if op == "*" {
				val *= num
			}
			if op == "+" {
				val += num
			}
		}

		tot += val
	}

	return tot
}

func processLinesP2(lines []string) int {
	opsString := lines[len(lines)-1]
	ops := strings.Fields(opsString)
	slices.Reverse(ops)

	// fmt.Printf("%#v\n", ops)

	numsStrings := lines[:len(lines)-1]
	// fmt.Printf("%#v\n", numsStrings)

	// We need to pad the numsStrings to equal length by adding space to the end.
	maxLen := 0
	for _, numsString := range numsStrings {
		if len(numsString) > maxLen {
			maxLen = len(numsString)
		}
	}
	for i, numsString := range numsStrings {
		numsStrings[i] = numsString + strings.Repeat(" ", maxLen-len(numsString))
	}

	// fmt.Printf("%#v\n", numsStrings)

	// Then we start to build the array of arrays for the numbers; do it in the reverse
	// order.
	numss := [][]string{}
	nums := []string{}
	for i := maxLen - 1; i >= 0; i-- {
		currNum := ""
		for _, numsString := range numsStrings {
			currNum += string(numsString[i])
		}
		// fmt.Printf("%#v\n", currNum)
		trimmed := strings.TrimSpace(currNum)
		if len(trimmed) == 0 {
			numss = append(numss, nums)
			nums = []string{}
		} else {
			nums = append(nums, trimmed)
		}
	}
	numss = append(numss, nums)
	// fmt.Printf("%#v\n", numss)

	tot := 0

	for i, op := range ops {
		val := 0
		if op == "*" {
			val = 1
		}

		nums := numss[i]
		for _, num := range nums {
			n, err := strconv.Atoi(num)
			if err != nil {
				panic(err)
			}
			if op == "*" {
				val *= n
			}
			if op == "+" {
				val += n
			}
		}

		tot += val
	}

	return tot
}

func main() {
	lines := utils.ReadLines(FILENAME)
	// fmt.Printf("%#v\n", lines)

	fmt.Println("Part 1: ", processLinesP1(lines))
	fmt.Println("Part 2: ", processLinesP2(lines))
}
