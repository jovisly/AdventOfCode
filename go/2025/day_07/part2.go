package main

import (
	"aoc/utils"
	"fmt"
)

// Recursively count all unique paths from current position to the end row
// Uses memoization.
func countPaths(pos utils.P, board utils.Board, endRow int, memo map[utils.P]int) int {
	// Check if we've already computed this position
	if cached, exists := memo[pos]; exists {
		return cached
	}

	// Reached the bottom row
	if pos[0] == endRow {
		return 1
	}

	// Get next positions by moving the beam
	nextPositions := moveBeam(pos, board)

	// Sum paths from all branches
	totalPaths := 0
	for _, nextPos := range nextPositions {
		totalPaths += countPaths(nextPos, board, endRow, memo)
	}

	// Cache the result before returning
	memo[pos] = totalPaths
	return totalPaths
}

func Part2() {
	lines := utils.ReadLines(FILENAME)
	board := utils.GetBoard(lines)
	sPos := getStart(board)
	fmt.Printf("Start: %v\n", sPos)
	fmt.Printf("Number of rows: %v\n", len(lines))

	// Start counting from the position right below S
	startPos := utils.P{sPos[0] + 1, sPos[1]}
	endRow := len(lines) - 1

	// Create memoization map to cache results
	memo := make(map[utils.P]int)
	numPaths := countPaths(startPos, board, endRow, memo)

	fmt.Println("Part 2:", numPaths)
}
