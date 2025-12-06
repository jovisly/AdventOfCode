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

	// fmt.Println(processedLines)

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

func main() {
	lines := utils.ReadLines(FILENAME)

	fmt.Println("Part 1: ", processLinesP1(lines))
	// fmt.Println("Part 2: ", len(lines))
}
