// The question that makes me miss python :p
package main

import (
	"aoc/utils"
	"fmt"
	"strconv"
	"strings"
)

const FILENAME = "input.txt"

func cleanStrings(list_s []string) []string {
	cleaned := []string{}
	for _, s := range list_s {
		trimmed := strings.TrimSpace(s)
		if trimmed != "" {
			cleaned = append(cleaned, trimmed)
		}
	}
	return cleaned
}

func processLinesP1(lines []string) int {
	processedLines := [][]string{}
	for _, line := range lines {
		segs := strings.Split(line, " ")
		cleanedSegs := cleanStrings(segs)
		processedLines = append(processedLines, cleanedSegs)
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
			num, err := strconv.Atoi(strings.TrimSpace(string(line[i])))
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
	ops := strings.Split(opsString, " ")
	ops = cleanStrings(ops)
	// Reverse
	for i, j := 0, len(ops)-1; i < j; i, j = i+1, j-1 {
		ops[i], ops[j] = ops[j], ops[i]
	}

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
