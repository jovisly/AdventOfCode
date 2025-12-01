package main

import (
	"aoc/utils"
	"fmt"
	"log"
	"strconv"
	"strings"
)

const FILENAME = "input.txt"

func processLine(line string) (x1, y1, x2, y2 int) {
	parts := strings.Split(line, "->")
	part1 := strings.Split(parts[0], ",")
	part2 := strings.Split(parts[1], ",")
	x1, err := strconv.Atoi(strings.TrimSpace(part1[0]))
	if err != nil {
		log.Fatal(err)
	}
	y1, err = strconv.Atoi(strings.TrimSpace(part1[1]))
	if err != nil {
		log.Fatal(err)
	}
	x2, err = strconv.Atoi(strings.TrimSpace(part2[0]))
	if err != nil {
		log.Fatal(err)
	}
	y2, err = strconv.Atoi(strings.TrimSpace(part2[1]))
	if err != nil {
		log.Fatal(err)
	}
	return x1, y1, x2, y2
}

func processLinesPart1(lines []string) int {
	// Keep a map of points and the number of times they appear.
	mapPos := make(map[utils.P]int)

	for _, line := range lines {
		x1, y1, x2, y2 := processLine(line)
		if x1 == x2 {
			minY := min(y1, y2)
			maxY := max(y1, y2)
			for y := minY; y <= maxY; y++ {
				mapPos[utils.P{x1, y}]++
			}
		} else if y1 == y2 {
			minX := min(x1, x2)
			maxX := max(x1, x2)
			for x := minX; x <= maxX; x++ {
				mapPos[utils.P{x, y1}]++
			}
		}
	}

	// Count the positions that appear more than twice.
	count := 0
	for _, val := range mapPos {
		if val >= 2 {
			count++
		}
	}
	return count
}

func processLinesPart2(lines []string) int {
	mapPos := make(map[utils.P]int)

	for _, line := range lines {
		x1, y1, x2, y2 := processLine(line)
		// fmt.Println("-----")
		// fmt.Println("line: ", line)
		// fmt.Println("x1: ", x1)
		// fmt.Println("y1: ", y1)
		// fmt.Println("x2: ", x2)
		// fmt.Println("y2: ", y2)

		// Same from Part 1.
		if x1 == x2 {
			minY := min(y1, y2)
			maxY := max(y1, y2)
			for y := minY; y <= maxY; y++ {
				mapPos[utils.P{x1, y}]++
			}
		} else if y1 == y2 {
			minX := min(x1, x2)
			maxX := max(x1, x2)
			for x := minX; x <= maxX; x++ {
				mapPos[utils.P{x, y1}]++
			}
		} else if x1 != x2 && y1 != y2 {
			// Diagonal line - determine step direction
			stepX := 1
			if x1 > x2 {
				stepX = -1
			}
			stepY := 1
			if y1 > y2 {
				stepY = -1
			}

			// Calculate number of steps
			diffX := x2 - x1
			if diffX < 0 {
				diffX = -diffX
			}

			// Iterate from (x1, y1) to (x2, y2)
			for i := 0; i <= diffX; i++ {
				x := x1 + i*stepX
				y := y1 + i*stepY
				mapPos[utils.P{x, y}]++
				// fmt.Println("  adding: ", utils.P{x, y})
			}
		}
	}

	// Count the positions that appear more than twice.
	count := 0
	for _, val := range mapPos {
		if val >= 2 {
			count++
		}
	}
	return count
}

func main() {
	lines := utils.ReadLines(FILENAME)
	count1 := processLinesPart1(lines)
	fmt.Println("Part 1: ", count1)

	count2 := processLinesPart2(lines)
	fmt.Println("Part 2: ", count2)
}
