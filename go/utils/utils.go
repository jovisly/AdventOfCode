package utils

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
)

// ReadLines reads all lines from a file and returns them as a slice of strings.
func ReadLines(filename string) []string {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return lines
}

// ReadFile reads the entire file as a single string.
func ReadFile(filename string) string {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	content, err := io.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	}

	return string(content)
}


// P represents a point (i, j) on a board.
type P [2]int

// Board represents a 2D board as a map from coordinates to values.
type Board map[P]string

// Equivalent to:
// https://github.com/jovisly/AdventOfCode/blob/b65a96f35363531cf0b03f8dacd30aae75be7a68/templates/utils.py#L83C1-L91C1
func GetBoard(lines []string) Board {
	board := make(Board)
	for i, row := range lines {
		for j, char := range row {
			board[P{i, j}] = string(char)
		}
	}
	return board
}

// Return a position's 4 neighbors (up, down, left, right).
// Return only positions that exists on the board.
func GetNeighbors4(board Board, pos P) []P {
	neighbors := []P{}
	_, exists := board[P{pos[0] - 1, pos[1]}]
	if exists {
		neighbors = append(neighbors, P{pos[0] - 1, pos[1]})
	}
	_, exists = board[P{pos[0] + 1, pos[1]}]
	if exists {
		neighbors = append(neighbors, P{pos[0] + 1, pos[1]})
	}
	_, exists = board[P{pos[0], pos[1] - 1}]
	if exists {
		neighbors = append(neighbors, P{pos[0], pos[1] - 1})
	}
	_, exists = board[P{pos[0], pos[1] + 1}]
	if exists {
		neighbors = append(neighbors, P{pos[0], pos[1] + 1})
	}
	return neighbors
}

func GetNeighbors8(board Board, pos P) []P {
	// Start with the 4 cardinal neighbors
	neighbors := GetNeighbors4(board, pos)

	// Add the 4 diagonal neighbors
	diagonals := []P{
		{pos[0] - 1, pos[1] - 1},
		{pos[0] - 1, pos[1] + 1},
		{pos[0] + 1, pos[1] - 1},
		{pos[0] + 1, pos[1] + 1},
	}

	for _, diag := range diagonals {
		_, exists := board[diag]
		if exists {
			neighbors = append(neighbors, diag)
		}
	}

	return neighbors
}

// Return the values of a position's 4 neighbors.
func GetNeighborValues4(board Board, pos P) []string {
	neighbors := GetNeighbors4(board, pos)
	values := []string{}
	for _, neighbor := range neighbors {
		values = append(values, board[neighbor])
	}
	return values
}

func GetNeighborValues8(board Board, pos P) []string {
	neighbors := GetNeighbors8(board, pos)
	values := []string{}
	for _, neighbor := range neighbors {
		values = append(values, board[neighbor])
	}
	return values
}


func VisualizeBoard(board Board) {
	if len(board) == 0 {
		return
	}

	maxRow, maxCol := 0, 0
	for pos := range board {
		if pos[0] > maxRow {
			maxRow = pos[0]
		}
		if pos[1] > maxCol {
			maxCol = pos[1]
		}
	}

	for i := 0; i <= maxRow; i++ {
		line := ""
		for j := 0; j <= maxCol; j++ {
			line += board[P{i, j}]
		}
		fmt.Println(line)
	}
}
